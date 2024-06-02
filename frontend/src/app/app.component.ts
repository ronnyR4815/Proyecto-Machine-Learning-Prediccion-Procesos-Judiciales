import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CargaDocumentosComponent } from './carga-documentos/carga-documentos.component';
import { AnalisisDocumentoComponent } from './analisis-documento/analisis-documento.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CargaDocumentosComponent, AnalisisDocumentoComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend';
}
