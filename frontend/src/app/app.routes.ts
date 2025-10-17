import { Routes } from '@angular/router';
import { HomeComponet } from './pages/home/home-component';
import { AutoresPage } from './pages/authors/authors-component';
import { EditorasPage } from './pages/editoras/editoras-component';
import { LivrosPage } from './pages/livros/livros-component';
import { LoginComponent } from './pages/login/login-component';
import { LivroDetalhePage } from './pages/livro/livro-component';
import { authGuard } from './services/guard';

export const routes: Routes = [
  {
    path: '',
    component: HomeComponet,
    canActivate: [authGuard]
  },
  {
    path: 'home',
    component: HomeComponet,
    canActivate: [authGuard]
  },
  {
    path: 'autores',
    component: AutoresPage,
    canActivate: [authGuard]
  },
  {
    path: 'editoras',
    component: EditorasPage,
    canActivate: [authGuard]
  },
  {
    path: 'livros',
    component: LivrosPage,
    canActivate: [authGuard]
  },
  {
    path: 'livros/:id',
    component: LivroDetalhePage,
    canActivate: [authGuard]
  },
  {
    path: 'login',
    component: LoginComponent
  }
];
