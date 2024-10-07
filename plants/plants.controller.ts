import { Controller, Get } from '@nestjs/common';
import { PlantsService } from './plants.service';

@Controller()
export class PlantsController {
  constructor(private readonly plantsService: PlantsService) {}

  @Get()
  getHello(): string {
    return this.plantsService.getHello();
  }
}
