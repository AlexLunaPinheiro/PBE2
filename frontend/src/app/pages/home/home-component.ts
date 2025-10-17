import { Component, inject, signal } from '@angular/core';
import { Router } from '@angular/router';
import { LivrosStoreService } from '../../services/livro-store-service';
import { LivrosServices } from '../../services/livros-services';
import { Livro } from '../../models/livro';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [FormsModule, CommonModule, RouterLink],
  templateUrl: './home-component.html',
  styleUrls: ['./home-component.css'],
})
export class HomeComponet {
  private store = inject(LivrosStoreService);
  private svc = inject(LivrosServices);
  private router = inject(Router);

  livros = this.store.livros;
  carregando = this.store.carregando;
  erro = this.store.erro;
  filtro = '';
  sugestoes = signal<Livro[]>([]);

  buscarSugestoes() {
    const termo = this.filtro.trim();
    if (termo.length < 2) {
      this.sugestoes.set([]);
      return;
    }

    // Chama o backend com o filtro
    this.svc.listar(termo).subscribe({
      next: (data) => {
        // Limita a 3 resultados
        this.sugestoes.set(data.slice(0, 3));
      },
      error: () => this.sugestoes.set([]),
    });
  }

  irParaLivro(id: number) {
    this.sugestoes.set([]);
    this.filtro = '';
    this.router.navigate(['/livros', id]);
  }
}
