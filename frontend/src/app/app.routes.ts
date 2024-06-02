import { Routes } from '@angular/router';
import { CargaDocumentosComponent } from './carga-documentos/carga-documentos.component';
import { BolsaPalabrasComponent } from './bolsa-palabras/bolsa-palabras.component';

export const routes: Routes = [
    { path: 'documentos', component: CargaDocumentosComponent },
    { path: 'tabla', component: BolsaPalabrasComponent },
];
