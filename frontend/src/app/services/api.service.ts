import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  constructor(private http: HttpClient) { }

  private apiUrl = process.env['APP_API_ENDPOINT'];

  postFile(file: File): Observable<unknown> {
    const formData = new FormData();
    formData.append('file', file);

    const headers = new HttpHeaders();
    headers.set('Content-Type', 'multipart/form-data');

    return this.http.post(`${this.apiUrl}/upload-spreadsheet`, formData, { headers });
  }
}
