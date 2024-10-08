import { Inject, Injectable } from '@nestjs/common';
import { ClientProxy } from '@nestjs/microservices';
import {
  CreateSpeciesDto as ClientCreateSpeciesDto,
  SPECIES_PATTERNS,
  UpdateSpeciesDto as ClientUpdateSpeciesDto,
  SpeciesDto as ClientSpeciesDto,
} from '@app/contracts/species';
import { map } from 'rxjs'

import { SpeciesDto } from './dto/species.dto';
import { CreateSpeciesDto } from './dto/create-species.dto';
import { UpdateSpeciesDto } from './dto/update-species.dto';

@Injectable()
export class SpeciesService {
  constructor(@Inject('SPECIES_CLIENT') private speciesClient: ClientProxy) {}

  private mapSpeciesDto(speciesDto: ClientSpeciesDto): SpeciesDto {
    return {
      id: speciesDto.id,
      name: speciesDto.name,
      type: speciesDto.type,
    };
  }

  create(createSpeciesDto: CreateSpeciesDto) {
    return this.speciesClient.send<ClientSpeciesDto, ClientCreateSpeciesDto>(
      SPECIES_PATTERNS.CREATE,
      createSpeciesDto
    ).pipe(map(this.mapSpeciesDto));
  }

  findAll() {
    return this.speciesClient.send<ClientSpeciesDto>(
      SPECIES_PATTERNS.FIND_ALL,
      {}
    ).pipe(map(this.mapSpeciesDto));
  }

  findOne(id: number) {
    return this.speciesClient.send<ClientSpeciesDto>(
      SPECIES_PATTERNS.FIND_ONE,
      id
    ).pipe(map(this.mapSpeciesDto));
  }

  update(id: number, updateSpeciesDto: UpdateSpeciesDto) {
    return this.speciesClient.send<ClientSpeciesDto, ClientUpdateSpeciesDto>(
      SPECIES_PATTERNS.UPDATE, {
      id,
      ...updateSpeciesDto,
    }).pipe(map(this.mapSpeciesDto));
  }

  remove(id: number) {
    return this.speciesClient.send<ClientSpeciesDto>(
      SPECIES_PATTERNS.REMOVE,
      id
    ).pipe(map(this.mapSpeciesDto));
  }
}
