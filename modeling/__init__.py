from .example_model import ResnNet18

def build_model(cfg):
  model = ResNet18(cfg.MODEL.NUM_CLASSES)
  return model
