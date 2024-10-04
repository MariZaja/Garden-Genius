import { Injectable } from '@nestjs/common';

@Injectable()
export class PlantsService {
  getHello(): string {
    return 'This is plant';
  }
}
