# Copyright 2023 Nisaba Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for txn2ltn."""

from absl.testing import absltest

from nisaba.scripts.natural_translit.phonology import txn2ltn
from nisaba.scripts.utils import test_util

_TEST_CASES = [
    (lambda: txn2ltn.TRANSLIT_DIPHTHONG, [
        ('{a}{+}{i}', '`s_ai`'),
    ]),
    (lambda: txn2ltn.TRANSLIT_AFFRICATE, [
        ('{t}{+}{sh}', '`s_ch`'),
    ]),
    (lambda: txn2ltn.TRANSLIT_BASE, [
        ('{t}{sh}', '`t``s_sh`'),
    ]),
    (lambda: txn2ltn.IGNORE_MODIFIERS, [
        ('{:h}', '`DEL`'),
    ]),
    (lambda: txn2ltn.DEL_REPEATED_SUBSTRING, [
        ('`s_sh``s_sh`', '`s_sh`'),
    ]),
]


class Txn2IpaTest(test_util.FstTestCase):

  def test_all(self):
    self.assertFstStrIoTestCases(_TEST_CASES)


if __name__ == '__main__':
  absltest.main()
