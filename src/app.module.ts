import { Module } from '@nestjs/common';
import { GardensModule } from './gardens/gardens.module';
import { PlantsModule } from './plants/plants.module';
import { UsersModule } from './users/users.module';
import { SpeciesModule } from './species/species.module';

@Module({
  imports: [GardensModule, PlantsModule, UsersModule, SpeciesModule],
  controllers: [],
  providers: [],
})
export class AppModule {}
