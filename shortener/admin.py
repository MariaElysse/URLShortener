#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from shortener.models import shortenedURL

admin.site.register(shortenedURL)
