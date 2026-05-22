# Deploy (Dinord)

## Изменение 1.2.2

Исправлен перевод опций Select с учётом doctype / Translation context (форма и фильтры списка).

## Prod / test / dev

```bash
cd apps/frappe_better_select_control
git pull upstream main   # или origin main, если remote так назван
cd ../..
bench build --app frappe_better_select_control
bench --site <sitename> clear-cache
# bench restart   # при необходимости
```

- Ветка: **main**
- Миграции, `install-app`, правки БД: **не требуются**
- Зависит от записей Translation с Context (например `Opportunity` для `Closed`)
