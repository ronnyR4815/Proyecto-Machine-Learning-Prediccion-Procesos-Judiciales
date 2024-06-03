import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

export interface Documento {
  _id: string;
  nombre: string;
  resultado: string;
}

@Component({
  selector: 'app-validaciones',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './validaciones.component.html',
  styleUrl: './validaciones.component.css'
})
export class ValidacionesComponent implements OnInit{
  listaDocumentos: Documento[] = [];
  loading = false;

  ngOnInit(): void {
    this.fetchDocumentos();
  }
  fetchDocumentos(): void {
      fetch('http://127.0.0.1:5000/get_documentos')
        .then(response => response.json())
        .then(data => {
          this.listaDocumentos = data as Documento[]
          console.log(this.listaDocumentos)
        })
        .catch(error => console.error('Error:', error));
    }
}