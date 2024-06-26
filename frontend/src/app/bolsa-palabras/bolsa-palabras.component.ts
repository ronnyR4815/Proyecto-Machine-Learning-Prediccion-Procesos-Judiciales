import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import {MatProgressBarModule} from '@angular/material/progress-bar';

@Component({
  selector: 'app-bolsa-palabras',
  standalone: true,
  imports: [CommonModule, MatProgressBarModule],
  templateUrl: './bolsa-palabras.component.html',
  styleUrl: './bolsa-palabras.component.css'
})
export class BolsaPalabrasComponent implements OnInit {
  loading = false;
  invertedIndex: Dictionary | null = null;

  fetchBolsaPalabras(): void {
  this.loading = true;
    fetch('http://127.0.0.1:5000/bolsa_palabras')
      .then(response => response.json())
      .then(data => {
        this.invertedIndex = data as Dictionary;
        this.loading = false;
      })
      .catch(error => {
        console.error('Error:', error);
        this.loading = false;
      });
  }
  ngOnInit(): void {
    this.fetchBolsaPalabras();
  }
}
export interface Dictionary {
  [key: string]: {
    [docId: number]: [number, number[]]; // Ocurrencias y posiciones
  }
}