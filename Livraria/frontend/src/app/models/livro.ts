export interface Livro {
    id: number;
    titulo: string;
    subtitulo: string;
    editora: number; // Aqui é o id da editora, pois é um ForeignKey
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
    autor: number; // id do autor, por causa do ForeignKey
}
