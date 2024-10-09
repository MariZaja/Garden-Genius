import { Controller } from '@nestjs/common';
import { MessagePattern, Payload } from '@nestjs/microservices';
import { SpeciesService } from './species.service';
import {
  CreateSpeciesDto,
  SPECIES_PATTERNS,
  UpdateSpeciesDto,
} from '@app/contracts/species';

@Controller()
export class SpeciesController {
  constructor(private readonly speciesService: SpeciesService) {}

  @MessagePattern(SPECIES_PATTERNS.CREATE)
  create(@Payload() createSpeciesDto: CreateSpeciesDto) {
    return this.speciesService.create(createSpeciesDto);
  }

  @MessagePattern(SPECIES_PATTERNS.FIND_ALL)
  findAll() {
    return this.speciesService.findAll();
  }

  @MessagePattern(SPECIES_PATTERNS.FIND_ONE)
  findOne(@Payload() id: number) {
    return this.speciesService.findOne(id);
  }

  @MessagePattern(SPECIES_PATTERNS.UPDATE)
  update(@Payload() updateSpeciesDto: UpdateSpeciesDto) {
    return this.speciesService.update(updateSpeciesDto.id, updateSpeciesDto);
  }

  @MessagePattern(SPECIES_PATTERNS.REMOVE)
  remove(@Payload() id: number) {
    return this.speciesService.remove(id);
  }
}
