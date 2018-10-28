#!/usr/bin/env python3

# fc-infinality-update-config
# Author: Philip Deljanov <philip@pdeljanov.com>
#
# This utility examines changes to the list of installed fonts and, as appropriate, links and/or unlinks font-specific
# configuration files into /etc/fonts/conf.d/. Once complete the font cache is refreshed.
#
# This script should be run after installing or removing fonts from the system.
#
# Font configuration files are discovered from /etc/fonts/conf.avail/fonts/. They should be nameds in the following
# format: [##]-<family name>-<specifier>.conf.
#
# The initial [##]- is ignored. Use two digits to specify a priority level for the configuration. This is useful for
# creating a generic conf file for one family, but allowing secondary conf files to be used to tweak more specific
# variations of the same font family (i.e., 00-noto-sans.conf, 10-noto-sans-light.conf).
#
# <Family Name> is the font family name. Lower case. Underscores between words in the family name.
# <Specifier> is used to denote a variation of the font, for example "light".
#
# Given an installed font, this script will link in the generic font family conf file, followed by the varation's conf
# file as available. Therefore, conf files for font variations should have a higher priority.
