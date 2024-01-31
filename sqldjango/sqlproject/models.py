from django.db import models


class Bills(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    # 账单名称，应收
    billname = models.TextField(
        db_column="BillName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    # 应收金额
    billamount = models.DecimalField(
        db_column="BillAmount", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    paymentdate = models.DateTimeField(
        db_column="PaymentDate", blank=True, null=True
    )  # Field name made lowercase.
    billclass = models.IntegerField(db_column="BillClass")  # Field name made lowercase.
    isconfirmed = models.BooleanField(
        db_column="IsConfirmed"
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    saleorderid = models.ForeignKey(
        "Saleorders", models.DO_NOTHING, db_column="SaleOrderId", blank=True, null=True
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    confirmeruserid = models.BigIntegerField(
        db_column="ConfirmerUserId"
    )  # Field name made lowercase.
    billreceivedamount = models.DecimalField(
        db_column="BillReceivedAmount", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    receiptamount = models.DecimalField(
        db_column="ReceiptAmount", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    receiptdate = models.DateTimeField(
        db_column="ReceiptDate", blank=True, null=True
    )  # Field name made lowercase.
    paymentstatus = models.IntegerField(
        db_column="PaymentStatus"
    )  # Field name made lowercase.
    receiptstatus = models.IntegerField(
        db_column="ReceiptStatus"
    )  # Field name made lowercase.
    isreceiptfirst = models.BooleanField(
        db_column="IsReceiptFirst"
    )  # Field name made lowercase.
    isexportreceiptexcel = models.BooleanField(
        db_column="IsExportReceiptExcel"
    )  # Field name made lowercase.
    remarksforreceiptfirst = models.TextField(
        db_column="RemarksForReceiptFirst",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    finishpaymentdate = models.DateTimeField(
        db_column="FinishPaymentDate", blank=True, null=True
    )  # Field name made lowercase.
    billcustomername = models.TextField(
        db_column="BillCustomerName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    isforeigncurrency = models.BooleanField(
        db_column="IsForeignCurrency"
    )  # Field name made lowercase.
    foreigncurrencyname = models.TextField(
        db_column="ForeignCurrencyName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    foreigncurrencysymbol = models.TextField(
        db_column="ForeignCurrencySymbol",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    exchangerate = models.DecimalField(
        db_column="ExchangeRate", max_digits=20, decimal_places=8
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Bills"


class Brands(models.Model):
    id = models.AutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    brandname = models.TextField(
        db_column="BrandName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Brands"


class Checkrepodetails(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    productid = models.BigIntegerField(
        db_column="ProductId"
    )  # Field name made lowercase.
    productname = models.TextField(
        db_column="ProductName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    productcode = models.TextField(
        db_column="ProductCode", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    # 产品类别名称
    producttypename = models.TextField(
        db_column="ProductTypeName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    # 产品品牌
    productbrandname = models.TextField(
        db_column="ProductBrandName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    numbeforecheck = models.IntegerField(
        db_column="NumBeforeCheck"
    )  # Field name made lowercase.
    numaftercheck = models.IntegerField(
        db_column="NumAfterCheck"
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    checkrepoid = models.ForeignKey(
        "Checkrepoes", models.DO_NOTHING, db_column="CheckRepoId"
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        db_table = "CheckRepoDetails"


class Checkrepoes(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    checkrepocode = models.TextField(
        db_column="CheckRepoCode", db_collation="Chinese_PRC_CI_AS"
    )  # Field name made lowercase.
    checkreponame = models.TextField(
        db_column="CheckRepoName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    checkstatus = models.IntegerField(
        db_column="CheckStatus"
    )  # Field name made lowercase.
    checkcompletedtime = models.DateTimeField(
        db_column="CheckCompletedTime", blank=True, null=True
    )  # Field name made lowercase.
    checker = models.TextField(
        db_column="Checker", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    warehouseid = models.ForeignKey(
        "Warehouses", models.DO_NOTHING, db_column="WarehouseId"
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "CheckRepoes"


class Customercontracts(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    saleorderid = models.ForeignKey(
        "Saleorders", models.DO_NOTHING, db_column="SaleOrderId"
    )  # Field name made lowercase.
    mycompanyid = models.IntegerField(
        db_column="MyCompanyId"
    )  # Field name made lowercase.
    uploaduserid = models.IntegerField(
        db_column="UploadUserId"
    )  # Field name made lowercase.
    filename = models.TextField(
        db_column="FileName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    contracttime = models.DateTimeField(
        db_column="ContractTime", blank=True, null=True
    )  # Field name made lowercase.
    uploadtime = models.DateTimeField(
        db_column="UploadTime", blank=True, null=True
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    downloadurl = models.TextField(
        db_column="DownloadUrl", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "CustomerContracts"


# 客户接收表
class Customerreceivers(models.Model):
    id = models.AutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    receivername = models.TextField(
        db_column="ReceiverName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    receiverphone = models.TextField(
        db_column="ReceiverPhone",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    receiveraddress = models.TextField(
        db_column="ReceiverAddress",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    receiverpostcode = models.TextField(
        db_column="ReceiverPostCode",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    customerid = models.ForeignKey(
        "Customers", models.DO_NOTHING, db_column="CustomerId"
    )  # Field name made lowercase.
    addressclass = models.IntegerField(
        db_column="AddressClass"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "CustomerReceivers"


# 客户表
class Customers(models.Model):
    id = models.AutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    name = models.TextField(
        db_column="Name", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    address = models.TextField(
        db_column="Address", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    contactperson = models.TextField(
        db_column="ContactPerson",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contactphone = models.TextField(
        db_column="ContactPhone",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    # 传真
    fax = models.TextField(
        db_column="Fax", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    accountbank = models.TextField(
        db_column="AccountBank", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    accountid = models.TextField(
        db_column="AccountId", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    texid = models.TextField(
        db_column="TexId", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    # 省份
    province = models.TextField(
        db_column="Province", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    mobile = models.TextField(
        db_column="Mobile", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    email = models.TextField(
        db_column="Email", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    customerclass = models.IntegerField(
        db_column="CustomerClass"
    )  # Field name made lowercase.
    ismycompany = models.BooleanField(
        db_column="IsMyCompany"
    )  # Field name made lowercase.
    remindnobusinessdays = models.IntegerField(
        db_column="RemindNoBusinessDays"
    )  # Field name made lowercase.
    remindtime = models.IntegerField(
        db_column="RemindTime"
    )  # Field name made lowercase.
    cancelremaindthistimedate = models.DateTimeField(
        db_column="CancelRemaindThisTimeDate", blank=True, null=True
    )  # Field name made lowercase.
    cancelremainduserid = models.BigIntegerField(
        db_column="CancelRemaindUserId", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Customers"


class Departments(models.Model):
    id = models.AutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    departmentname = models.TextField(
        db_column="DepartmentName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Departments"


class Directshipdetails(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    itemname = models.TextField(
        db_column="ItemName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    itemcode = models.TextField(
        db_column="ItemCode", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    shipnumber = models.IntegerField(
        db_column="ShipNumber"
    )  # Field name made lowercase.
    shipstatus = models.IntegerField(
        db_column="ShipStatus"
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    shiplistid = models.ForeignKey(
        "Shiplists", models.DO_NOTHING, db_column="ShipListId", blank=True, null=True
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    isreceipt = models.BooleanField(db_column="IsReceipt")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "DirectShipDetails"


class Ereceiptfiles(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    receiptid = models.ForeignKey(
        "Receipts", models.DO_NOTHING, db_column="ReceiptId"
    )  # Field name made lowercase.
    mycompanyid = models.IntegerField(
        db_column="MyCompanyId"
    )  # Field name made lowercase.
    uploaduserid = models.IntegerField(
        db_column="UploadUserId"
    )  # Field name made lowercase.
    downloadurl = models.TextField(
        db_column="DownloadUrl", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    filename = models.TextField(
        db_column="FileName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    uploadtime = models.DateTimeField(
        db_column="UploadTime", blank=True, null=True
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "EReceiptFiles"


# 交换订单详情
class Exchangeorderdetails(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    exchangeorderid = models.ForeignKey(
        "Exchangeorders", models.DO_NOTHING, db_column="ExchangeOrderId"
    )  # Field name made lowercase.
    productid = models.ForeignKey(
        "Products", models.DO_NOTHING, db_column="ProductId", blank=True, null=True
    )  # Field name made lowercase.
    ordernumber = models.IntegerField(
        db_column="OrderNumber"
    )  # Field name made lowercase.
    realprice = models.DecimalField(
        db_column="RealPrice", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    requestedshipdate = models.DateTimeField(
        db_column="RequestedShipDate", blank=True, null=True
    )  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    fromwarehouseid = models.ForeignKey(
        "Warehouses",
        models.DO_NOTHING,
        db_column="FromWarehouseId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    towarehouseid = models.ForeignKey(
        "Warehouses",
        models.DO_NOTHING,
        db_column="ToWarehouseId",
        related_name="exchangeorderdetails_towarehouseid_set",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ExchangeOrderDetails"


# 交换订单,就是子公司之间的互相交换
class Exchangeorders(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    ordercode = models.TextField(
        db_column="OrderCode", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    frommycompanyname = models.TextField(
        db_column="FromMyCompanyName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    tomycompanyname = models.TextField(
        db_column="ToMyCompanyName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    orderconfirmeddate = models.DateTimeField(
        db_column="OrderConfirmedDate"
    )  # Field name made lowercase.
    newaddeddate = models.DateTimeField(
        db_column="NewAddedDate", blank=True, null=True
    )  # Field name made lowercase.
    finisheddate = models.DateTimeField(
        db_column="FinishedDate", blank=True, null=True
    )  # Field name made lowercase.
    orderstatus = models.IntegerField(
        db_column="OrderStatus"
    )  # Field name made lowercase.
    requirefinalpaydate = models.DateTimeField(
        db_column="RequireFinalPayDate", blank=True, null=True
    )  # Field name made lowercase.
    shipdate = models.DateTimeField(
        db_column="ShipDate", blank=True, null=True
    )  # Field name made lowercase.
    istaxfreepay = models.BooleanField(
        db_column="IsTaxFreePay"
    )  # Field name made lowercase.
    confirmeruserid = models.BigIntegerField(
        db_column="ConfirmerUserId", blank=True, null=True
    )  # Field name made lowercase.
    finisheduserid = models.BigIntegerField(
        db_column="FinishedUserId", blank=True, null=True
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    # 销售订单编号
    saleordercode = models.TextField(
        db_column="SaleOrderCode",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    # 购买订单编号
    purchaseordercode = models.TextField(
        db_column="PurchaseOrderCode",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ExchangeOrders"


# 财政记录表
class Financerecords(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    amount = models.DecimalField(
        db_column="Amount", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    paymenttime = models.DateTimeField(
        db_column="PaymentTime", blank=True, null=True
    )  # Field name made lowercase.
    # 支付公司
    paymentparty = models.TextField(
        db_column="PaymentParty",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    # 账单编号，对应bill那个表
    billid = models.ForeignKey(
        Bills, models.DO_NOTHING, db_column="BillId", blank=True, null=True
    )  # Field name made lowercase.
    payid = models.ForeignKey(
        "Pays", models.DO_NOTHING, db_column="PayId", blank=True, null=True
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    serialnumber = models.TextField(
        db_column="SerialNumber", db_collation="Chinese_PRC_CI_AS"
    )  # Field name made lowercase.
    amountrmb = models.DecimalField(
        db_column="AmountRMB", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    isforeigncurrency = models.BooleanField(
        db_column="IsForeignCurrency"
    )  # Field name made lowercase.
    foreigncurrencyname = models.TextField(
        db_column="ForeignCurrencyName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    foreigncurrencysymbol = models.TextField(
        db_column="ForeignCurrencySymbol",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "FinanceRecords"


class Inrepodetails(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    inrepocode = models.TextField(
        db_column="InRepoCode", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    receivenumber = models.IntegerField(
        db_column="ReceiveNumber"
    )  # Field name made lowercase.
    receivednumber = models.IntegerField(
        db_column="ReceivedNumber"
    )  # Field name made lowercase.
    receivestatus = models.IntegerField(
        db_column="ReceiveStatus"
    )  # Field name made lowercase.
    warehouseid = models.ForeignKey(
        "Warehouses", models.DO_NOTHING, db_column="WarehouseId", blank=True, null=True
    )  # Field name made lowercase.
    purchaseorderdetailid = models.ForeignKey(
        "Purchaseorderdetails",
        models.DO_NOTHING,
        db_column="PurchaseOrderDetailId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    directshipnumber = models.IntegerField(
        db_column="DirectShipNumber"
    )  # Field name made lowercase.
    finishedreceivedate = models.DateTimeField(
        db_column="FinishedReceiveDate", blank=True, null=True
    )  # Field name made lowercase.
    inrepotype = models.IntegerField(
        db_column="InRepoType"
    )  # Field name made lowercase.
    returnproductid = models.ForeignKey(
        "Products",
        models.DO_NOTHING,
        db_column="ReturnProductId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    shippingorderid = models.ForeignKey(
        "Shippingorders",
        models.DO_NOTHING,
        db_column="ShippingOrderId",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "InRepoDetails"


class Mycompanies(models.Model):
    id = models.AutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    name = models.TextField(
        db_column="Name", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    province = models.TextField(
        db_column="Province", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    address = models.TextField(
        db_column="Address", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    contactperson = models.TextField(
        db_column="ContactPerson",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mobile = models.TextField(
        db_column="Mobile", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    email = models.TextField(
        db_column="Email", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    contactphone = models.TextField(
        db_column="ContactPhone",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    fax = models.TextField(
        db_column="Fax", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    accountbank = models.TextField(
        db_column="AccountBank", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    accountid = models.TextField(
        db_column="AccountId", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    texid = models.TextField(
        db_column="TexId", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    isdefault = models.BooleanField(db_column="IsDefault")  # Field name made lowercase.
    prefix = models.TextField(
        db_column="Prefix", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "MyCompanies"


class Noneorderoutrepodetails(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    outrepodetailid = models.ForeignKey(
        "Outrepodetails", models.DO_NOTHING, db_column="OutRepoDetailId"
    )  # Field name made lowercase.
    noneorderoutrepodetailstatus = models.IntegerField(
        db_column="NoneOrderOutRepoDetailStatus"
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    shippednumber = models.IntegerField(
        db_column="ShippedNumber"
    )  # Field name made lowercase.
    cost = models.DecimalField(
        db_column="Cost", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    saledate = models.DateTimeField(
        db_column="SaleDate", blank=True, null=True
    )  # Field name made lowercase.
    gifteddate = models.DateTimeField(
        db_column="GiftedDate", blank=True, null=True
    )  # Field name made lowercase.
    inrepodetailid = models.ForeignKey(
        Inrepodetails,
        models.DO_NOTHING,
        db_column="InRepoDetailId",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "NoneOrderOutRepoDetails"


# 订单合同详细信息
class Ordercontractdetails(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    # 订单合同id
    ordercontractid = models.ForeignKey(
        "Ordercontracts", models.DO_NOTHING, db_column="OrderContractId"
    )  # Field name made lowercase.
    brandname = models.TextField(
        db_column="BrandName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    typename = models.TextField(
        db_column="TypeName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    productname = models.TextField(
        db_column="ProductName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    productcode = models.TextField(
        db_column="ProductCode", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    ordernumber = models.IntegerField(
        db_column="OrderNumber"
    )  # Field name made lowercase.
    realprice = models.DecimalField(
        db_column="RealPrice", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    requestedshipdate = models.DateTimeField(
        db_column="RequestedShipDate", blank=True, null=True
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    foreigncurrencyprice = models.DecimalField(
        db_column="ForeignCurrencyPrice", max_digits=20, decimal_places=8
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "OrderContractDetails"


# 订单合同
class Ordercontracts(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    purchaseordersuppliername = models.TextField(
        db_column="PurchaseOrderSupplierName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    purchaseorderprice = models.DecimalField(
        db_column="PurchaseOrderPrice", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    saleordercustomername = models.TextField(
        db_column="SaleOrderCustomerName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    saleorderprice = models.DecimalField(
        db_column="SaleOrderPrice", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    ordercode = models.TextField(
        db_column="OrderCode", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    orderdate = models.DateTimeField(
        db_column="OrderDate", blank=True, null=True
    )  # Field name made lowercase.
    paymentmode = models.IntegerField(
        db_column="PaymentMode"
    )  # Field name made lowercase.
    isrequirereceiptbeforepay = models.BooleanField(
        db_column="IsRequireReceiptBeforePay"
    )  # Field name made lowercase.
    istaxfreepay = models.BooleanField(
        db_column="IsTaxFreePay"
    )  # Field name made lowercase.
    prepayratio = models.IntegerField(
        db_column="PrePayRatio"
    )  # Field name made lowercase.
    requireprepaydate = models.DateTimeField(
        db_column="RequirePrePayDate", blank=True, null=True
    )  # Field name made lowercase.
    requirefinalpaydate = models.DateTimeField(
        db_column="RequireFinalPayDate", blank=True, null=True
    )  # Field name made lowercase.
    location = models.TextField(
        db_column="Location", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    contract01title = models.TextField(
        db_column="Contract01Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract01text = models.TextField(
        db_column="Contract01Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract02title = models.TextField(
        db_column="Contract02Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract02text = models.TextField(
        db_column="Contract02Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract03title = models.TextField(
        db_column="Contract03Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract03text = models.TextField(
        db_column="Contract03Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract04title = models.TextField(
        db_column="Contract04Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract04text = models.TextField(
        db_column="Contract04Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract05title = models.TextField(
        db_column="Contract05Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract05text = models.TextField(
        db_column="Contract05Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract06title = models.TextField(
        db_column="Contract06Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract06text = models.TextField(
        db_column="Contract06Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract07title = models.TextField(
        db_column="Contract07Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract07text = models.TextField(
        db_column="Contract07Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract08title = models.TextField(
        db_column="Contract08Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract08text = models.TextField(
        db_column="Contract08Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract09title = models.TextField(
        db_column="Contract09Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract09text = models.TextField(
        db_column="Contract09Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract10title = models.TextField(
        db_column="Contract10Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract10text = models.TextField(
        db_column="Contract10Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract11title = models.TextField(
        db_column="Contract11Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract11text = models.TextField(
        db_column="Contract11Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract12title = models.TextField(
        db_column="Contract12Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract12text = models.TextField(
        db_column="Contract12Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract13title = models.TextField(
        db_column="Contract13Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract13text = models.TextField(
        db_column="Contract13Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mycompanyinfo_name = models.TextField(
        db_column="MyCompanyInfo_Name",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mycompanyinfo_province = models.TextField(
        db_column="MyCompanyInfo_Province",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mycompanyinfo_address = models.TextField(
        db_column="MyCompanyInfo_Address",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mycompanyinfo_contactperson = models.TextField(
        db_column="MyCompanyInfo_ContactPerson",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mycompanyinfo_mobile = models.TextField(
        db_column="MyCompanyInfo_Mobile",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mycompanyinfo_email = models.TextField(
        db_column="MyCompanyInfo_Email",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mycompanyinfo_contactphone = models.TextField(
        db_column="MyCompanyInfo_ContactPhone",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mycompanyinfo_fax = models.TextField(
        db_column="MyCompanyInfo_Fax",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mycompanyinfo_accountbank = models.TextField(
        db_column="MyCompanyInfo_AccountBank",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mycompanyinfo_accountid = models.TextField(
        db_column="MyCompanyInfo_AccountId",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mycompanyinfo_texid = models.TextField(
        db_column="MyCompanyInfo_TexId",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    othercompanyinfo_name = models.TextField(
        db_column="OtherCompanyInfo_Name",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    othercompanyinfo_province = models.TextField(
        db_column="OtherCompanyInfo_Province",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    othercompanyinfo_address = models.TextField(
        db_column="OtherCompanyInfo_Address",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    othercompanyinfo_contactperson = models.TextField(
        db_column="OtherCompanyInfo_ContactPerson",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    othercompanyinfo_mobile = models.TextField(
        db_column="OtherCompanyInfo_Mobile",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    othercompanyinfo_contactphone = models.TextField(
        db_column="OtherCompanyInfo_ContactPhone",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    othercompanyinfo_fax = models.TextField(
        db_column="OtherCompanyInfo_Fax",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    othercompanyinfo_email = models.TextField(
        db_column="OtherCompanyInfo_Email",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    othercompanyinfo_accountbank = models.TextField(
        db_column="OtherCompanyInfo_AccountBank",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    othercompanyinfo_accountid = models.TextField(
        db_column="OtherCompanyInfo_AccountId",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    othercompanyinfo_texid = models.TextField(
        db_column="OtherCompanyInfo_TexId",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    mycompanyinfo_prefix = models.TextField(
        db_column="MyCompanyInfo_PreFix",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    isforeigncurrency = models.BooleanField(
        db_column="IsForeignCurrency"
    )  # Field name made lowercase.
    foreigncurrencyname = models.TextField(
        db_column="ForeignCurrencyName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    foreigncurrencysymbol = models.TextField(
        db_column="ForeignCurrencySymbol",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    exchangerate = models.DecimalField(
        db_column="ExchangeRate", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    saleorderpricebydiscount = models.DecimalField(
        db_column="SaleOrderPriceByDiscount", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    purchaseorderpricebydiscount = models.DecimalField(
        db_column="PurchaseOrderPriceByDiscount", max_digits=20, decimal_places=8
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "OrderContracts"


# 回购详细信息
class Outrepodetails(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    shipnumber = models.IntegerField(
        db_column="ShipNumber"
    )  # Field name made lowercase.
    iscompleted = models.BooleanField(
        db_column="IsCompleted"
    )  # Field name made lowercase.
    saleorderdetailid = models.ForeignKey(
        "Saleorderdetails", models.DO_NOTHING, db_column="SaleOrderDetailId"
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    outrepocode = models.TextField(
        db_column="OutRepoCode", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    shiplistid = models.ForeignKey(
        "Shiplists", models.DO_NOTHING, db_column="ShipListId", blank=True, null=True
    )  # Field name made lowercase.
    # 仓库id
    warehouseid = models.ForeignKey(
        "Warehouses", models.DO_NOTHING, db_column="WarehouseId", blank=True, null=True
    )  # Field name made lowercase.
    shipstatus = models.IntegerField(
        db_column="ShipStatus"
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    realcost = models.DecimalField(
        db_column="RealCost", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    isnoneorder = models.BooleanField(
        db_column="IsNoneOrder"
    )  # Field name made lowercase.
    realoutrepoproductid = models.BigIntegerField(
        db_column="RealOutRepoProductId", blank=True, null=True
    )  # Field name made lowercase.
    realoutrepoproductcode = models.TextField(
        db_column="RealOutRepoProductCode",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    realoutrepoproductname = models.TextField(
        db_column="RealOutRepoProductName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    realoutrepoproducttypename = models.TextField(
        db_column="RealOutRepoProductTypeName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    realoutrepoproductbrandname = models.TextField(
        db_column="RealOutRepoProductBrandName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    shippingorderid = models.ForeignKey(
        "Shippingorders",
        models.DO_NOTHING,
        db_column="ShippingOrderId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    haswritenreceipt = models.BooleanField(
        db_column="HasWritenReceipt"
    )  # Field name made lowercase.
    receiptid = models.ForeignKey(
        "Receipts", models.DO_NOTHING, db_column="ReceiptId", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "OutRepoDetails"


class Pays(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    payname = models.TextField(
        db_column="PayName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    payamount = models.DecimalField(
        db_column="PayAmount", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    paymentdate = models.DateTimeField(
        db_column="PaymentDate", blank=True, null=True
    )  # Field name made lowercase.
    payclass = models.IntegerField(db_column="PayClass")  # Field name made lowercase.
    isconfirmed = models.BooleanField(
        db_column="IsConfirmed"
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    payoutedamount = models.DecimalField(
        db_column="PayOutedAmount", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    purchaseorderid = models.ForeignKey(
        "Purchaseorders",
        models.DO_NOTHING,
        db_column="PurchaseOrderId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    paymentstatus = models.IntegerField(
        db_column="PaymentStatus"
    )  # Field name made lowercase.
    receiptstatus = models.IntegerField(
        db_column="ReceiptStatus"
    )  # Field name made lowercase.
    receiptamount = models.DecimalField(
        db_column="ReceiptAmount", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    receiptdate = models.DateTimeField(
        db_column="ReceiptDate", blank=True, null=True
    )  # Field name made lowercase.
    finishpaymentdate = models.DateTimeField(
        db_column="FinishPaymentDate", blank=True, null=True
    )  # Field name made lowercase.
    shippingorderid = models.ForeignKey(
        "Shippingorders",
        models.DO_NOTHING,
        db_column="ShippingOrderId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    paysuppliername = models.TextField(
        db_column="PaySupplierName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    isforeigncurrency = models.BooleanField(
        db_column="IsForeignCurrency"
    )  # Field name made lowercase.
    foreigncurrencyname = models.TextField(
        db_column="ForeignCurrencyName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    foreigncurrencysymbol = models.TextField(
        db_column="ForeignCurrencySymbol",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    exchangerate = models.DecimalField(
        db_column="ExchangeRate", max_digits=20, decimal_places=8
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Pays"


class Productreposnaps(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    snapid = models.IntegerField(db_column="SnapId")  # Field name made lowercase.
    numberinrepo = models.IntegerField(
        db_column="NumberInRepo"
    )  # Field name made lowercase.
    avgcost = models.DecimalField(
        db_column="AvgCost", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    productid = models.ForeignKey(
        "Products", models.DO_NOTHING, db_column="ProductId"
    )  # Field name made lowercase.
    warehouseid = models.ForeignKey(
        "Warehouses", models.DO_NOTHING, db_column="WarehouseId"
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ProductRepoSnaps"


# 产品回购更新日志
class Productrepoupdatelogs(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    newproductid = models.BigIntegerField(
        db_column="NewProductId"
    )  # Field name made lowercase.
    newwarehouseid = models.IntegerField(
        db_column="NewWarehouseId"
    )  # Field name made lowercase.
    newnumberinrepo = models.IntegerField(
        db_column="NewNumberInRepo"
    )  # Field name made lowercase.
    newavgcost = models.DecimalField(
        db_column="NewAvgCost", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    newnumberlocked = models.IntegerField(
        db_column="NewNumberLocked"
    )  # Field name made lowercase.
    beforenumberinrepo = models.IntegerField(
        db_column="BeforeNumberInRepo"
    )  # Field name made lowercase.
    beforeavgcost = models.DecimalField(
        db_column="BeforeAvgCost", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    beforenumberlocked = models.IntegerField(
        db_column="BeforeNumberLocked"
    )  # Field name made lowercase.
    beforelastmodificationtime = models.DateTimeField(
        db_column="BeforeLastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    approvestatus = models.IntegerField(
        db_column="ApproveStatus"
    )  # Field name made lowercase.
    approvedate = models.DateTimeField(
        db_column="ApproveDate", blank=True, null=True
    )  # Field name made lowercase.
    approveremarks = models.TextField(
        db_column="ApproveRemarks",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    approveruserid = models.BigIntegerField(
        db_column="ApproverUserId", blank=True, null=True
    )  # Field name made lowercase.
    iscreatorupdate = models.BooleanField(
        db_column="IsCreatOrUpdate"
    )  # Field name made lowercase.
    issucceeded = models.BooleanField(
        db_column="IsSucceeded"
    )  # Field name made lowercase.
    applyuserid = models.BigIntegerField(
        db_column="ApplyUserId"
    )  # Field name made lowercase.
    applyusername = models.TextField(
        db_column="ApplyUserName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    applydate = models.DateTimeField(
        db_column="ApplyDate", blank=True, null=True
    )  # Field name made lowercase.
    applyremarks = models.TextField(
        db_column="ApplyRemarks",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    clientipaddress = models.TextField(
        db_column="ClientIpAddress",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    productrepoid = models.ForeignKey(
        "Productrepoes",
        models.DO_NOTHING,
        db_column="ProductRepoId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    productcode = models.TextField(
        db_column="ProductCode", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    productname = models.TextField(
        db_column="ProductName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    warehousename = models.TextField(
        db_column="WarehouseName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    brandname = models.TextField(
        db_column="BrandName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ProductRepoUpdateLogs"


class Productrepoes(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    numberinrepo = models.IntegerField(
        db_column="NumberInRepo"
    )  # Field name made lowercase.
    avgcost = models.DecimalField(
        db_column="AvgCost", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    numberlocked = models.IntegerField(
        db_column="NumberLocked"
    )  # Field name made lowercase.
    productid = models.ForeignKey(
        "Products", models.DO_NOTHING, db_column="ProductId"
    )  # Field name made lowercase.
    warehouseid = models.ForeignKey(
        "Warehouses", models.DO_NOTHING, db_column="WarehouseId"
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ProductRepoes"


# 产品集详细信息，就是合并产品的
class Productsetdetails(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    productsetid = models.ForeignKey(
        "Productsets", models.DO_NOTHING, db_column="ProductSetId"
    )  # Field name made lowercase.
    productid = models.ForeignKey(
        "Products", models.DO_NOTHING, db_column="ProductId"
    )  # Field name made lowercase.
    numinset = models.IntegerField(db_column="NumInSet")  # Field name made lowercase.
    priceinset = models.DecimalField(
        db_column="PriceInSet", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ProductSetDetails"


# 产品集表
class Productsets(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    isenabled = models.BooleanField(db_column="IsEnabled")  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    productsetname = models.TextField(
        db_column="ProductSetName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    productsetcode = models.TextField(
        db_column="ProductSetCode",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    productsetbrand = models.TextField(
        db_column="ProductSetBrand",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ProductSets"


# 产品类别表
class Producttypes(models.Model):
    id = models.AutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    typename = models.TextField(
        db_column="TypeName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    # 产品品牌id
    typebrand = models.ForeignKey(
        Brands, models.DO_NOTHING, db_column="TypeBrand_Id", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ProductTypes"


# 产品表
class Products(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    productname = models.TextField(
        db_column="ProductName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    productcode = models.TextField(
        db_column="ProductCode", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    # 参考价格
    refprice = models.DecimalField(
        db_column="RefPrice", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    # 参考成本
    refcost = models.DecimalField(
        db_column="RefCost", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    # 产品类别id
    producttype = models.ForeignKey(
        Producttypes,
        models.DO_NOTHING,
        db_column="ProductType_Id",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    isremind = models.BooleanField(db_column="IsRemind")  # Field name made lowercase.
    minreponumber = models.IntegerField(
        db_column="MinRepoNumber"
    )  # Field name made lowercase.
    unit = models.TextField(
        db_column="Unit", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    sptoftprice = models.DecimalField(
        db_column="SPtoFTPrice", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    fttospprice = models.DecimalField(
        db_column="FTtoSPPrice", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    unifiedcost = models.DecimalField(
        db_column="UnifiedCost", max_digits=20, decimal_places=8
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Products"


# 采购订单详细信息表
class Purchaseorderdetails(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    purchaseorderid = models.ForeignKey(
        "Purchaseorders", models.DO_NOTHING, db_column="PurchaseOrderId"
    )  # Field name made lowercase.
    productid = models.ForeignKey(
        Products, models.DO_NOTHING, db_column="ProductId", blank=True, null=True
    )  # Field name made lowercase.
    # 产品购买数量
    ordernumber = models.IntegerField(
        db_column="OrderNumber"
    )  # Field name made lowercase.
    realprice = models.DecimalField(
        db_column="RealPrice", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    # 产品收到的数量
    numberreceived = models.IntegerField(
        db_column="NumberReceived"
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    # 要求发货日期
    requestedshipdate = models.DateTimeField(
        db_column="RequestedShipDate", blank=True, null=True
    )  # Field name made lowercase.
    paymentmode = models.IntegerField(
        db_column="PaymentMode"
    )  # Field name made lowercase.
    requireprepaydate = models.DateTimeField(
        db_column="RequirePrePayDate", blank=True, null=True
    )  # Field name made lowercase.
    prepayratio = models.IntegerField(
        db_column="PrePayRatio"
    )  # Field name made lowercase.
    requirefinalpaydate = models.DateTimeField(
        db_column="RequireFinalPayDate", blank=True, null=True
    )  # Field name made lowercase.
    isrequirereceiptbeforepay = models.BooleanField(
        db_column="IsRequireReceiptBeforePay", blank=True, null=True
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    numbertoreceive = models.IntegerField(
        db_column="NumberToReceive"
    )  # Field name made lowercase.
    foreigncurrencyprice = models.DecimalField(
        db_column="ForeignCurrencyPrice", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    foreigncurrencyname = models.TextField(
        db_column="ForeignCurrencyName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    foreigncurrencysymbol = models.TextField(
        db_column="ForeignCurrencySymbol",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    exchangerate = models.DecimalField(
        db_column="ExchangeRate", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    nonerepoproductname = models.TextField(
        db_column="NoneRepoProductName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    nonerepoproductcode = models.TextField(
        db_column="NoneRepoProductCode",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    nonerepoproducttype = models.TextField(
        db_column="NoneRepoProductType",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    nonerepoproductbrand = models.TextField(
        db_column="NoneRepoProductBrand",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    finishshipdate = models.DateTimeField(
        db_column="FinishShipDate", blank=True, null=True
    )  # Field name made lowercase.
    forcustomername = models.TextField(
        db_column="ForCustomerName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "PurchaseOrderDetails"


# 购买订单
class Purchaseorders(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    # 订单状态
    orderstatus = models.IntegerField(
        db_column="OrderStatus"
    )  # Field name made lowercase.
    # 接收状态
    receivestatus = models.IntegerField(
        db_column="ReceiveStatus"
    )  # Field name made lowercase.
    # 付款方式
    paymentmode = models.IntegerField(
        db_column="PaymentMode"
    )  # Field name made lowercase.
    ordercode = models.TextField(
        db_column="OrderCode", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    orderdate = models.DateTimeField(
        db_column="OrderDate"
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    requireprepaydate = models.DateTimeField(
        db_column="RequirePrePayDate", blank=True, null=True
    )  # Field name made lowercase.
    prepayratio = models.IntegerField(
        db_column="PrePayRatio"
    )  # Field name made lowercase.
    requirefinalpaydate = models.DateTimeField(
        db_column="RequireFinalPayDate", blank=True, null=True
    )  # Field name made lowercase.
    isrequirereceiptbeforepay = models.BooleanField(
        db_column="IsRequireReceiptBeforePay", blank=True, null=True
    )  # Field name made lowercase.
    contract01title = models.TextField(
        db_column="Contract01Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract01text = models.TextField(
        db_column="Contract01Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract02title = models.TextField(
        db_column="Contract02Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract02text = models.TextField(
        db_column="Contract02Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract03title = models.TextField(
        db_column="Contract03Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract03text = models.TextField(
        db_column="Contract03Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract04title = models.TextField(
        db_column="Contract04Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract04text = models.TextField(
        db_column="Contract04Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract05title = models.TextField(
        db_column="Contract05Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract05text = models.TextField(
        db_column="Contract05Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract06title = models.TextField(
        db_column="Contract06Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract06text = models.TextField(
        db_column="Contract06Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract07title = models.TextField(
        db_column="Contract07Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract07text = models.TextField(
        db_column="Contract07Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract08title = models.TextField(
        db_column="Contract08Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract08text = models.TextField(
        db_column="Contract08Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract09title = models.TextField(
        db_column="Contract09Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract09text = models.TextField(
        db_column="Contract09Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract10title = models.TextField(
        db_column="Contract10Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract10text = models.TextField(
        db_column="Contract10Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract11title = models.TextField(
        db_column="Contract11Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract11text = models.TextField(
        db_column="Contract11Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract12title = models.TextField(
        db_column="Contract12Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract12text = models.TextField(
        db_column="Contract12Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract13title = models.TextField(
        db_column="Contract13Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract13text = models.TextField(
        db_column="Contract13Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    # 采购订单供应商Id
    purchaseordersupplier = models.ForeignKey(
        "Suppliers",
        models.DO_NOTHING,
        db_column="PurchaseOrderSupplier_Id",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    # 订单id
    payid = models.ForeignKey(
        Pays, models.DO_NOTHING, db_column="PayId", blank=True, null=True
    )  # Field name made lowercase.
    istaxfreepay = models.BooleanField(
        db_column="IsTaxFreePay"
    )  # Field name made lowercase.
    ordercontractid = models.ForeignKey(
        Ordercontracts,
        models.DO_NOTHING,
        db_column="OrderContractId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    location = models.TextField(
        db_column="Location", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    mycompanyid = models.IntegerField(
        db_column="MyCompanyId", blank=True, null=True
    )  # Field name made lowercase.
    confirmeruserid = models.BigIntegerField(
        db_column="ConfirmerUserId", blank=True, null=True
    )  # Field name made lowercase.
    isforeigncurrency = models.BooleanField(
        db_column="IsForeignCurrency"
    )  # Field name made lowercase.
    foreigncurrencyname = models.TextField(
        db_column="ForeignCurrencyName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    foreigncurrencysymbol = models.TextField(
        db_column="ForeignCurrencySymbol",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    exchangerate = models.DecimalField(
        db_column="ExchangeRate", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    numberofpushship = models.IntegerField(
        db_column="NumberOfPushShip"
    )  # Field name made lowercase.
    numberofpushpay = models.IntegerField(
        db_column="NumberOfPushPay"
    )  # Field name made lowercase.
    finisheddate = models.DateTimeField(
        db_column="FinishedDate", blank=True, null=True
    )  # Field name made lowercase.
    newaddeddate = models.DateTimeField(
        db_column="NewAddedDate", blank=True, null=True
    )  # Field name made lowercase.
    obsoleteddate = models.DateTimeField(
        db_column="ObsoletedDate", blank=True, null=True
    )  # Field name made lowercase.
    isautocompleted = models.BooleanField(
        db_column="IsAutoCompleted"
    )  # Field name made lowercase.
    finishshipdate = models.DateTimeField(
        db_column="FinishShipDate", blank=True, null=True
    )  # Field name made lowercase.
    purchaseorderpricebydiscount = models.DecimalField(
        db_column="PurchaseOrderPriceByDiscount", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    customerordercode = models.TextField(
        db_column="CustomerOrderCode",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    isexchangeorder = models.BooleanField(
        db_column="IsExchangeOrder"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "PurchaseOrders"


class Receipts(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    receiptname = models.TextField(
        db_column="ReceiptName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    receipttitle = models.TextField(
        db_column="ReceiptTitle",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    receiptcontent = models.TextField(
        db_column="ReceiptContent",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    amount = models.DecimalField(
        db_column="Amount", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    receiptdate = models.DateTimeField(
        db_column="ReceiptDate", blank=True, null=True
    )  # Field name made lowercase.
    receiptclass = models.IntegerField(
        db_column="ReceiptClass"
    )  # Field name made lowercase.
    receiptuserid = models.BigIntegerField(
        db_column="ReceiptUserId", blank=True, null=True
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    billid = models.ForeignKey(
        Bills, models.DO_NOTHING, db_column="BillId", blank=True, null=True
    )  # Field name made lowercase.
    payid = models.ForeignKey(
        Pays, models.DO_NOTHING, db_column="PayId", blank=True, null=True
    )  # Field name made lowercase.
    issendout = models.BooleanField(db_column="IsSendOut")  # Field name made lowercase.
    directshipdetailid = models.ForeignKey(
        Directshipdetails,
        models.DO_NOTHING,
        db_column="DirectShipDetailId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    mycompanyid = models.ForeignKey(
        Mycompanies, models.DO_NOTHING, db_column="MyCompanyId", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Receipts"


class Receiveconfirms(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    shiplistid = models.ForeignKey(
        "Shiplists", models.DO_NOTHING, db_column="ShipListId"
    )  # Field name made lowercase.
    mycompanyid = models.IntegerField(
        db_column="MyCompanyId"
    )  # Field name made lowercase.
    uploaduserid = models.IntegerField(
        db_column="UploadUserId"
    )  # Field name made lowercase.
    downloadurl = models.TextField(
        db_column="DownloadUrl", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    filename = models.TextField(
        db_column="FileName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    receivedtime = models.DateTimeField(
        db_column="ReceivedTime", blank=True, null=True
    )  # Field name made lowercase.
    uploadtime = models.DateTimeField(
        db_column="UploadTime", blank=True, null=True
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ReceiveConfirms"


# 收到记录表
class Receivedrecords(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    productid = models.BigIntegerField(
        db_column="ProductId", blank=True, null=True
    )  # Field name made lowercase.
    brandname = models.TextField(
        db_column="BrandName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    typename = models.TextField(
        db_column="TypeName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    productname = models.TextField(
        db_column="ProductName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    productcode = models.TextField(
        db_column="ProductCode", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    receivednumber = models.IntegerField(
        db_column="ReceivedNumber"
    )  # Field name made lowercase.
    receiveddate = models.DateTimeField(
        db_column="ReceivedDate", blank=True, null=True
    )  # Field name made lowercase.
    receiveduserid = models.BigIntegerField(
        db_column="ReceivedUserId", blank=True, null=True
    )  # Field name made lowercase.
    inrepodetailid = models.ForeignKey(
        Inrepodetails,
        models.DO_NOTHING,
        db_column="InRepoDetailId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    purchaseproductid = models.BigIntegerField(
        db_column="PurchaseProductId", blank=True, null=True
    )  # Field name made lowercase.
    purchasebrandname = models.TextField(
        db_column="PurchaseBrandName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    purchasetypename = models.TextField(
        db_column="PurchaseTypeName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    purchaseproductname = models.TextField(
        db_column="PurchaseProductName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    purchaseproductcode = models.TextField(
        db_column="PurchaseProductCode",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ReceivedRecords"


class Saleorderdetails(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    saleorderid = models.ForeignKey(
        "Saleorders", models.DO_NOTHING, db_column="SaleOrderId"
    )  # Field name made lowercase.
    productid = models.ForeignKey(
        Products, models.DO_NOTHING, db_column="ProductId", blank=True, null=True
    )  # Field name made lowercase.
    ordernumber = models.IntegerField(
        db_column="OrderNumber"
    )  # Field name made lowercase.
    realprice = models.DecimalField(
        db_column="RealPrice", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    realcost = models.DecimalField(
        db_column="RealCost", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    numbertoship = models.IntegerField(
        db_column="NumberToShip"
    )  # Field name made lowercase.
    numbershiped = models.IntegerField(
        db_column="NumberShiped"
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    requestedshipdate = models.DateTimeField(
        db_column="RequestedShipDate", blank=True, null=True
    )  # Field name made lowercase.
    paymentmode = models.IntegerField(
        db_column="PaymentMode"
    )  # Field name made lowercase.
    requireprepaydate = models.DateTimeField(
        db_column="RequirePrePayDate", blank=True, null=True
    )  # Field name made lowercase.
    prepayratio = models.IntegerField(
        db_column="PrePayRatio"
    )  # Field name made lowercase.
    requirefinalpaydate = models.DateTimeField(
        db_column="RequireFinalPayDate", blank=True, null=True
    )  # Field name made lowercase.
    isrequirereceiptbeforepay = models.BooleanField(
        db_column="IsRequireReceiptBeforePay", blank=True, null=True
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    isinproductset = models.BooleanField(
        db_column="IsInProductSet"
    )  # Field name made lowercase.
    productsetname = models.TextField(
        db_column="ProductSetName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    productsetcode = models.TextField(
        db_column="ProductSetCode",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    numofproductset = models.IntegerField(
        db_column="NumOfProductSet"
    )  # Field name made lowercase.
    remarksofproductset = models.TextField(
        db_column="RemarksOfProductSet",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    productsetgroup = models.TextField(
        db_column="ProductSetGroup",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    productsetrealprice = models.DecimalField(
        db_column="ProductSetRealPrice", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    productsetbrand = models.TextField(
        db_column="ProductSetBrand",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    nonerepoproductname = models.TextField(
        db_column="NoneRepoProductName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    nonerepoproductcode = models.TextField(
        db_column="NoneRepoProductCode",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    nonerepoproducttype = models.TextField(
        db_column="NoneRepoProductType",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    nonerepoproductbrand = models.TextField(
        db_column="NoneRepoProductBrand",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    foreigncurrencyprice = models.DecimalField(
        db_column="ForeignCurrencyPrice", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    foreigncurrencyname = models.TextField(
        db_column="ForeignCurrencyName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    foreigncurrencysymbol = models.TextField(
        db_column="ForeignCurrencySymbol",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    exchangerate = models.DecimalField(
        db_column="ExchangeRate", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    costestimate = models.DecimalField(
        db_column="CostEstimate", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    finishshipdate = models.DateTimeField(
        db_column="FinishShipDate", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "SaleOrderDetails"


class Saleorders(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    ordercode = models.TextField(
        db_column="OrderCode", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    orderdate = models.DateTimeField(
        db_column="OrderDate"
    )  # Field name made lowercase.
    shipdate = models.DateTimeField(
        db_column="ShipDate", blank=True, null=True
    )  # Field name made lowercase.
    paymentdate = models.DateTimeField(
        db_column="PaymentDate", blank=True, null=True
    )  # Field name made lowercase.
    orderstatus = models.IntegerField(
        db_column="OrderStatus"
    )  # Field name made lowercase.
    paymentmode = models.IntegerField(
        db_column="PaymentMode"
    )  # Field name made lowercase.
    shipstatus = models.IntegerField(
        db_column="ShipStatus"
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    saleordercustomerid = models.ForeignKey(
        Customers, models.DO_NOTHING, db_column="SaleOrderCustomerId"
    )  # Field name made lowercase.
    requireprepaydate = models.DateTimeField(
        db_column="RequirePrePayDate", blank=True, null=True
    )  # Field name made lowercase.
    prepayratio = models.IntegerField(
        db_column="PrePayRatio"
    )  # Field name made lowercase.
    requirefinalpaydate = models.DateTimeField(
        db_column="RequireFinalPayDate", blank=True, null=True
    )  # Field name made lowercase.
    isrequirereceiptbeforepay = models.BooleanField(
        db_column="IsRequireReceiptBeforePay", blank=True, null=True
    )  # Field name made lowercase.
    contract01title = models.TextField(
        db_column="Contract01Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract01text = models.TextField(
        db_column="Contract01Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract02title = models.TextField(
        db_column="Contract02Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract02text = models.TextField(
        db_column="Contract02Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract03title = models.TextField(
        db_column="Contract03Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract03text = models.TextField(
        db_column="Contract03Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract04title = models.TextField(
        db_column="Contract04Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract04text = models.TextField(
        db_column="Contract04Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract05title = models.TextField(
        db_column="Contract05Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract05text = models.TextField(
        db_column="Contract05Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract06title = models.TextField(
        db_column="Contract06Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract06text = models.TextField(
        db_column="Contract06Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract07title = models.TextField(
        db_column="Contract07Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract07text = models.TextField(
        db_column="Contract07Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract08title = models.TextField(
        db_column="Contract08Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract08text = models.TextField(
        db_column="Contract08Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract09title = models.TextField(
        db_column="Contract09Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract09text = models.TextField(
        db_column="Contract09Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract10title = models.TextField(
        db_column="Contract10Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract10text = models.TextField(
        db_column="Contract10Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract11title = models.TextField(
        db_column="Contract11Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract11text = models.TextField(
        db_column="Contract11Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract12title = models.TextField(
        db_column="Contract12Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract12text = models.TextField(
        db_column="Contract12Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract13title = models.TextField(
        db_column="Contract13Title",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contract13text = models.TextField(
        db_column="Contract13Text",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    billid = models.ForeignKey(
        Bills, models.DO_NOTHING, db_column="BillId", blank=True, null=True
    )  # Field name made lowercase.
    istaxfreepay = models.BooleanField(
        db_column="IsTaxFreePay"
    )  # Field name made lowercase.
    profit = models.DecimalField(
        db_column="Profit", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    ordercontractid = models.ForeignKey(
        Ordercontracts,
        models.DO_NOTHING,
        db_column="OrderContractId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    location = models.TextField(
        db_column="Location", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    mycompanyid = models.IntegerField(
        db_column="MyCompanyId", blank=True, null=True
    )  # Field name made lowercase.
    confirmeruserid = models.BigIntegerField(
        db_column="ConfirmerUserId", blank=True, null=True
    )  # Field name made lowercase.
    expressrequired = models.TextField(
        db_column="ExpressRequired",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    isforeigncurrency = models.BooleanField(
        db_column="IsForeignCurrency"
    )  # Field name made lowercase.
    foreigncurrencyname = models.TextField(
        db_column="ForeignCurrencyName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    foreigncurrencysymbol = models.TextField(
        db_column="ForeignCurrencySymbol",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    exchangerate = models.DecimalField(
        db_column="ExchangeRate", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    numberofpushship = models.IntegerField(
        db_column="NumberOfPushShip"
    )  # Field name made lowercase.
    numberofpushpay = models.IntegerField(
        db_column="NumberOfPushPay"
    )  # Field name made lowercase.
    finisheddate = models.DateTimeField(
        db_column="FinishedDate", blank=True, null=True
    )  # Field name made lowercase.
    newaddeddate = models.DateTimeField(
        db_column="NewAddedDate", blank=True, null=True
    )  # Field name made lowercase.
    obsoleteddate = models.DateTimeField(
        db_column="ObsoletedDate", blank=True, null=True
    )  # Field name made lowercase.
    saleorderpricebydiscount = models.DecimalField(
        db_column="SaleOrderPriceByDiscount", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    isautocompleted = models.BooleanField(
        db_column="IsAutoCompleted"
    )  # Field name made lowercase.
    profitestimate = models.DecimalField(
        db_column="ProfitEstimate", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    productreceiverid = models.ForeignKey(
        Customerreceivers,
        models.DO_NOTHING,
        db_column="ProductReceiverId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    receiptreceiverid = models.ForeignKey(
        Customerreceivers,
        models.DO_NOTHING,
        db_column="ReceiptReceiverId",
        related_name="saleorders_receiptreceiverid_set",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    finishshipdate = models.DateTimeField(
        db_column="FinishShipDate", blank=True, null=True
    )  # Field name made lowercase.
    customerordercode = models.TextField(
        db_column="CustomerOrderCode",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    isexchangeorder = models.BooleanField(
        db_column="IsExchangeOrder"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "SaleOrders"


class Saleplanitems(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    plancode = models.TextField(
        db_column="PlanCode", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    productid = models.ForeignKey(
        Products, models.DO_NOTHING, db_column="ProductId"
    )  # Field name made lowercase.
    customerproductcode = models.TextField(
        db_column="CustomerProductCode",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    plancustomerid = models.ForeignKey(
        Customers, models.DO_NOTHING, db_column="PlanCustomerId"
    )  # Field name made lowercase.
    mycompanyid = models.ForeignKey(
        Mycompanies, models.DO_NOTHING, db_column="MyCompanyId"
    )  # Field name made lowercase.
    plansalenumber = models.IntegerField(
        db_column="PlanSaleNumber"
    )  # Field name made lowercase.
    plansaleprice = models.DecimalField(
        db_column="PlanSalePrice", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    isforeigncurrency = models.BooleanField(
        db_column="IsForeignCurrency"
    )  # Field name made lowercase.
    plandate = models.DateTimeField(
        db_column="PlanDate", blank=True, null=True
    )  # Field name made lowercase.
    needdate = models.DateTimeField(
        db_column="NeedDate", blank=True, null=True
    )  # Field name made lowercase.
    planstatus = models.IntegerField(
        db_column="PlanStatus"
    )  # Field name made lowercase.
    isinproductset = models.BooleanField(
        db_column="IsInProductSet"
    )  # Field name made lowercase.
    productsetgroup = models.TextField(
        db_column="ProductSetGroup",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    productsetrealprice = models.DecimalField(
        db_column="ProductSetRealPrice", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    productsetname = models.TextField(
        db_column="ProductSetName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    productsetbrand = models.TextField(
        db_column="ProductSetBrand",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    productsetcode = models.TextField(
        db_column="ProductSetCode",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    numofproductset = models.IntegerField(
        db_column="NumOfProductSet"
    )  # Field name made lowercase.
    saleorderdetailid = models.ForeignKey(
        Saleorderdetails,
        models.DO_NOTHING,
        db_column="SaleOrderDetailId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    purchaseorderdetailid = models.ForeignKey(
        Purchaseorderdetails,
        models.DO_NOTHING,
        db_column="PurchaseOrderDetailId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "SalePlanItems"


class Shiplists(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    shiplistcode = models.TextField(
        db_column="ShipListCode", db_collation="Chinese_PRC_CI_AS"
    )  # Field name made lowercase.
    iscompleted = models.BooleanField(
        db_column="IsCompleted", blank=True, null=True
    )  # Field name made lowercase.
    customername = models.TextField(
        db_column="CustomerName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    address = models.TextField(
        db_column="Address", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    contactperson = models.TextField(
        db_column="ContactPerson",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contactphone = models.TextField(
        db_column="ContactPhone",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mobile = models.TextField(
        db_column="Mobile", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    expressname = models.TextField(
        db_column="ExpressName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    expressorderid = models.TextField(
        db_column="ExpressOrderId",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    shipaddress = models.TextField(
        db_column="ShipAddress", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    receiver = models.TextField(
        db_column="Receiver", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    shipdate = models.DateTimeField(
        db_column="ShipDate", blank=True, null=True
    )  # Field name made lowercase.
    shipper = models.TextField(
        db_column="Shipper", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    shiptocompany = models.TextField(
        db_column="ShipToCompany",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    shiptocompanyphone = models.TextField(
        db_column="ShipToCompanyPhone",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    receiverphone = models.TextField(
        db_column="ReceiverPhone",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mycompanyid = models.IntegerField(
        db_column="MyCompanyId"
    )  # Field name made lowercase.
    issigned = models.BooleanField(
        db_column="IsSigned", blank=True, null=True
    )  # Field name made lowercase.
    signer = models.TextField(
        db_column="Signer", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    signdate = models.DateTimeField(
        db_column="SignDate", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ShipLists"


class Shippingorders(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    weight = models.FloatField(db_column="Weight")  # Field name made lowercase.
    carrier = models.TextField(
        db_column="Carrier", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    shippingpricermb = models.DecimalField(
        db_column="ShippingPriceRMB", max_digits=20, decimal_places=8
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    shipmode = models.IntegerField(db_column="ShipMode")  # Field name made lowercase.
    shiptype = models.IntegerField(db_column="ShipType")  # Field name made lowercase.
    shipdir = models.IntegerField(db_column="ShipDir")  # Field name made lowercase.
    orderdate = models.DateTimeField(
        db_column="OrderDate", blank=True, null=True
    )  # Field name made lowercase.
    mycompanyid = models.IntegerField(
        db_column="MyCompanyId", blank=True, null=True
    )  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    chinashippingordername = models.TextField(
        db_column="ChinaShippingOrderName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    foreignshippingordercode = models.TextField(
        db_column="ForeignShippingOrderCode",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    estimatedarrivedate = models.DateTimeField(
        db_column="EstimatedArriveDate", blank=True, null=True
    )  # Field name made lowercase.
    importreportcode = models.TextField(
        db_column="ImportReportCode",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    importreportfeermb = models.DecimalField(
        db_column="ImportReportFeeRMB",
        max_digits=20,
        decimal_places=8,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    importtaxrmb = models.DecimalField(
        db_column="ImportTaxRMB", max_digits=20, decimal_places=8, blank=True, null=True
    )  # Field name made lowercase.
    valueaddedtaxrmb = models.DecimalField(
        db_column="ValueAddedTaxRMB",
        max_digits=20,
        decimal_places=8,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    exchangerate = models.DecimalField(
        db_column="ExchangeRate", max_digits=20, decimal_places=8, blank=True, null=True
    )  # Field name made lowercase.
    discriminator = models.CharField(
        db_column="Discriminator", max_length=128, db_collation="Chinese_PRC_CI_AS"
    )  # Field name made lowercase.
    payid = models.ForeignKey(
        Pays, models.DO_NOTHING, db_column="PayId", blank=True, null=True
    )  # Field name made lowercase.
    orderstatus = models.IntegerField(
        db_column="OrderStatus"
    )  # Field name made lowercase.
    shippingordercode = models.TextField(
        db_column="ShippingOrderCode",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    confirmeruserid = models.BigIntegerField(
        db_column="ConfirmerUserId", blank=True, null=True
    )  # Field name made lowercase.
    confirmdate = models.DateTimeField(
        db_column="ConfirmDate", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ShippingOrders"


class Suppliercontracts(models.Model):
    id = models.BigAutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    purchaseorderid = models.ForeignKey(
        Purchaseorders, models.DO_NOTHING, db_column="PurchaseOrderId"
    )  # Field name made lowercase.
    mycompanyid = models.IntegerField(
        db_column="MyCompanyId"
    )  # Field name made lowercase.
    uploaduserid = models.IntegerField(
        db_column="UploadUserId"
    )  # Field name made lowercase.
    downloadurl = models.TextField(
        db_column="DownloadUrl", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    filename = models.TextField(
        db_column="FileName", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    contracttime = models.DateTimeField(
        db_column="ContractTime", blank=True, null=True
    )  # Field name made lowercase.
    uploadtime = models.DateTimeField(
        db_column="UploadTime", blank=True, null=True
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "SupplierContracts"


# 供货方表
class Suppliers(models.Model):
    id = models.AutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    name = models.TextField(
        db_column="Name", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    address = models.TextField(
        db_column="Address", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    contactperson = models.TextField(
        db_column="ContactPerson",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    contactphone = models.TextField(
        db_column="ContactPhone",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    fax = models.TextField(
        db_column="Fax", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    email = models.TextField(
        db_column="Email", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    accountbank = models.TextField(
        db_column="AccountBank", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    accountid = models.TextField(
        db_column="AccountId", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    texid = models.TextField(
        db_column="TexId", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    province = models.TextField(
        db_column="Province", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    mobile = models.TextField(
        db_column="Mobile", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    ismycompany = models.BooleanField(
        db_column="IsMyCompany"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Suppliers"


class Warehouses(models.Model):
    id = models.AutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    warehousename = models.TextField(
        db_column="WarehouseName",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    warehouseadmin = models.TextField(
        db_column="WarehouseAdmin",
        db_collation="Chinese_PRC_CI_AS",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    remarks = models.TextField(
        db_column="Remarks", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p1str = models.TextField(
        db_column="P1str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p2str = models.TextField(
        db_column="P2str", db_collation="Chinese_PRC_CI_AS", blank=True, null=True
    )  # Field name made lowercase.
    p3double = models.FloatField(db_column="P3double")  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column="IsDeleted")  # Field name made lowercase.
    deleteruserid = models.BigIntegerField(
        db_column="DeleterUserId", blank=True, null=True
    )  # Field name made lowercase.
    deletiontime = models.DateTimeField(
        db_column="DeletionTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(
        db_column="LastModificationTime", blank=True, null=True
    )  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(
        db_column="LastModifierUserId", blank=True, null=True
    )  # Field name made lowercase.
    creationtime = models.DateTimeField(
        db_column="CreationTime"
    )  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(
        db_column="CreatorUserId", blank=True, null=True
    )  # Field name made lowercase.
    mycompanyid = models.ForeignKey(
        Mycompanies, models.DO_NOTHING, db_column="MyCompanyId", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Warehouses"


class Migrationhistory(models.Model):
    migrationid = models.CharField(
        db_column="MigrationId",
        primary_key=True,
        max_length=150,
        db_collation="Chinese_PRC_CI_AS",
    )  # Field name made lowercase. The composite primary key (MigrationId, ContextKey) found, that is not supported. The first column is selected.
    contextkey = models.CharField(
        db_column="ContextKey", max_length=300, db_collation="Chinese_PRC_CI_AS"
    )  # Field name made lowercase.
    model = models.BinaryField(db_column="Model")  # Field name made lowercase.
    productversion = models.CharField(
        db_column="ProductVersion", max_length=32, db_collation="Chinese_PRC_CI_AS"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "__MigrationHistory"
        unique_together = (("migrationid", "contextkey"),)


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation="Chinese_PRC_CI_AS")
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sysdiagrams"
        unique_together = (("principal_id", "name"),)
