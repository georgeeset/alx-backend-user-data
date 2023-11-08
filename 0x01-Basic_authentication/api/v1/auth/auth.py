#!/usr/bin/env python3
"""
API authentication module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ will be used later, now, you dont
        need to take care of them """
        if path is None or not excluded_paths:
            return True
        for i in excluded_paths:
            if i.endswith('*') and path.startswith(i[:-1]):
                return False
            elif i in {path, path + '/'}:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ that returns None - request """
        pass

    def current_user(self, request=None) -> TypeVar('User'):
        """ Flask request object"""
        return None
