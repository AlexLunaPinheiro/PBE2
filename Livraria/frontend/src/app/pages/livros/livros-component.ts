import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { LivrosServices } from '../../services/livros-services';
import { Livro } from '../../models/livro';
import { AuthService } from '../../services/auth-services';

@Component({
  standalone: true,
  imports: [RouterLink],
  template: `
    <section style="max-width:900px;margin:2rem auto;padding:0 1rem">
      <h1>Livros</h1>

      @if (carregando()) {
        <p>Carregando…</p>
      } @else if (erro()) {
        <p style="color:#c62828">{{ erro() }}</p>
      } @else {
        <ul style="padding-left:1.25rem">
          @for (livro of livros(); track livro.id) {
            <li style="margin:.25rem 0">
              <strong>{{ livro.titulo }}</strong>
              @if (livro.subtitulo) { — <em style="color:#666">{{ livro.subtitulo }}</em> }
              @if (livro.editora) { • {{ livro.editora }} }
              @if (livro.isbn) { <div style="color:#555">ISBN: {{ livro.isbn }}</div> }
              @if (livro.cnpj) { <div style="color:#555">CNPJ: {{ livro.cnpj }}</div> }
              @if (livro.endereco) { <div style="color:#555">{{ livro.endereco }}</div> }
              @if (livro.telefone) { <div style="color:#555">Telefone: {{ livro.telefone }}</div> }
              @if (livro.email) { <div style="color:#555">Email: {{ livro.email }}</div> }
              @if (livro.site) { <div style="color:#555"><a href="{{ livro.site }}" target="_blank">{{ livro.site }}</a></div> }
            </li>
          }
        </ul>
      }

      <nav style="margin-top:1rem">
        <a routerLink="/">Voltar ao início</a>
      </nav>
    </section>
  `
})
export class LivrosPage {
  private svc = inject(LivrosServices);
  private auth = inject(AuthService);   //Ver o token
  livros = signal<Livro[]>([]);
  carregando = signal(true);
  erro = signal<string | null>(null);

  constructor() {
    console.log("Token de acesso: ", this.auth.token());
    
    this.svc.listar().subscribe({
      next: (data) => { this.livros.set(data); this.carregando.set(false); },
      error: () => { this.erro.set('Falha ao carregar livros'); this.carregando.set(false); }
    });
  }
}