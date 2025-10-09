import { Component , inject} from '@angular/core';
import { RouterLink } from "@angular/router";
import { LivrosStoreService } from '../../services/livro-store-service';

@Component({
    selector:'app-home',
    standalone: true,
    imports: [RouterLink],
    templateUrl: './home-component.html',
    styleUrls: ['./home-component.css']
  
})
export class HomeComponet {
  private store = inject(LivrosStoreService);
  livros = this.store.livros;
  carregando = this.store.carregando;
  erro = this.store.erro;
}
