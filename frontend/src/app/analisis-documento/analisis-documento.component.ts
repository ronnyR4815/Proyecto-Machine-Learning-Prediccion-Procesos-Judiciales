import { Component } from '@angular/core';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatSelectModule } from '@angular/material/select';
import { MatIconModule } from '@angular/material/icon';
import {MatProgressBarModule} from '@angular/material/progress-bar';

@Component({
  selector: 'app-analisis-documento',
  standalone: true,
  imports: [MatFormFieldModule, MatInputModule, MatButtonModule, MatSelectModule, MatIconModule, MatProgressBarModule],
  templateUrl: './analisis-documento.component.html',
  styleUrl: './analisis-documento.component.css'
})
export class AnalisisDocumentoComponent {
  selectedFile: File | null = null;
  loading = false;
  // data = null;

  onFileSelected(event: any) {
    const file: File = event.target.files[0];
    if (file && file.type === 'application/pdf') {
      this.selectedFile = file;
    } else {
      console.error('Por favor, selecciona un archivo PDF.');
    }
  }

  onUpload() {
    if (!this.selectedFile) {
      console.error('No se ha seleccionado ningún archivo.');
      return;
    }
    this.loading = true;
    const formData = new FormData();
    formData.append('filePdf', this.selectedFile);

    fetch('https://fead-45-235-142-196.ngrok-free.app/analizar_documento', {
      method: 'POST',
      body: formData
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Error en la solicitud.');
        }
        return response.json();
      })
      .then(data => {
        console.log('Respuesta del servidor:', data);
        // this.data = data
        this.loading = false;
      })
      .catch(error => {
        console.error('Error:', error);
        this.loading = false;
      });
  }
}
