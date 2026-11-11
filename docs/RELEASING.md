# GitHub и выпуск версии

## Первое размещение

Репозиторий: https://github.com/Hozren/pikabu-elkashka, основная ветка main. Перед отправкой изменений получить актуальное состояние origin. Если история изменилась — совместить изменения, не использовать force push.

Не отправлять research, домашние пути, дампы браузера или секреты. Перед публичным размещением проверить статус прав на картинки: docs/THIRD_PARTY.md.

## Выпуск

1. Изменить version в extension/manifest.json и обновить CHANGELOG.md и README при необходимости.
2. Выполнить python3 scripts/check.py и python3 scripts/build.py.
3. Пройти docs/TESTING.md.
4. Закоммитить изменения, создать тег v<VERSION> и отправить его в согласованный репозиторий.
5. Дождаться workflow Build Chrome extension: тег v<VERSION> автоматически создаёт GitHub Release с ZIP и SHA256. Тег обязан совпадать с version в manifest. Повторный запуск обновляет вложения того же релиза.
6. Если используется Chrome Web Store, отдельно загрузить новую версию через кабинет. GitHub Release сам по себе не обновляет магазин.

Распакованные установки обновляются вручную. Автоматические обновления для пользователей Chrome Web Store предоставляет магазин.

CI публикует GitHub Release только для push тега v*. Для обычных push, pull request и ручного запуска сохраняет архив в Actions Artifacts на 30 дней. Публикация использует встроенный GITHUB_TOKEN с contents: write только в release job. Токены Chrome Web Store не нужны; магазин автоматически не публикуется.
