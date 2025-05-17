import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () => import('./views/welcome-screen/welcome-screen.component').then((component) => component.WelcomeScreenComponent),
  },
  {
    path: 'upload-spreadsheet',
    loadComponent: () => import('./views/upload-spreadsheet/upload-spreadsheet.component').then((component) => component.UploadSpreadsheetComponent),
  },
];
