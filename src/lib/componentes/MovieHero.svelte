<script lang="ts">
	import { resolve } from '$app/paths';
	import type { typeDados } from '$lib/types/typeDados';
	import Rating from './Rating.svelte';

	let { revista }: { revista: typeDados } = $props();

	// const getYear = (date: string | number | Date) => {
	// 	const d = new Date(date);
	// 	return d.getFullYear();
	// };
</script>

<a href={resolve('/')} class=" bg-light dark:bg-gray-dark dark:text-gray-light">
	<div class="group relative">
		<div class="text-light absolute z-20 flex h-full w-full flex-col justify-between">
			<div class="p-6">
				{#if revista.rating}
					<Rating valor={revista.rating} />
				{/if}
			</div>
			<div class="flex flex-col space-y-1 p-6">
				<div
					class="font-secondary text-6xl font-bold text-[rgb(241,245,249)] transition-all group-hover:text-6xl"
				>
					{revista.titulo}
				</div>
				<div class="text-md font-bold text-[rgb(241,245,249)]">{revista.ano}</div>
				<!-- <p class="line-clamp-3 max-w-xl leading-snug font-light">{revista.overview}</p> -->
			</div>
		</div>
		<div
			class="from-dark absolute z-10 h-full w-full bg-linear-to-tr to-transparent mix-blend-multiply transition-all group-hover:opacity-50"
		></div>

		<img
			class="bg-light h-80 w-full object-cover object-center transition-all duration-200 group-hover:scale-105 sm:h-128"
			src={revista.banner}
			alt="poster"
		/>
	</div>
</a>
