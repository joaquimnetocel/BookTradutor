<script lang="ts">
	// import { getContext } from 'svelte';
	import { resolve } from '$app/paths';
	import { pesquisaVisivel } from '$lib/stores/pesquisaVisivel.svelte';
	import { Icon, MagnifyingGlass } from 'svelte-hero-icons';
	// import Logo from '$assets/img/Logo.svg?src';
	import SearchModal from '../../lib/componentes/SearchModal.svelte';
</script>

<SearchModal
	show={pesquisaVisivel.value}
	onhide={() => {
		pesquisaVisivel.value = false;
	}}
/>
<div class="container">
	<div class="flex items-center justify-between">
		<div class="flex items-center">
			<div class="w-10 py-2 md:py-4">
				<a href={resolve('/')} class="group hover:text-primary-light text-red-600 transition-all">
					<!-- <img src="/imagens/Logo.svg" alt="logo" /> -->
					<svg xmlns="http://www.w3.org/2000/svg" data-name="Layer 1" viewBox="0 0 100 100">
						<path
							fill="currentColor"
							d="M50 36a14 14 0 1 0 12.9 8.55A14 14 0 0 0 50 36Zm0 20a6 6 0 1 1 6-6 6 6 0 0 1-6 6Z"
						/>
						<path
							fill="currentColor"
							d="M81.39 43.75a3.87 3.87 0 0 0-5.26-2.81l-.23.06a3.89 3.89 0 0 0-2.34 4.38A24 24 0 1 1 50 26a23.81 23.81 0 0 1 4.73.48A3.83 3.83 0 0 0 59 24.09l.09-.21a3.87 3.87 0 0 0-2.84-5.27A32 32 0 0 0 18 48.82a32 32 0 1 0 63.36-5.07Z"
						/>
						<circle fill="currentColor" cx="72" cy="28" r="4" />
					</svg>
					<!-- {@html Logo} -->
				</a>
			</div>
			<div class="font-secondary text-gray font-bold text-red-600 select-none">HUB</div>
		</div>

		<div>
			<button
				class="text-gray hover:bg-light dark:hover:bg-opacity-10 inline-flex items-center rounded-full border border-transparent p-2 transition-all focus:ring-2 focus:outline-none {pesquisaVisivel.value &&
					'ring-2 dark:text-white'}  ring-primary-light"
				onclick={() => (pesquisaVisivel.value = true)}
				><Icon src={MagnifyingGlass} class="w-5 text-gray-dark dark:text-gray-light" /></button
			>
		</div>
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
