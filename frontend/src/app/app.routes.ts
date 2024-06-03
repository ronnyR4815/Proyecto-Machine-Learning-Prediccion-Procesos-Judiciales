import { Routes } from '@angular/router';
import { CargaDocumentosComponent } from './carga-documentos/carga-documentos.component';
import { BolsaPalabrasComponent } from './bolsa-palabras/bolsa-palabras.component';
import { ValidacionesComponent } from './validaciones/validaciones.component';

export const routes: Routes = [
    { path: 'documentos', component: CargaDocumentosComponent },
    { path: 'tabla', component: BolsaPalabrasComponent },
    { path: 'validaciones', component: ValidacionesComponent },
];
