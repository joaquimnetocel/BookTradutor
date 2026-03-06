<script lang="ts">
	import Banner from '$lib/componentes/Banner.svelte';
	import Revista from '$lib/componentes/Revista.svelte';
	import RolagemHorizontal from '$lib/componentes/RolagemHorizontal.svelte';
	import type { typeDados } from '$lib/types/typeDados';
	import { fade } from 'svelte/transition';
	import { funcaoCarregarDadosDasRevistas } from './funcaoCarregarDadosDasRevistas.remote';

	let dados = $state<typeDados[]>([]);

	$effect(() => {
		(async () => {
			try {
				dados = await funcaoCarregarDadosDasRevistas();
				// eslint-disable-next-line @typescript-eslint/no-explicit-any
			} catch (e: any) {
				alert(e.body.message); // aqui você pega a mensagem do erro
			}

			dados = await funcaoCarregarDadosDasRevistas();
		})();
	});
</script>

<div class="mt-8 mb-6">
	<Banner colecao={dados.filter((current) => current.banner)} />
</div>

<div class="container space-y-6">
	<div>
		<h2 class="text-2xl font-bold text-gray-dark sm:text-3xl dark:text-gray-light">DESTAQUES</h2>
		<RolagemHorizontal colecao={dados} />
	</div>
</div>
<br />
<div class="container mt-2 mb-7">
	<h2 class="text-2xl font-bold text-gray-dark sm:text-3xl dark:text-gray-light">REVISTAS</h2>
	<div class="grid grid-cols-3 gap-2 sm:grid-cols-4 lg:grid-cols-7">
		{#each dados as revista, index (index)}
			<div in:fade={{ duration: 300, delay: index * 100 }}><Revista {revista} /></div>
		{/each}
	</div>
</div>

<style>
	.container {
		width: 100%;
		margin-right: auto;
		margin-left: auto;
		padding-right: 0.5rem /* 8px */;
		padding-left: 0.5rem /* 8px */;
	}
	@media (min-width: 1280px) {
		.container {
			max-width: 1280px;
		}
	}
</style>
