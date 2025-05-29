import { Component } from '@angular/core';
import { RouterModule, Router } from '@angular/router';

@Component({
  selector: 'app-header',
  imports: [RouterModule],
  templateUrl: './app-header.component.html',
  styleUrl: './app-header.component.scss'
})
export class AppHeaderComponent {
  constructor(private router: Router) { }

  title = 'Predictive Model for Tumor Type Classification';
  subtitle = 'Diagnose prediction';
}
