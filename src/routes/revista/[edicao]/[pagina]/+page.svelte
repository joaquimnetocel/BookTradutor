<script lang="ts">
	import { goto } from '$app/navigation';
	import { resolve } from '$app/paths';
	import { page } from '$app/state';
	import { type Balao } from '$lib/types/typeBalao';
	import { tick } from 'svelte';
	import { slide } from 'svelte/transition';

	let { data } = $props();

	let balaoJson = $state<Balao[]>([]);
	let imgElement = $state<HTMLImageElement>();
	let larguraOriginal = $state(0);
	let alturaOriginal = $state(0);
	let estadoIdioma = $state<'ptbr' | 'en'>('ptbr');

	let popupVisivel = $state(false);
	let popupTexto = $state('');
	let popupX = $state(0);
	let popupY = $state(0);
	let popupBalãoIndex = $state<number | null>(null);

	let paginaAtual = $derived(parseInt(page.params.pagina ?? '1'));

	let audio: HTMLAudioElement;

	const asyncEffect = async () => {
		const resultado = await fetch(`/${page.params.edicao}/json/${page.params.pagina}.json`);
		balaoJson = await resultado.json();
		audio = new Audio('/audio/musica_teste.mp3');
	};

	$effect(() => {
		asyncEffect();
	});

	// Fechar popup ao clicar fora
	$effect(() => {
		const fechar = () => ((popupVisivel = false), (popupBalãoIndex = null));
		window.addEventListener('click', fechar);
		return () => window.removeEventListener('click', fechar);
	});

	async function abrirPopup(event: MouseEvent, balao: Balao, index: number) {
		event.stopPropagation();

		// Toggle: se clicar no mesmo balão fecha
		if (popupVisivel && popupBalãoIndex === index) {
			popupVisivel = false;
			popupBalãoIndex = null;
			return;
		}

		const target = event.currentTarget as HTMLElement;
		const container = target.offsetParent as HTMLElement;
		const rect = target.getBoundingClientRect();
		const containerRect = container.getBoundingClientRect();

		const larguraPopup = 260;

		let x = rect.left - containerRect.left + rect.width / 2 - larguraPopup / 2;
		let y = rect.bottom - containerRect.top + 10;

		const larguraContainer = container.offsetWidth;
		if (x + larguraPopup > larguraContainer) x = larguraContainer - larguraPopup - 10;
		if (x < 10) x = 10;

		// Força transição: fecha antes de abrir novo popup
		popupVisivel = false;
		await tick(); // espera o DOM atualizar e aplicar out:slide

		popupTexto = balao[estadoIdioma];
		popupX = x;
		popupY = y;
		popupBalãoIndex = index;
		popupVisivel = true;
	}

	let popupFontSize = $state(14); // tamanho inicial da fonte do popup

	function aumentarFonte() {
		if (popupFontSize < 30) popupFontSize += 2; // limite máximo 30px
	}

	function diminuirFonte() {
		if (popupFontSize > 10) popupFontSize -= 2; // limite mínimo 10px
	}
</script>

<div class="mt-2 mb-2 flex items-center justify-center gap-3">
	<button
		class="classButton disabled:cursor-not-allowed disabled:opacity-50"
		disabled={paginaAtual <= 1}
		onclick={() =>
			paginaAtual > 1 && goto(resolve(`/revista/${page.params.edicao}/${paginaAtual - 1}`))}
	>
		VOLTAR
	</button>

	<select
		value={paginaAtual}
		onchange={(event) => {
			const valorSelecionado = (event.currentTarget as HTMLSelectElement).value;
			goto(resolve(`/revista/${page.params.edicao}/${valorSelecionado}`));
		}}
		class="max-w-20 rounded border p-2"
	>
		{#each Array.from({ length: data.totalPaginas }) as _, p (p)}
			<option value={p + 1}>{p + 1} / {data.totalPaginas}</option>
		{/each}
	</select>

	<button
		class="classButton disabled:cursor-not-allowed disabled:opacity-50"
		disabled={paginaAtual >= data.totalPaginas}
		onclick={() =>
			paginaAtual < data.totalPaginas &&
			goto(resolve(`/revista/${page.params.edicao}/${paginaAtual + 1}`))}
	>
		AVANÇAR
	</button>
</div>

<div class="relative mx-auto w-full">
	<img
		bind:this={imgElement}
		src={`/${page.params.edicao}/${page.params.pagina}.jpg`}
		alt="Quadrinho"
		class="mb-4 block w-full"
		onload={() => {
			if (imgElement) {
				larguraOriginal = imgElement.naturalWidth;
				alturaOriginal = imgElement.naturalHeight;
			}
		}}
	/>

	{#each balaoJson as balao, i (i)}
		<!-- svelte-ignore a11y_consider_explicit_label -->
		<button
			type="button"
			class="absolute cursor-pointer bg-blue-500/30 p-0 lg:bg-transparent lg:hover:bg-red-500/20"
			style="
        left: {(balao.x1 / larguraOriginal) * 100}%;
        top: {(balao.y1 / alturaOriginal) * 100}%;
        width: {((balao.x2 - balao.x1) / larguraOriginal) * 100}%;
        height: {((balao.y2 - balao.y1) / alturaOriginal) * 100}%;
      "
			onclick={(e) => abrirPopup(e, balao, i)}
		></button>
	{/each}

	{#if popupVisivel}
		<div
			class="absolute z-50 w-64"
			style="left: {popupX}px; top: {popupY}px;"
			in:slide={{ duration: 500 }}
			out:slide={{ duration: 150 }}
		>
			<!-- svelte-ignore a11y_click_events_have_key_events -->
			<!-- svelte-ignore a11y_no_static_element_interactions -->
			<div
				class="relative rounded-2xl bg-black p-4 text-white shadow-xl"
				style="font-size: {popupFontSize}px;"
				onclick={(event) => {
					event.stopPropagation(); // ⚡ impede o fechamento do popup
				}}
			>
				{popupTexto}

				<div class="mt-2 flex justify-between gap-1">
					<button
						onclick={() => ((popupVisivel = false), (popupBalãoIndex = null))}
						class="rounded bg-blue-500 px-2 py-1"
					>
						Fechar
					</button>

					<div class="flex gap-1">
						<button onclick={diminuirFonte} class="rounded bg-gray-700 px-2 py-1">-</button>
						<button onclick={aumentarFonte} class="rounded bg-gray-700 px-2 py-1">+</button>
					</div>
				</div>

				<div class="absolute -top-2 left-6 h-4 w-4 rotate-45 bg-black"></div>
			</div>
		</div>
	{/if}
</div>

<div class="mx-auto mb-4 w-full max-w-150">
	<select bind:value={estadoIdioma} class="mx-auto block w-full max-w-50 rounded border p-2">
		<option value="ptbr">Português</option>
		<option value="en">English</option>
	</select>
</div>
