# This file is licensed under the Affero General Public License (AGPL) version 3.
#
# Copyright (C) 2024 New Vector, Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# See the GNU Affero General Public License for more details:
# <https://www.gnu.org/licenses/agpl-3.0.html>.

from twisted.web.iweb import IRequest

class RendezVous:
    def __init__(self, base: str): ...
    def handle_post(self, request: IRequest): ...
    def handle_get(self, request: IRequest, session_id: str): ...
    def handle_put(self, request: IRequest, session_id: str): ...
    def handle_delete(self, request: IRequest, session_id: str): ...
