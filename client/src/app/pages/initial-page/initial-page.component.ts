import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-initial-page',
  templateUrl: './initial-page.component.html',
  styleUrls: ['./initial-page.component.scss']
})
export class InitialPageComponent implements OnInit {

  data: Date = new Date();
  focus;
  focus1;

  products = [];

  // change this function* to a appropriate to this action
  const mapKeys = {
      13: 'function_to_next_item',
      113: 'function_to_cancel',
      173: 'function_finish',
      191: 'funtion_to_back',
    }

  product = {
    id: '',
    quantity: 0
    // id: integer
    // name: string,
    // category: string,
    // price: float
    // active: boolean
  }

  order = {
    // customer : id do cliente
    // item: id do produto
  }

  constructor(private http: HttpClient) { }

  ngOnInit() {
    var body = document.getElementsByTagName('body')[0];
    body.classList.add('login-page');

    var navbar = document.getElementsByTagName('nav')[0];
    // navbar.classList.add('navbar-transparent');
  }
  ngOnDestroy() {
    var body = document.getElementsByTagName('body')[0];
    body.classList.remove('login-page');

    var navbar = document.getElementsByTagName('nav')[0];
    navbar.classList.remove('navbar-transparent');
  }

  /*
    ENDPOINTS

    product - precisa de autenticação (GET lista tudo, POST cria produto)
    product/list - não precisa de autenticação  (não aceita POST)
    product/:id - (GET retorna objeto, POST atualiza)
e
   */

  addProduct() {
    console.log('this.product', this.product);
    // this.http.get(`product/`)
    this.products.push({
      id: this.product.id,
      quantity: this.product.quantity
    })
    this.product = { id: '', quantity: 0 };
  }

  document.onkeydown = function(event) {
    event.preventDefault();
    if (event.keyCode in mapKeys) {
      mapKeys[event.keyCode]
      console.log(mapKeys[event.keyCode]) // hehehe
    }
  }
}
