import { getRequestEvent, query } from '$app/server';
import type { Balao } from '$lib/types/typeBalao';
import * as v from 'valibot';

const schema = v.object({
	pagina: v.string(),
	edicao: v.string(),
	saga: v.optional(v.string())
});

export const funcaoLerBaloes = query(schema, async ({ pagina, edicao, saga }): Promise<Balao[]> => {
	const { fetch } = getRequestEvent();

	if (saga === undefined) {
		const resultado = await fetch(`/${edicao}/${pagina}.json`);
		if (resultado.ok === false) {
			return [];
		}
		return await resultado.json();
	}

	const resultado = await fetch(`/${saga}/${edicao}/${pagina}.json`);
	if (resultado.ok === false) {
		return [];
	}
	return await resultado.json();
});
