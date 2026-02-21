<script lang="ts">
	import IconePalavraPorPalavra from '$lib/icones/iconePalavraPorPalavra.svelte';
	import { mount, unmount } from 'svelte';
	import Swal from 'sweetalert2';
	import Modal from './Modal.svelte';

	let {
		original,
		traducaopp,
		traducao,
		voz
	}: {
		original: string[];
		traducaopp: string[];
		traducao: string[];
		voz: string;
	} = $props();

	function abrirSweetAlert() {
		const container = document.createElement('div');

		// 2. Monta o componente passando as props necessárias
		const app = mount(Modal, {
			target: container,
			props: { traducaopp, original, traducao, voz }
		});

		Swal.fire({
			title: 'TRADUÇÃO PALAVRA POR PALAVRA',
			html: container,
			customClass: {
				popup: 'meu-swal',
				title: 'meu-titulo-pequeno'
			},
			footer: '* Clique em cada palavra isoladamente para ver sua tradução.',
			confirmButtonColor: '#3085d6',
			didClose: () => {
				unmount(app);
			}
		});
	}
</script>

<button onclick={abrirSweetAlert} class="cursor-pointer rounded bg-gray-700 px-2 py-1">
	<IconePalavraPorPalavra />
</button>

<style>
	:global(.meu-swal) {
		overflow: visible !important;
	}
	:global(.meu-swal .swal2-html-container) {
		overflow: visible !important;
	}
	:global(.tooltip-container) {
		position: relative;
		cursor: pointer;
		color: #0d6efd;
		background-color: lightcyan;
		font-weight: bold;
		margin: 0px 5px;
		display: inline-block;
	}
	:global(.meu-titulo-pequeno) {
		font-size: 26px;
		font-weight: normal;
	}
</style>
