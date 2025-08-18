from math import ceil
from typing import Dict, Any, Callable
from flask import redirect, url_for
from utils.constants import ITEM_LIMIT, PAGE_LIMIT


def paginate(
    page: str, 
    endpoint: str,
    get_count_func: Callable[[], int], 
    get_items_func: Callable[[int, int], Dict[str, Any]], 
    limit: int = ITEM_LIMIT,
) -> Dict[str, Any]:

    try:
        page = int(page)
    except ValueError:
        return redirect(url_for(endpoint))

    last_page = ceil(get_count_func() / limit)

    if page < 1:
        return redirect(url_for(endpoint, page=1))
    if page > last_page:
        return redirect(url_for(endpoint, page=last_page))

    items = get_items_func(page, limit)
    pagination = {
        'start': (ceil(page / PAGE_LIMIT) - 1) * PAGE_LIMIT + 1,
        'end': min(ceil(page / PAGE_LIMIT) * PAGE_LIMIT, last_page),
        'current_page': page,
        'last_page': last_page,
    }

    return {
        'items': items,
        'pagination': pagination
    } 