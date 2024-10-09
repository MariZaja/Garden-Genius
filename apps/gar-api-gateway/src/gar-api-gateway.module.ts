import { Module } from '@nestjs/common';
import { GarApiGatewayController } from './gar-api-gateway.controller';
import { GarApiGatewayService } from './gar-api-gateway.service';
import { SpeciesModule } from './species/species.module';
import { UsersModule } from './users/users.module';

@Module({
  imports: [UsersModule, SpeciesModule],
  controllers: [GarApiGatewayController],
  providers: [GarApiGatewayService],
})
export class GarApiGatewayModule {}
