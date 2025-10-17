import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { LivrosServices } from '../../services/livros-services';
import { Livro } from '../../models/livro';
import { AuthService } from '../../services/auth-services';
import { LivrosStoreService } from '../../services/livro-store-service';

const Texto = "";

@Component({
  standalone: true,
  imports: [RouterLink],
  templateUrl: './livros-component.html',
  styleUrls: ['./livros-component.css']
})
export class LivrosPage {
  private store = inject(LivrosStoreService);
  livros = this.store.livros;
  carregando = this.store.carregando;
  erro = this.store.erro;
}