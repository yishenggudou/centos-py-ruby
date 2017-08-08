#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


class BorgTest(unittest.TestCase):
    def setUp(self):
        self.a = 1

    def test_initial_borg_state_shall_be_init(self):
        self.assertEqual(self.a, 1)
