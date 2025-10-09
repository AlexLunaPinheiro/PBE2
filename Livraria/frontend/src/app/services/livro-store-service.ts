import { Injectable, signal } from '@angular/core';
import { LivrosServices } from './livros-services';
import { Livro } from '../models/livro';

@Injectable({ providedIn: 'root' })
export class LivrosStoreService {
  livros = signal<Livro[]>([]);
  carregando = signal(true);
  erro = signal<string | null>(null);

  constructor(private svc: LivrosServices) {
    this.loadLivros();
  }

  loadLivros() {
    this.carregando.set(true);
    this.svc.listar().subscribe({
      next: (data) => {
        this.livros.set(data);
        this.carregando.set(false);
      },
      error: () => {
        this.erro.set('Falha ao carregar livros');
        this.carregando.set(false);
      },
    });
  }
}