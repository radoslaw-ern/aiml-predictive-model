import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ApiService } from '../../services/api.service';
import { apiResponse } from '../../types/api';

@Component({
  selector: 'app-upload-spreadsheet',
  imports: [CommonModule, RouterModule],
  templateUrl: './upload-spreadsheet.component.html',
  styleUrl: './upload-spreadsheet.component.scss',
})
export class UploadSpreadsheetComponent {
  constructor(private apiService: ApiService) { }

  uploadStatus: number = 0;
  diagnosePrediction: number = 0;

  onFileSelected(event: Event): void {
    const file: File = (event.target as HTMLInputElement).files![0];
    this.uploadStatus = 1;
    
    this.apiService.postFile(file).subscribe((response: unknown) => {
      if ((response as apiResponse).prediction) {
        this.diagnosePrediction = Math.floor((response as apiResponse).prediction as number * 100000) / 1000
        console.log({
          r: (response as apiResponse).prediction,
          d: this.diagnosePrediction,
        });

        this.uploadStatus = 2;
      }
    });
  }

  onRefresh = () => {
    window.location.reload()
  }
}
