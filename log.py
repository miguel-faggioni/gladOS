#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
log = logging.getLogger(__file__)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.DEBUG)
