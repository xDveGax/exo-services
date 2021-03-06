from populate.populator.common.errors import ConfigurationError
from .forum_manager import ForumManager


def forum_constructor(loader, node):
    item = loader.construct_scalar(node)
    if not isinstance(item, str) or not item:
        raise ConfigurationError(
            'value {} cannot be interpreted as post'.format(item))
    return ForumManager().get_object(item)
