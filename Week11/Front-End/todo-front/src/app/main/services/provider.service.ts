import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {ITaskList} from '../models/todo'

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MyserService {
  [x: string]: any;

  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<ITaskList[]>{
    return this.get(`http://http://localhost:4200//api/task_lists/`,{});
  }

  getExactList(id: number): Promise<ITaskList>{
    return this.get(`http://localhost:4200/api/task_lists/${id}/`,{id})
  }
  getTasks(id: number): Promise<ITask[]> {
    return this.get(`http://127.0.0.1:8000/api/task_lists/${id}/tasks/`, {id});
  }

}
