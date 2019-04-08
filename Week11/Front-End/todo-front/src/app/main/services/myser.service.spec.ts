import { TestBed } from '@angular/core/testing';

import { MyserService } from './myser.service';

describe('MyserService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: MyserService = TestBed.get(MyserService);
    expect(service).toBeTruthy();
  });
});
