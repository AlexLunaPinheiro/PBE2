import { Autor } from "./autor";
import { Editora } from "./editora";

export interface Livro {
    id: number;
    titulo: string;
    subtitulo: string;
    editora: Editora; 
    isbn: string;
    descricao: string;
    idioma: string;
    ano: number;
    paginas: number;
    preco: number; // DecimalField -> number
    estoque: number;
    desconto: number; // DecimalField -> number
    disponivel: boolean;
    dimensoes: string;
    peso: number; // DecimalField -> number
    autor: Autor; // id do autor, por causa do ForeignKey
    capa: string;
}
