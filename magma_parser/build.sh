#!/bin/sh
pip3 install -r ../requirements.txt
antlr4 -v 4.13.0 \
       -Dlanguage=Python3 \
       -Xexact-output-dir \
       -o generated/ \
       -lib generated/ \
       -visitor \
       grammar/MagmaLexer.g4 grammar/MagmaParser.g4
