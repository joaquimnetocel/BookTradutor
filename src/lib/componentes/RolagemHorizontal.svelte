<script lang="ts">
	import type { typeDados } from '$lib/types/typeDados';
	import { tick } from 'svelte';
	import { fade } from 'svelte/transition';
	import 'swiper/css';
	import { Swiper, SwiperSlide } from 'swiper/svelte';
	import Revista from './Revista.svelte';

	let {
		colecao
	}: {
		colecao: typeDados[];
	} = $props();

	let innerWidth = $state<number>();
	let slidesPerView = $state<number>();

	const setSlidesPerView = async (w: number) => {
		await tick();
		if (w >= 1024) {
			slidesPerView = 6.5;
		} else if (w >= 768) {
			slidesPerView = 4.5;
		} else if (w >= 480) {
			slidesPerView = 3.5;
		} else {
			slidesPerView = 2.2;
		}
	};

	$effect(() => {
		if (innerWidth) {
			setSlidesPerView(innerWidth);
		}
	});
</script>

<svelte:window bind:innerWidth />

<div class="relative">
	<div
		class="absolute right-0 z-20 h-full w-20 bg-linear-to-l from-gray-light to-transparent dark:from-gray-dark"
	></div>

	<Swiper spaceBetween={10} {slidesPerView}>
		{#each colecao as revista, index (index)}
			<SwiperSlide>
				<div in:fade={{ duration: 300, delay: index * 100 }}>
					<Revista {revista} />
				</div>
			</SwiperSlide>
		{/each}
	</Swiper>
</div>
