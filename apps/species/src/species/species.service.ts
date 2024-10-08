import { Injectable } from '@nestjs/common';
import {
  CreateSpeciesDto,
  SpeciesDto,
  UpdateSpeciesDto,
} from '@app/contracts/species';

@Injectable()
export class SpeciesService {
  private species: SpeciesDto[] = [
    {
      id: 1,
      name: 'Sosna',
      type: 'Tree',
    },
    {
      id: 2,
      name: 'Jodla',
      type: 'Tree',
    }
  ]

  create(createSpeciesDto: CreateSpeciesDto) {
    return 'This action adds a new species';
  }

  findAll() {
    return this.species;
  }

  findOne(id: number) {
    return `This action returns a #${id} species`;
  }

  update(id: number, updateSpeciesDto: UpdateSpeciesDto) {
    return `This action updates a #${id} species`;
  }

  remove(id: number) {
    return `This action removes a #${id} species`;
  }
}
