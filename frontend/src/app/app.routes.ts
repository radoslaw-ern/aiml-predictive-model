import { Routes } from '@angular/router';

export const routes: Routes = [
  { path: '', redirectTo: '/upload-spreadsheet', pathMatch: 'full' },
  {
    path: 'upload-spreadsheet',
    loadComponent: () => import('./views/upload-spreadsheet/upload-spreadsheet.component').then((component) => component.UploadSpreadsheetComponent),
  },
];
