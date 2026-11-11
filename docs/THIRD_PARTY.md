# Происхождение изображений

Источник шести SVG: https://cs.pikabu.ru/apps/ub/5.4.1063/desktop/sprite.svg

Символы `icon--ui-kit__poop_m`, `poop_s`, `clown_m`, `clown_s`, `cock_m`, `cock_s` извлечены в самостоятельные SVG с сохранением viewBox и графического содержимого. Имена файлов совпадают с окончанием ID символа.

Дата исследования: 2026-11-11. Маппинг проверен на странице и в раскрытых ветках комментариев:
https://pikabu.ru/story/provozglashayu_yolku_novoy_kakashkoy_14516150

Текущие исходные реакции: christmastree (ID 35), skull (ID 27), dove (ID 11). Используются варианты m и s. ID задокументированы для диагностики, CSS их не изменяет.

Авторство и лицензия графики отдельно не подтверждены. Файлы не объявляются произведениями автора расширения и не включаются автоматически в будущую лицензию кода. До публичного распространения следует получить подходящее разрешение либо использовать собственные/лицензированные альтернативы, сохранив подтверждения прав и требуемую атрибуцию.

Исследовательские выгрузки страниц, сторонние JS-бандлы и пользовательские иллюстрации в репозиторий и ZIP не входят.

## Иконка расширения

Изображение предоставлено владельцем проекта в чате 2026-11-11. Белый фон удалён встроенным imagegen; PNG с настоящим альфа-каналом: docs/images/elkashka-transparent.png. Авторство исходной картинки отдельно не проверялось.

Промпт: background-extraction; remove only white/off-white background and floor shadow to genuine transparent alpha PNG; preserve subject, silhouette, colors, ornaments, star, face and internal white eye highlights; no redesign, no white halo, complete uncropped subject on square transparent canvas.

Иконки 16/32/48/128 уменьшены из результата с сохранением alpha. Для 128 px предусмотрено прозрачное поле минимум 16 px по краям.
