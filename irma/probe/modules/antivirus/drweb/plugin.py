#
# Copyright (c) 2013-2018 Quarkslab.
# This file is part of IRMA project.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the top-level directory
# of this distribution and at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# No part of the project, including this file, may be copied,
# modified, propagated, or distributed except according to the
# terms contained in the LICENSE file.

from .drweb import DrWeb
from ..interface import AntivirusPluginInterface

from irma.common.plugins import PluginMetaClass, BinaryDependency, \
    PlatformDependency
from irma.common.base.utils import IrmaProbeType


class DrWebPlugin(AntivirusPluginInterface, metaclass=PluginMetaClass):

    # =================
    #  plugin metadata
    # =================

    _plugin_name_ = "DrWeb"
    _plugin_display_name_ = DrWeb.name
    _plugin_author_ = "IRMA (c) Quarkslab"
    _plugin_version_ = "1.0.0"
    _plugin_category_ = IrmaProbeType.antivirus
    _plugin_description_ = "Plugin for DrWeb for Linux"
    _plugin_dependencies_ = [
        PlatformDependency('linux'),
        BinaryDependency(
            'drweb-ctl',
            help='drweb-ctl executable is provided by Dr Web antivirus'
        )
    ]

    # ================
    #  interface data
    # ================

    module_cls = DrWeb
