import { BrowserAnimationsModule } from '@angular/platform-browser/animations'; // this is needed!
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { RouterModule } from '@angular/router';
import { AppRoutingModule } from './app.routing';
import { ComponentsModule } from './components/components.module';
import { ExamplesModule } from './examples/examples.module';

import { AppComponent } from './app.component';
import { NavbarComponent } from './shared/navbar/navbar.component';
import { InitialPageComponent } from './pages/initial-page/initial-page.component';
import { AdminComponent } from './pages/admin/admin.component';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { NgbdModalBasic } from './components/modal/modal.component';
import { ApiService } from './components/core/api.service';

@NgModule({
    declarations: [
        AppComponent,
        NavbarComponent,
        InitialPageComponent,
        AdminComponent
    ],
    imports: [
        BrowserAnimationsModule,
        NgbModule.forRoot(),
        FormsModule,
        ComponentsModule,
        BrowserModule,
        HttpClientModule,
        RouterModule,
        AppRoutingModule,
        ExamplesModule
    ],
    providers: [ApiService],
    bootstrap: [AppComponent]
})
export class AppModule { }
