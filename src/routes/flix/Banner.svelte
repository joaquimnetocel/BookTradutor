<script lang="ts">
	import { fade } from 'svelte/transition';
	import { Autoplay, EffectFade } from 'swiper';
	import { Swiper, SwiperSlide } from 'swiper/svelte';
	import MovieHero from './MovieHero.svelte';

	import type { typeDados } from '$lib/types/typeDados';
	import 'swiper/css';
	import 'swiper/css/effect-fade';
	import 'swiper/css/pagination';

	let { colecao }: { colecao: typeDados[] } = $props();
</script>

<div class="container">
	<Swiper
		modules={[EffectFade, Autoplay]}
		effect="fade"
		autoplay={{
			delay: 5000,
			disableOnInteraction: false
		}}
		speed={750}
		slidesPerView={1}
	>
		{#each colecao as revista, i (i)}
			<SwiperSlide>
				<div in:fade={{ duration: 1000 }}><MovieHero {revista} /></div>
			</SwiperSlide>
		{/each}
	</Swiper>
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
