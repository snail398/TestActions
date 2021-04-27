#!/bin/bash
rm -r "./Assets/Plugins/LibsSymlinks"
mkdir "./Assets/Plugins/LibsSymlinks"
mkdir "./Assets/Plugins/LibsSymlinks/Editor"
# BODY_START
ln -s "../../../lib" "./Assets/Plugins/LibsSymlinks/lib"
# BODY_END
