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
  
  listar(filtro: string = ''): Observable<Livro[]>{
    let url = `${this.base}api/livros`
    if (filtro){
      url+= `/?titulo=${encodeURIComponent(filtro)}`
    }
    return this.http.get<Livro[]>(url)
  }

  obterPorId(id: string) {
  const url = `${this.base}api/livros/${id}`;
  return this.http.get<Livro>(url);
  }
}
