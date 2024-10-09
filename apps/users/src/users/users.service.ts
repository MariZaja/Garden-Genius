import { Injectable } from '@nestjs/common';
import { CreateUserDto, UpdateUserDto, UserDto } from '@app/contracts/users';

@Injectable()
export class UsersService {
  private users: UserDto[] = [
    {
      id: 1,
      username: 'john123',
      email: 'john123@gmail.com',
      password: 'password',
    },
    {
      id: 2,
      username: 'jane123',
      email: 'jane123@mailsac.com',
      password: 'password',
    }
  ]

  create(createUserDto: CreateUserDto) {
    return 'This action adds a new user';
  }

  findAll() {
    return this.users;
  }

  findOne(id: number) {
    return this.users.find(user => user.id === id);
  }

  update(id: number, updateUserDto: UpdateUserDto) {
    return `This action updates a #${id} user`;
  }

  remove(id: number) {
    return `This action removes a #${id} user`;
  }
}
