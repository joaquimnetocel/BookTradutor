import { query } from '$app/server';
import { type typeDados, schemaDados } from '$lib/types/typeDados';
import { error } from '@sveltejs/kit';
import fs from 'fs';
import path from 'path';
import * as v from 'valibot';

const arrayTypeDadosSchema = v.array(schemaDados);

export const funcaoCarregarDadosDasRevistas = query(async (): Promise<typeDados[]> => {
	const basePath = path.resolve('static');
	const pastas = fs.readdirSync(basePath);

	const resultado: unknown[] = [];

	for (const pasta of pastas) {
		const arquivo = path.join(basePath, pasta, '0 - dados.json');

		if (fs.existsSync(arquivo)) {
			const conteudo = fs.readFileSync(arquivo, 'utf-8');
			const json = JSON.parse(conteudo);
			resultado.push(json);
		}
	}

	const dadosValidados = v.safeParse(arrayTypeDadosSchema, resultado);
	if (dadosValidados.success === false) {
		error(404, 'ALGUM DADO DA REVISTA NÃO ESTÁ RESPEITANDO A TIPAGEM CORRETA!');
	}

	return dadosValidados.output;
});
