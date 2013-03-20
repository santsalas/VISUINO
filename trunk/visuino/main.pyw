#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Purpose:     Simply calls the VISUINO application. Also makes available the
#              execute() function, from which you can simply do:
#                  >>> import visuino
#                  >>> visuino.execute()     # will launch the application
#
# Author:      Nelso G. Jost (nelsojost@gmail.com)
#
#              This file is part of VISUINO project - Copyright (C) 2013
#
# Licence:     GNU GPL. Its simple: use and modify as you please, and redis-
#              tribute ONLY as 100% free and keeping the credits.
#-------------------------------------------------------------------------------
__all__ = ['execute']

import sys

from visuino.gui import AppVisuino


def execute():
    AppVisuino(sys.argv).execute()


if __name__ == '__main__':
    execute()