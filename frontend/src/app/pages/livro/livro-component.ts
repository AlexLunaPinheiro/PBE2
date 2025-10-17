import { Component, inject, signal } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { LivrosServices } from '../../services/livros-services';
import { Livro } from '../../models/livro';
import { CommonModule } from '@angular/common';

@Component({
    standalone: true,
    imports: [CommonModule, RouterLink],
    templateUrl: './livro-component.html',
    styleUrls: ['./livro-component.css']
})
export class LivroDetalhePage {
  private route = inject(ActivatedRoute);
  private svc = inject(LivrosServices);

  livro = signal<any>({
  autor: {},
  editora: {}
    });
  carregando = signal(true);
  erro = signal<string | null>(null);

  constructor() {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.svc.obterPorId(id).subscribe({
        next: (data) => {
          this.livro.set(data);
          this.carregando.set(false);
        },
        error: () => {
          this.erro.set('Livro não encontrado');
          this.carregando.set(false);
        }
      });
    } else {
      this.erro.set('ID do livro não informado');
      this.carregando.set(false);
    }
  }
}