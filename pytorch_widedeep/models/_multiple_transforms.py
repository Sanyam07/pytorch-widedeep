from torchvision.transforms import Compose

from ..wdtypes import *

class MultipleTransforms(object):

	def __init__(self, transforms:List):

		instantiated_transforms = []
		for transform in transforms:
			if isinstance(transform, type): instantiated_transforms.append(transform())
			else: instantiated_transforms.append(transform)
		self._transforms = instantiated_transforms

	def __call__(self):
		return Compose(self._transforms)