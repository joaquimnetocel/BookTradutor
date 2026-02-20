<script lang="ts">
	let modal = $state<HTMLDialogElement | undefined>(undefined);

	function openModal() {
		modal?.showModal();
	}

	function closeModal() {
		modal?.close();
	}
</script>

<button onclick={openModal}>open modal</button>

<dialog bind:this={modal} class="daisy-modal">
	<div class="daisy-modal-box">
		<h3 class="text-lg font-bold">Hello!</h3>
		<p class="py-4">Press ESC key or click outside to close</p>
	</div>
	<form method="dialog" class="daisy-modal-backdrop">
		<button onclick={closeModal}>close</button>
	</form>
</dialog>
