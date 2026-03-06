<script lang="ts">
	import { resolve } from '$app/paths';
	import type { typeDados } from '$lib/types/typeDados';
	import Rating from './Rating.svelte';

	// const getYear = (date: string | number | Date) => {
	// 	const d = new Date(date);
	// 	return d.getFullYear();
	// };

	let { revista }: { revista: typeDados } = $props();
</script>

<a href={resolve('/')} data-sveltekit-prefetch class="bg-light">
	<div class="group relative overflow-hidden rounded-lg sm:rounded-xl">
		<div class="text-light absolute z-20 flex h-full w-full flex-col items-end justify-between">
			<div class="p-0">
				{#if revista.rating}
					<Rating valor={revista.rating} />
				{/if}
			</div>

			<div class="flex w-full flex-col space-y-1 bg-slate-600 px-6 py-1 text-center opacity-80">
				<div class="font-secondary font-bold text-[rgb(241,245,249)] transition-all sm:text-lg">
					{revista.titulo}
					{#if revista.ano}
						({revista.ano})
					{/if}
				</div>
			</div>
		</div>
		<div
			class="from-dark absolute z-10 h-full w-full bg-linear-to-t to-transparent hover:opacity-0"
		></div>
		<div
			class="to-primary-light absolute z-10 h-full w-full bg-linear-to-tr from-primary opacity-0 transition-all duration-500 ease-out group-hover:opacity-50"
		></div>
		<img
			class="h-64 w-full object-fill transition-all duration-200 group-hover:scale-105 sm:h-60"
			src={revista.capa ? revista.capa : '/img/mesh.png'}
			alt="poster"
			onerror={(ev) => {
				const img = ev.currentTarget as HTMLImageElement;
				img.src = '/img/mesh.png';
			}}
		/>
	</div>
</a>

<style>
	.font-secondary {
		font-family:
			Roboto Condensed,
			ui-sans-serif,
			system-ui,
			-apple-system,
			BlinkMacSystemFont,
			'Segoe UI',
			Roboto,
			'Helvetica Neue',
			Arial,
			'Noto Sans',
			sans-serif,
			'Apple Color Emoji',
			'Segoe UI Emoji',
			'Segoe UI Symbol',
			'Noto Color Emoji';
	}
</style>
