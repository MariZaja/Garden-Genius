import { Controller, Get } from '@nestjs/common';
import { GarApiGatewayService } from './gar-api-gateway.service';

@Controller()
export class GarApiGatewayController {
  constructor(private readonly garApiGatewayService: GarApiGatewayService) {}

  @Get()
  getHello(): string {
    return this.garApiGatewayService.getHello();
  }
}
