<script>
	import { tema } from '$lib/stores/tema.svelte';
	import { Icon, Moon, Sun } from 'svelte-hero-icons';
</script>

<footer class="border-t border-gray-dark bg-gray-light dark:border-gray-light dark:bg-gray-dark">
	<div class="container px-4 py-12 sm:px-6 md:flex md:items-center md:justify-between lg:px-8">
		<div class="flex items-center justify-center space-x-6 md:order-2">
			<a href="https://www.themoviedb.org/" rel="external" target="_blank">
				<img src="/imagens/themoviedb.svg" alt="themoviedb" width="200" /></a
			>
			<button
				onclick={() => {
					if (tema.value === 'dark') {
						tema.value = 'light';
					} else {
						tema.value = 'dark';
					}
					window.localStorage.setItem('tema', tema.value);
				}}
				class="cursor-pointer text-gray-dark dark:text-gray-light"
				><Icon src={tema.value === 'dark' ? Sun : Moon} class="w-6" /></button
			>
		</div>
		<div class="mt-8 flex text-gray-dark md:order-1 md:mt-0 dark:text-gray-light">
			<p class="text-gray text-center text-sm">&copy; 2022 Movie HUB. All rights reserved.</p>
		</div>
	</div>
</footer>
