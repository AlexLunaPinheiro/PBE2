import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Livro } from '../models/livro';
import { enviroment } from '../../enviroments/enviroments';

@Injectable({
  providedIn: 'root'
})
export class LivrosServices {
  private http = inject(HttpClient)
  private base = enviroment.apiBase
  
  listar(): Observable<Livro[]>{
    const url = `${this.base}api/livros`
    return this.http.get<Livro[]>(url)
  }
}
