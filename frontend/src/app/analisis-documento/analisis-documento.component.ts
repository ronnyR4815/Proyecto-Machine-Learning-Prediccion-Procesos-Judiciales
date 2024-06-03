import { Component } from '@angular/core';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatSelectModule } from '@angular/material/select';
import { MatIconModule } from '@angular/material/icon';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatCardModule } from '@angular/material/card'; // Importar MatCardModule
import { CommonModule } from '@angular/common'; // Importar CommonModule

@Component({
  selector: 'app-analisis-documento',
  standalone: true,
  imports: [
    CommonModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatSelectModule,
    MatIconModule,
    MatProgressBarModule,
    MatCardModule // Añadir MatCardModule a imports
  ],
  templateUrl: './analisis-documento.component.html',
  styleUrl: './analisis-documento.component.css'
})
export class AnalisisDocumentoComponent {
  selectedFile: File | null = null;
  loading = false;
  message: string | null = null; // Nueva propiedad para almacenar el mensaje

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
    this.message = null; // Limpiar el mensaje anterior
    const formData = new FormData();
    formData.append('file', this.selectedFile);

    fetch('http://127.0.0.1:5000/analizar_documento', {
      method: 'POST',
      body: formData
    })
      .then(response => response.json())
      .then(data => {
        console.log('Respuesta del servidor:', data);
        this.message = data.message; // Asignar el mensaje del backend
        this.loading = false;
      })
      .catch(error => {
        console.error('Error:', error);
        this.message = 'Error al procesar el documento.'; // Mensaje de error
        this.loading = false;
      });
  }
}
