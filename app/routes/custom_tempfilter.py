#!/usr/bin/env python3
# encoding: utf-8
def init_ctfilter(app):
    app.add_template_filter(eval_filter,'eval')


def eval_filter(i):
    return eval(i)