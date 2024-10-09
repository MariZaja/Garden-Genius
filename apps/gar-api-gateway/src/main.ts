import { NestFactory } from '@nestjs/core';
import { GarApiGatewayModule } from './gar-api-gateway.module';

async function bootstrap() {
  const app = await NestFactory.create(GarApiGatewayModule);
  await app.listen(3000);
}
bootstrap();
