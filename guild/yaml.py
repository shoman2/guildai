# Copyright 2017 TensorHub, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division

import os

import yaml as _yaml

def _load(loader, node):
    filename = os.path.join(os.path.dirname(loader.name), node.value)
    with open(filename, "r") as f:
        return _yaml.safe_load(f)

_yaml.add_constructor("!load", _load, _yaml.SafeLoader)

safe_load = _yaml.safe_load
safe_dump = _yaml.safe_dump
YAMLError = _yaml.YAMLError
