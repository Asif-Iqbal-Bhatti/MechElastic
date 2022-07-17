#!/usr/bin/env python


def ductile_test(ratio):
    """Test for ductility."""
    return "ductile" if ratio > 1.75 else "brittle"
