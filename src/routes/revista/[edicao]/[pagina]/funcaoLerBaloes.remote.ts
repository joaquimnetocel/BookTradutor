import { getRequestEvent, query } from '$app/server';
import type { Balao } from '$lib/types/typeBalao';
import * as v from 'valibot';

const schema = v.object({
	pagina: v.string(),
	edicao: v.string()
});

export const funcaoLerBaloes = query(schema, async ({ pagina, edicao }): Promise<Balao[]> => {
	const { fetch } = getRequestEvent();
	const resultado = await fetch(`/${edicao}/${pagina}.json`);
	if (resultado.ok === false) {
		return [];
	}
	return await resultado.json();
});
