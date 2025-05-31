import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from './../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  constructor(private http: HttpClient) { }

  private apiUrl = environment.apiUrl

  postFile(file: File): Observable<unknown> {
    const formData = new FormData();
    formData.append('file', file);

    const headers = new HttpHeaders();
    headers.set('Content-Type', 'multipart/form-data');

    return this.http.post(`${this.apiUrl}/upload-spreadsheet`, formData, { headers });
  }
}
