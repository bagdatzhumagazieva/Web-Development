import { Component, OnInit } from '@angular/core';
import { ProviderService } from './services/provider.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  public tasklists: ITaskList[] = [];


  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res=>{
      this.tasklists=res;
    });
  }

}
