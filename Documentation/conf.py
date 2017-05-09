# -*- coding: utf-8 -*-
#
# Open vSwitch documentation build configuration file, created by
# sphinx-quickstart on Fri Sep 30 09:57:36 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import string
import sys

try:
    import ovs_sphinx_theme
    use_ovs_theme = True
except ImportError:
    print("Cannot find 'ovs_sphinx' package. Falling back to default theme.")
    use_ovs_theme = False

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.1'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = u'Open vSwitch'
copyright = u'2016, The Open vSwitch Development Community'
author = u'The Open vSwitch Development Community'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = None
filename = "../configure.ac"
with open(filename, 'rU') as f:
    for line in f:
        if 'AC_INIT' in line:
            # Parse "AC_INIT(openvswitch, 2.7.90, bugs@openvswitch.org)":
            release = line.split(',')[1].strip(string.whitespace + '[]')
            break
if release is None:
    sys.stderr.write('%s: failed to determine Open vSwitch version\n'
                     % filename)
    sys.exit(1)

# The short X.Y version.
#
# However, it's important to know the difference between, e.g., 2.7
# and 2.7.90, which can be very different versions (2.7.90 may be much
# closer to 2.8 than to 2.7), so check for that.
version = release if '.90' in release else '.'.join(release.split('.')[0:2])

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# If true, check the validity of #anchors in links.
linkcheck_anchors = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
if use_ovs_theme:
    html_theme = 'ovs'

# Add any paths that contain custom themes here, relative to this directory.
if use_ovs_theme:
    html_theme_path = [ovs_sphinx_theme.get_theme_dir()]
else:
    html_theme_path = []

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
html_logo = '_static/logo.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('ref/ovs-test.8', 'ovs-test',
     u'Check Linux drivers for performance, vlan and L3 tunneling problems',
     [author], 8),
    ('ref/ovs-vlan-test.8', 'ovs-vlan-test',
     u'Check Linux drivers for problems with vlan traffic',
     [author], 8)
]
