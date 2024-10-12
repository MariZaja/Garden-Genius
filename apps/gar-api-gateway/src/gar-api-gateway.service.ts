import { Injectable } from '@nestjs/common';

@Injectable()
export class GarApiGatewayService {
  getHello(): string {
    return 'Hello World!';
  }
}
