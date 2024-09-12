MANAGE_UTF = python -Xutf8 manage.py

.PHONY: dump-catalog-fixtures
dump-catalog-fixtures:
	${MANAGE_UTF} dumpdata catalog.Categories catalog.Goods catalog.GoodsImage catalog.GoodsVideo catalog.GoodsCharacteristic --output fixtures/catalog.json

.PHONY: load-catalog-fixtures
load-catalog-fixtures:
	${MANAGE_UTF} loaddata fixtures/catalog.json