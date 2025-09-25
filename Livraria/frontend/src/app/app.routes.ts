import { Routes } from '@angular/router';
import { HomeComponet } from './pages/home/home-componet';
import { AutoresPage } from './pages/authors/authors-component';
import { EditorasPage } from './pages/editoras/editoras-component';

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
    }
];
