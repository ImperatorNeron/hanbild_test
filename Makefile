MANAGE_UTF = python -Xutf8 manage.py

.PHONY: dump-catalog-fixtures
dump-fixtures-catalog:
	${MANAGE_UTF} dumpdata catalog.Categories catalog.Goods catalog.GoodsImage catalog.GoodsVideo catalog.GoodsCharacteristic --output fixtures/catalog.json

.PHONY: load-catalog-fixtures
load-fixtures:
	${MANAGE_UTF} loaddata fixtures/catalog.json