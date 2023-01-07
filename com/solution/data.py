from dataclasses import dataclass, field
from typing import Dict
import json
import os
from com.solution.solutionlog import logger


@dataclass
class Data:
    item_json: str = field(
        default=os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../item.json')))
    shipping_json: str = field(
        default=os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../shipping.json')))
    items: Dict[str, Dict] = field(default=None)
    rates: Dict[str, float] = field(default=None)

    def __post_init__(self):
        self.reload_config()

    def reload_config(self):
        with open(self.item_json) as item_file:
            try:
                self.items = json.load(item_file)
            except Exception as err:
                logger.error(err)
        with open(self.shipping_json) as shipping_file:
            try:
                self.rates = json.load(shipping_file)
            except Exception as err:
                logger.error(err)


