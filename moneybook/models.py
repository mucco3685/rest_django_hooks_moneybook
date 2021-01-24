from django.db import models
from django.utils import timezone, dateformat
import datetime
import uuid

# 未実装
# ondelete=SET(関数名)→削除された名前を文字列として入れ込みたい
# もしくは、名前(削除済み)のようにしたい
# ItemCategoryでは__str__(self)→self.itemだからいけるのでは？？？

class ItemCategory(models.Model):
  """どんぶり勘定のどんぶり部分"""
  class Meta:
    db_table = 'itemcategory'
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  item = models.CharField(max_length =20)
  upper_limit = models.IntegerField()

  def __str__(self):
    return self.item

class AllBook(models.Model):
  """全てのお金を使ったデータを記録"""
  class Meta:
    db_table = 'allbook'

  item_num = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, null=True)
  calc_method = models.BooleanField(default=False)
  price = models.IntegerField()
  date_of_use = models.CharField(
    '使用日',max_length=19,
    default = str(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    )
  date_of_regist = models.CharField(
    '登録日',max_length=19,
    default = str(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    )

  def __str__(self):
    return f'{self.date_of_regist} {self.item_num}{self.price}'