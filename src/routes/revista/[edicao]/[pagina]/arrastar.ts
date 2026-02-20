import { goto } from '$app/navigation';
import { resolve } from '$app/paths';
import { page } from '$app/state';

let startX = 0;
let endX = 0;

export function handleTouchStart(e: TouchEvent) {
	startX = e.touches[0].clientX;
}

export function handleTouchEnd(e: TouchEvent) {
	endX = e.changedTouches[0].clientX;

	const distance = endX - startX;

	if (distance > 50) {
		goto(
			resolve(
				`/revista/${page.params.edicao}/${parseInt(page.params.pagina ?? '1') - 1}?direction=previous`
			)
		);
	}

	if (distance < -50) {
		goto(
			resolve(
				`/revista/${page.params.edicao}/${parseInt(page.params.pagina ?? '1') + 1}?direction=next`
			)
		);
	}
}
