import { Routes } from '@angular/router';
import { HomeComponet } from './pages/home/home-component';
import { AutoresPage } from './pages/authors/authors-component';
import { EditorasPage } from './pages/editoras/editoras-component';
import { LivrosPage } from './pages/livros/livros-component';
import { LoginComponent } from './pages/login/login-component'

export const routes: Routes = [
    {
        path: '',
        component: HomeComponet
    },
    {
        path: 'home',
        component: HomeComponet
    },
    {
        path:'autores',
        component: AutoresPage
    },
    {
        path:'editoras',
        component: EditorasPage
    },
    {
        path:'livros',
        component: LivrosPage
    },
    {
        path:'login',
        component: LoginComponent
    }
];
