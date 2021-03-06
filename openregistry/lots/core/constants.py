# -*- coding: utf-8 -*-

from openprocurement.api.constants import (
    TZ,  # noqa forwarded import
    DOCUMENT_TYPES,  # noqa forwarded import
    ROUTE_PREFIX,  # noqa forwarded import
    IDENTIFIER_CODES # noqa forwarded import
)
from openprocurement.api.models.registry_models.ocds import LOKI_DOCUMENT_TYPES # noqa forwarded import


DEFAULT_LOT_TYPE = 'basic'

LOT_STATUSES = ["draft", "pending", "deleted", "verification", "recomposed",
                "active.salable", "pending.dissolution", "dissolved", "active.awaiting",
                "active.auction", "pending.sold", "sold"]
