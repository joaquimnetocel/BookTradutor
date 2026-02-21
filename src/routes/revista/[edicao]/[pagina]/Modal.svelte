<script lang="ts">
	import TextToSpeech from './TextToSpeech.svelte';

	let modal = $state<HTMLDialogElement>();
	let palavraSelecionada = $state(''); // Estado para armazenar o texto atual
	let palavraSelecionadaOriginal = $state(''); // Estado para armazenar o texto atual

	let {
		traducaopp,
		original,
		traducao,
		voz
	}: { traducaopp: string[]; original: string[]; traducao: string[]; voz: string } = $props();

	function abrir(traducao: string, original: string) {
		palavraSelecionada = traducao; // Atualiza o conteúdo
		palavraSelecionadaOriginal = original; // Atualiza o conteúdo
		modal?.showModal(); // Abre o modal único
	}
</script>

{#each traducaopp as traducaocorrente, i (i)}
	{@const primeiroCaracter = traducaocorrente.slice(0, 1)}
	{#if primeiroCaracter === '*'}
		<button
			onclick={() => abrir(traducaocorrente.slice(1), original[i])}
			class="cursor-pointer bg-[lightcyan] px-1 font-bold text-[#0d6efd]"
		>
			{original[i]}
		</button>&nbsp;&nbsp;
	{:else}
		<span class="tooltip-container">
			{original[i]}
			<div class="tooltip-text">
				{traducaocorrente}
			</div>
		</span>
	{/if}
{/each}
<br />
<div class="mt-2">
	<TextToSpeech texto={original.join(' ')} {voz} />
</div>

<br />
{traducao.join(' ')}

<dialog bind:this={modal} class="daisy-modal">
	<div class="daisy-modal-box">
		<h3 class="text-lg font-bold">{palavraSelecionadaOriginal}</h3>
		<h3 class="text-lg font-bold">{palavraSelecionada}</h3>
		<p class="py-4">Pressione ESC ou clique fora para fechar.</p>
		<!-- <div class="modal-action">
			<form method="dialog">
				<button class="btn">Fechar</button>
			</form>
		</div> -->
	</div>
	<form method="dialog" class="daisy-modal-backdrop">
		<button>close</button>
	</form>
</dialog>

<style>
	/* Tooltip padrão (desktop) */
	:global(.tooltip-text) {
		visibility: hidden;
		opacity: 0;
		transition: opacity 0.2s ease;

		position: absolute;
		bottom: 100%;
		left: 50%;
		transform: translateX(-50%);

		background: #333;
		color: #fff;
		padding: 8px 12px;
		border-radius: 8px;
		font-size: 14px;

		width: max-content;
		max-width: 300px;

		white-space: normal;
		word-break: break-word;
		overflow-wrap: break-word;

		box-sizing: border-box;
		z-index: 9999;
		text-align: center;
	}

	/* Mostra tooltip ao hover */
	:global(.tooltip-container:hover .tooltip-text) {
		visibility: visible;
		opacity: 1;
	}
</style>
