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

  title = '';

  ngOnInit(): void {
    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd) {
        const url = event.url;
        switch (url) {
          case '/home':
            this.title = 'Home';
            break;
          case '/about':
            this.title = 'About';
            break;
          case '/contact':
            this.title = 'Contact';
            break;
          default:
            this.title = 'Default Title';
            break;
        }
      }
    });
  }
}
