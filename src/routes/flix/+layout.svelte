<script lang="ts">
	// import { setContext } from 'svelte';
	// import { writable } from 'svelte/store';
	import { tema } from '$lib/stores/tema.svelte';
	import Navigation from './Navigation.svelte';
	import Rodape from './Rodape.svelte';
	// import '$lib/assets/css/app.css';
	// import '$lib/assets/css/typing.css';
	import type { Snippet } from 'svelte';

	// const activeSearch = writable(false);
	// setContext('activeSearch', activeSearch);

	let { children }: { children: Snippet } = $props();
</script>

<svelte:head>
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="" />
	<link
		href="https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@400;700&family=Roboto:wght@300;400;500&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<div class="{tema.value} flex h-screen flex-col">
	<div class="sticky top-0 z-50 bg-gray-light dark:bg-gray-dark">
		<Navigation />
	</div>
	<main class="grow bg-gray-light dark:bg-gray-dark">
		{@render children()}
	</main>
	<Rodape />
</div>
