#!/usr/bin/env python3
""" Take int arg and return random delay """

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """ Wait for random delay then return asyncio.Task object """
    return asyncio.create_task(wait_random(max_delay))
