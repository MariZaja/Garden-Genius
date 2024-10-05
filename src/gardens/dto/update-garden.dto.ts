import { PartialType } from '@nestjs/mapped-types';
import { CreateGardenDto } from './create-garden.dto';

export class UpdateGardenDto extends PartialType(CreateGardenDto) {}
