import { getRequestEvent, query } from '$app/server';
import { redirect } from '@sveltejs/kit';
import fs from 'fs';
import path from 'path';
import * as v from 'valibot';

const schema = v.object({
	edicao: v.string(),
	pagina: v.string(),
	saga: v.optional(v.string())
});

export const funcaoLerTotalDePaginas = query(schema, async ({ edicao, pagina, saga }) => {
	let pasta = '';
	if (saga === undefined) {
		pasta = path.join(process.cwd(), 'static', edicao ?? '1');
	} else {
		pasta = path.join(process.cwd(), 'static', saga, edicao ?? '1');
	}

	if (!fs.existsSync(pasta)) return 1;

	const arquivos = fs.readdirSync(pasta);
	const paginas = arquivos.filter((f) => /^\d+\.(jpg|jpeg|png|webp)$/.test(f));
	const totalDePaginas = paginas.length;

	if (parseInt(pagina ?? '1') < 1) {
		if (saga) {
			throw redirect(302, `/leitura/${saga}/${edicao ?? '1'}/1`);
		} else {
			throw redirect(302, `/leitura/${edicao ?? '1'}/1`);
		}
	}
	if (parseInt(pagina ?? '1') > paginas.length) {
		if (saga) {
			throw redirect(302, `/leitura/${saga}/${edicao ?? '1'}/${totalDePaginas}`);
		} else {
			throw redirect(302, `/leitura/${edicao ?? '1'}/${totalDePaginas}`);
		}
	}

	return paginas.length;
});
