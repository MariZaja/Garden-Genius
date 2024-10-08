import { Inject, Injectable } from '@nestjs/common';
import { ClientProxy } from '@nestjs/microservices';
import {
  CreateUserDto as CLientCreateUserDto,
  UpdateUserDto as ClientUpdateUserDto,
  UserDto as ClientUserDto,
  USERS_PATTERNS,
} from '@app/contracts/users';
import { map } from 'rxjs';
import { CreateUserDto } from './dto/create-user.dto';
import { UpdateUserDto } from './dto/update-user.dto';
import { UserDto } from './dto/user.dto';

@Injectable()
export class UsersService {
  constructor(@Inject('USERS_CLIENT') private usersClient: ClientProxy) {}

  private mapUserDto(userDto: ClientUserDto): UserDto {
    return {
      username: userDto.username,
      email: userDto.email,
    }
  }

  create(createUserDto: CreateUserDto) {
    return this.usersClient.send<ClientUserDto, CLientCreateUserDto>(
      USERS_PATTERNS.CREATE,
      createUserDto,
    ).pipe(map(this.mapUserDto));
  }

  findAll() {
    return this.usersClient
      .send<ClientUserDto[]>(USERS_PATTERNS.FIND_ALL, {})
      .pipe(map((users) => users.map(this.mapUserDto)));
  }

  findOne(id: number) {
    return this.usersClient.send<ClientUserDto>(USERS_PATTERNS.FIND_ONE, id).pipe(map(this.mapUserDto));
  }

  update(id: number, updateUserDto: UpdateUserDto) {
    return this.usersClient.send<ClientUserDto, ClientUpdateUserDto>(
      USERS_PATTERNS.UPDATE,
      { id, ...updateUserDto },
    ).pipe(map(this.mapUserDto));
  }

  remove(id: number) {
    return this.usersClient.send<ClientUserDto>(USERS_PATTERNS.REMOVE, id).pipe(map(this.mapUserDto));
  }
}
