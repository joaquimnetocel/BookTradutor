<script lang="ts">
	import { goto } from "$app/navigation";
	import { page } from "$app/state";
	import { parseAppSegmentConfig } from "next/dist/build/segment-config/app/app-segment-config";
	import { onMount } from "svelte";

  type Balao = {
    x1: number;
    y1: number;
    x2: number;
    y2: number;
    ptbr: string;
    en: string;
  };


  let balaoJson = $state<Balao[]>([]);
  let imgElement = $state<HTMLImageElement>();
  let larguraOriginal = $state(0);
  let alturaOriginal = $state(0);
  let estadoIdioma = $state<'ptbr' | 'en'>('ptbr');

  const funcaoLeitura = async () => {
    const res = await fetch(`/${page.params.edicao}/${page.params.pagina}.json`);
    balaoJson = await res.json();

  }

  $effect(() => {
    funcaoLeitura();
  });

  const mudarIdioma = (valor: string) => {
    estadoIdioma = valor as 'ptbr' | 'en';
  }



  let audio: HTMLAudioElement;

  onMount(async () => {
    // Carrega JSON (só no navegador)
    const res = await fetch(`/${page.params.edicao}/${page.params.pagina}.json`);
    balaoJson = await res.json();

    // Inicializa Audio só no navegador
    audio = new Audio('/audio/musica_teste.mp3');
  });

  function toggleAudio() {
    if (!audio) return;
    if (audio.paused) {
      audio.currentTime = 0;
      audio.play().catch(err => console.error('Erro ao tocar:', err));
    } else {
      audio.pause();
      audio.currentTime = 0;
    }
  }
</script>


<button onclick={() => goto(`/revista/${page.params.edicao}/${parseInt(page.params.pagina??'1') + 1}`)}>AVANÇAR</button>
<button onclick={() => goto(`/revista/${page.params.edicao}/${parseInt(page.params.pagina??'1') -1}`)}>VOLTAR</button>

<div class="w-full max-w-150 mx-auto mb-4 ">
  <select
    bind:value={estadoIdioma}
    class="block mx-auto p-2 border rounded w-full max-w-50"
  >
    <option value="ptbr">Português</option>
    <option value="en">English</option>
  </select>
</div>

<!-- Container do quadrinho centralizado -->
<div class="relative w-full mx-auto">
  <img
  bind:this={imgElement}
  src={`/${page.params.edicao}/${page.params.pagina}.jpg`}
  alt="Quadrinho"
  class="block w-full mb-4"
  onload={() => {
    if (imgElement) {
      larguraOriginal = imgElement.naturalWidth;
      alturaOriginal = imgElement.naturalHeight;
      console.log('Largura original:', larguraOriginal, 'Altura original:', alturaOriginal);
    }
  }}
/>

<!-- onclick={() => alert(balao[estadoIdioma])} -->
 <button class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600" onclick={toggleAudio}>
  Tocar / Parar áudio
</button>

  {#each balaoJson as balao}
    <button
      type="button"
      class="absolute cursor-pointer p-0 lg:hover:bg-red-500/20 bg-blue-500/30 lg:bg-transparent"
      aria-label="Clique para ver o diálogo: {balao[estadoIdioma]}"
      style="
        left: {(balao.x1 / larguraOriginal) * 100}%;
        top: {(balao.y1 / alturaOriginal) * 100}%;
        width: {((balao.x2 - balao.x1) / larguraOriginal) * 100}%;
        height: {((balao.y2 - balao.y1) / alturaOriginal) * 100}%;
      "
    ></button>
  {/each}
</div>

{page.params.edicao}

<!-- <script lang="ts">
  type Balao = {
    x1: number;
    y1: number;
    x2: number;
    y2: number;
    ptbr: string;
    en:string;
  };

  let balaoJson  = $state<Balao[]>([]);
  let imgElement = $state<HTMLImageElement>();
  let larguraOriginal = $state(0);
  let alturaOriginal = $state(0);
  let estadoIdioma = $state<'ptbr' | 'en'>('ptbr')

const funcaoLeitura = async () => {
    const res = await fetch('/Liga_da_Justiça_Odisseia_01/DC_16_(28).json');
    balaoJson = await res.json();
  }

  $effect(()=>{
    funcaoLeitura()
  });

  const mudarIdioma = (valor: string) => {
    estadoIdioma = valor as 'ptbr' | 'en';
  }
</script>

<select bind:value={estadoIdioma}>
    <option value="ptbr">Português</option>
    <option value="en">English</option>
</select>

<div class="quadrinho relative w-full max-w-150">
  <img
  class='block w-full'
bind:this={imgElement}
  src="/Liga_da_Justiça_Odisseia_01/DC_16_(28).jpg"
    alt="Quadrinho"
    onload={()=>{
      if (imgElement) {
      larguraOriginal = imgElement.naturalWidth;
      alturaOriginal = imgElement.naturalHeight;
      console.log('Largura original:', larguraOriginal, 'Altura original:', alturaOriginal);
    }
    }} 
  />

  {#each balaoJson as balao}
    <button
      type="button"
      class="absolute cursor-pointer p-0 hover:bg-red-500/20"
      aria-label="Clique para ver o diálogo: {balao[estadoIdioma]}"
      onclick={() => alert(balao[estadoIdioma])}
      style="
        left: {(balao.x1 / larguraOriginal) * 100}%;
        top: {(balao.y1 / alturaOriginal) * 100}%;
        width: {((balao.x2 - balao.x1) / larguraOriginal) * 100}%;
        height: {((balao.y2 - balao.y1) / alturaOriginal) * 100}%;
      "
    ></button>
  {/each}
</div> -->
