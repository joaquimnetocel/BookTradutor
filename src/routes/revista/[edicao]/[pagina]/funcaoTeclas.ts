import { goto } from '$app/navigation';
import { resolve } from '$app/paths';
import { page } from '$app/state';

export function funcaoTeclas(e: KeyboardEvent) {
	switch (e.key) {
		//   case 38:
		//     window.scrollBy({ top: -30 });
		//     break;
		//   case 40:
		//     window.scrollBy({ top: 30 });
		//     break;
		case 'ArrowLeft':
			goto(
				resolve(
					`/revista/${page.params.edicao}/${parseInt(page.params.pagina ?? '1') - 1}?direction=previous`
				)
			);

			break;
		case 'ArrowRight':
			goto(
				resolve(
					`/revista/${page.params.edicao}/${parseInt(page.params.pagina ?? '1') + 1}?direction=next`
				)
			);
			break;
	}
}
