import { Test, TestingModule } from '@nestjs/testing';
import { GarApiGatewayController } from './gar-api-gateway.controller';
import { GarApiGatewayService } from './gar-api-gateway.service';

describe('GarApiGatewayController', () => {
  let garApiGatewayController: GarApiGatewayController;

  beforeEach(async () => {
    const app: TestingModule = await Test.createTestingModule({
      controllers: [GarApiGatewayController],
      providers: [GarApiGatewayService],
    }).compile();

    garApiGatewayController = app.get<GarApiGatewayController>(GarApiGatewayController);
  });

  describe('root', () => {
    it('should return "Hello World!"', () => {
      expect(garApiGatewayController.getHello()).toBe('Hello World!');
    });
  });
});
