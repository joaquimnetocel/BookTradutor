<script lang="ts">
	import { goto } from '$app/navigation';
	import { resolve } from '$app/paths';
	import { page } from '$app/state';
	import { type Balao } from '$lib/types/typeBalao';
	import { fade, fly } from 'svelte/transition';

	let { data } = $props();

	let balaoJson = $state<Balao[]>([]);
	let imgElement = $state<HTMLImageElement>();
	let larguraOriginal = $state(0);
	let alturaOriginal = $state(0);
	let estadoIdioma = $state<'ptbr' | 'en'>('ptbr');
	let audio: HTMLAudioElement;

	let popupVisivel = $state(false);
	let popupTexto = $state('');
	let popupX = $state(0);
	let popupY = $state(0);

	let paginaAtual = $derived(parseInt(page.params.pagina ?? '1'));

	const asyncEffect = async () => {
		const resultado = await fetch(`/${page.params.edicao}/json/${page.params.pagina}.json`);
		balaoJson = await resultado.json();
		audio = new Audio('/audio/musica_teste.mp3');
	};

	$effect(() => {
		asyncEffect();
	});

	$effect(() => {
		const fechar = () => (popupVisivel = false);
		window.addEventListener('click', fechar);
		return () => window.removeEventListener('click', fechar);
	});
</script>

<div class="text-center">
	<button
		onclick={() =>
			paginaAtual > 1 && goto(resolve(`/revista/${page.params.edicao}/${paginaAtual - 1}`))}
		disabled={paginaAtual <= 1}
	>
		VOLTAR
	</button>

	<select
		value={paginaAtual}
		onchange={(event) => {
			const valorSelecionado = (event.currentTarget as HTMLSelectElement).value;
			goto(resolve(`/revista/${page.params.edicao}/${valorSelecionado}`));
		}}
		class="mx-auto max-w-20 rounded border p-2"
	>
		<!-- eslint-disable-next-line @typescript-eslint/no-unused-vars-->
		{#each Array.from({ length: data.totalPaginas }) as _, p (p)}
			<option value={p + 1}>{p + 1} / {data.totalPaginas}</option>
		{/each}
	</select>

	<button
		onclick={() =>
			paginaAtual < data.totalPaginas &&
			goto(resolve(`/revista/${page.params.edicao}/${paginaAtual + 1}`))}
		disabled={paginaAtual >= data.totalPaginas}
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
			onclick={(event) => {
				event.stopPropagation();

				const rect = (event.currentTarget as HTMLElement).getBoundingClientRect();
				const container = (event.currentTarget as HTMLElement).offsetParent as HTMLElement;
				const containerRect = container.getBoundingClientRect();

				const larguraPopup = 260;

				// 🔥 Centraliza horizontalmente
				let x = rect.left - containerRect.left + rect.width / 2 - larguraPopup / 2;

				let y = rect.bottom - containerRect.top + 10;

				const larguraContainer = container.offsetWidth;

				// 🔥 Ajuste para não sair da tela
				if (x + larguraPopup > larguraContainer) {
					x = larguraContainer - larguraPopup - 10;
				}
				if (x < 10) x = 10;

				popupTexto = balao[estadoIdioma];
				popupX = x;
				popupY = y;
				popupVisivel = true;
			}}
		></button>
	{/each}

	{#if popupVisivel}
		<!-- in:fade={{ duration: 200 }} -->
		<div
			class="absolute z-50 w-64"
			style="left: {popupX}px; top: {popupY}px;"
			in:fly={{ y: 10, duration: 200 }}
			out:fade={{ duration: 150 }}
		>
			<div class="relative rounded-2xl bg-black p-4 text-sm text-white shadow-xl">
				{popupTexto}
				<br /><button onclick={() => (popupVisivel = false)} class="bg-blue-500">aaaa</button>
				<br /><button onclick={() => alert(22)} class="bg-blue-500">aaaa</button>

				<!-- Pontinha do balão -->
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

<!-- 


<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/state';
	import { type Balao } from '$lib/types/typeBalao';

	let { data } = $props();

	let balaoJson = $state<Balao[]>([]);
	let imgElement = $state<HTMLImageElement>();
	let larguraOriginal = $state(0);
	let alturaOriginal = $state(0);
	let estadoIdioma = $state<'ptbr' | 'en'>('ptbr');
	let audio: HTMLAudioElement;

	let paginaAtual = $derived(parseInt(page.params.pagina ?? '1'));

	const asyncEffect = async () => {
		const resultado = await fetch(`/${page.params.edicao}/json/${page.params.pagina}.json`);
		balaoJson = await resultado.json();
		audio = new Audio('/audio/musica_teste.mp3');
	};

	$effect(() => {
		asyncEffect();
	});
</script>

<div class='text-center'>
<button
	onclick={() => {
		if (paginaAtual > 1) {
			goto(`/revista/${page.params.edicao}/${paginaAtual - 1}`);
		}
	}}
	disabled={paginaAtual <= 1}
>
	VOLTAR
</button>

<select
	onchange={(event) => {
		const select = event.currentTarget as HTMLSelectElement;
		const valorSelecionado = select.value;
		goto(`/revista/${page.params.edicao}/${valorSelecionado}`);
	}}
  class='mx-auto max-w-20 rounded border p-2'
>
	{#each Array.from({ length: data.totalPaginas }) as _, p}
		<option value={p + 1}>{p + 1} / {data.totalPaginas}</option>
	{/each}
</select>


<button
	onclick={() => {
		if (paginaAtual < data.totalPaginas) {
			goto(`/revista/${page.params.edicao}/${paginaAtual + 1}`);
		}
	}}
	disabled={paginaAtual >= data.totalPaginas}
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
				console.log('Largura original:', larguraOriginal, 'Altura original:', alturaOriginal);
			}
		}}
	/>

	{#each balaoJson as balao}
		<button
			type="button"
			class="absolute cursor-pointer bg-blue-500/30 p-0 lg:bg-transparent lg:hover:bg-red-500/20"
			aria-label="Clique para ver o diálogo: {balao[estadoIdioma]}"
			style="
        left: {(balao.x1 / larguraOriginal) * 100}%;
        top: {(balao.y1 / alturaOriginal) * 100}%;
        width: {((balao.x2 - balao.x1) / larguraOriginal) * 100}%;
        height: {((balao.y2 - balao.y1) / alturaOriginal) * 100}%;
      "
      onclick={() => {
        alert(balao[estadoIdioma]);
        // if (audio) {
        //   audio.currentTime = 0;
        //   audio.play();
        // }
      }}
		></button>
	{/each}
</div>

<div class="mx-auto mb-4 w-full max-w-150">
	<select bind:value={estadoIdioma} class="mx-auto block w-full max-w-50 rounded border p-2">
		<option value="ptbr">Português</option>
		<option value="en">English</option>
	</select>
</div> -->
