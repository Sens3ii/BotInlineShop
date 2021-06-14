from typing import List, Coroutine

from asgiref.sync import sync_to_async
from admin_side.api.models import Item, User


@sync_to_async
def add_user(user_id, full_name, username):
    try:
        return User(user_id=int(user_id), name=full_name, username=username).save()
    except Exception:
        return get_user(int(user_id))


@sync_to_async
def get_user(user_id: int) -> User:
    user = User.objects.filter(user_id=user_id).first()
    return user


@sync_to_async
def get_users() -> List[User]:
    users = User.objects.all()
    return users


@sync_to_async
def count_users():
    total = User.objects.all().count()
    return total


# Item functions
@sync_to_async
def add_item(**kwargs):
    new_item = Item(**kwargs).save()
    return new_item


@sync_to_async
def get_item(item_id) -> Item:
    item = Item.objects.filter(id=int(item_id)).first()
    return item


@sync_to_async
def get_items() -> List[Item]:
    items = Item.objects.all()
    return items


@sync_to_async
def count_items():
    total = Item.objects.all().count()
    return total


@sync_to_async
def get_items_by_query(query) -> List[Item]:
    items = Item.objects.filter(name__startswith=query)
    return items
