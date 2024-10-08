import { Module } from '@nestjs/common';
import { SpeciesModule } from './species/species.module';

@Module({
  imports: [SpeciesModule],
  controllers: [],
  providers: [],
})
export class SpeciesAppModule {}
