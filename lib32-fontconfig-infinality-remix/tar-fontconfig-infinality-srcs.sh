#!/bin/sh

VERSION=$1
NAME=fontconfig-infinality-remix-srcs-${VERSION}.tar.bz2

tar --owner=0 --group=0 -cvjSf $NAME fontconfig-infinality-remix-srcs
sha256sum $NAME
