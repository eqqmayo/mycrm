from math import ceil
from typing import Dict, Any, Callable
from utils.constants import ITEM_LIMIT, PAGE_LIMIT


def paginate(
    page: int, 
    get_count_func: Callable[[], int], 
    get_items_func: Callable[[int, int], Dict[str, Any]], 
    limit: int = ITEM_LIMIT
) -> Dict[str, Any]:

    items = get_items_func(page, limit)

    last_page = ceil(get_count_func() / limit)

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