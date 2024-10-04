import { Test, TestingModule } from '@nestjs/testing';
import { PlantsController } from './plants.controller';
import { PlantsService } from './plants.service';

describe('AppController', () => {
  let appController: PlantsController;

  beforeEach(async () => {
    const app: TestingModule = await Test.createTestingModule({
      controllers: [PlantsController],
      providers: [PlantsService],
    }).compile();

    appController = app.get<PlantsController>(PlantsController);
  });

  describe('root', () => {
    it('should return "Hello World!"', () => {
      expect(appController.getHello()).toBe('This is plant');
    });
  });
});
