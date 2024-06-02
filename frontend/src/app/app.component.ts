import { Component } from '@angular/core';
import { CargaDocumentosComponent } from './carga-documentos/carga-documentos.component';
import { AnalisisDocumentoComponent } from './analisis-documento/analisis-documento.component';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CargaDocumentosComponent, AnalisisDocumentoComponent, RouterLink, RouterLinkActive, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend';
}
