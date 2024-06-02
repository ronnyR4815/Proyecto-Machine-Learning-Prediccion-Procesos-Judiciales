import { Component, OnInit } from '@angular/core';
import { ReactiveFormsModule, FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatSelectModule } from '@angular/material/select';
import { MatIconModule } from '@angular/material/icon';
import {MatProgressBarModule} from '@angular/material/progress-bar';
import { AnalisisDocumentoComponent } from '../analisis-documento/analisis-documento.component';

@Component({
  selector: 'app-carga-documentos',
  standalone: true,
  imports: [ReactiveFormsModule, MatFormFieldModule, MatInputModule, MatButtonModule, MatSelectModule, MatIconModule, MatProgressBarModule, AnalisisDocumentoComponent],
  templateUrl: './carga-documentos.component.html',
  styleUrl: './carga-documentos.component.css'
})
export class CargaDocumentosComponent {

  formCarga: FormGroup;
  selectedFile: File | null = null;
  loading = false;

  constructor(private fb: FormBuilder) {
    this.formCarga = this.fb.group({
      titulo: ['', Validators.required],
      resultado: ['', Validators.required]
    })
  }

  onFileSelected(event: any) {
    const file: File = event.target.files[0];
    if (file && file.type === 'application/pdf') {
      this.selectedFile = file;
      this.formCarga.get('titulo')?.setValue(file.name); // Establece el nombre del archivo como título
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
    formData.append('resultado', this.formCarga.get('resultado')?.value);
    formData.append('nombre', this.formCarga.get('titulo')?.value);

    fetch('https://fead-45-235-142-196.ngrok-free.app/test', {
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
        this.loading = false;
      })
      .catch(error => {
        console.error('Error:', error);
        this.loading = false;
      });
  }
}
