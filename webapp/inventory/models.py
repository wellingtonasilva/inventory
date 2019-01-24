from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    question_test = models.CharField('Question text', max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_test


class DeviceStatus(models.Model):
    status = models.CharField("Status", max_length=30)

    def __str__(self):
        return self.status


class AndroidVersion(models.Model):
    description = models.CharField('Description', max_length=30)

    def __str__(self):
        return self.description


class SkuType(models.Model):
    description = models.CharField('Description', max_length=30)

    def __str__(self):
        return self.description


class Team(models.Model):
    description = models.CharField('Description', max_length=60)

    def __str__(self):
        return self.description


class Build(models.Model):
    description = models.CharField('Description', max_length=150)

    def __str__(self):
        return self.description


class Carrier(models.Model):
    description = models.CharField('Description', max_length=150)

    def __str__(self):
        return self.description


class HardwareType(models.Model):
    description = models.CharField('Description', max_length=150)

    def __str__(self):
        return self.description


class AccessoryType(models.Model):
    description = models.CharField('Description', max_length=150)

    def __str__(self):
        return self.description


class Device(models.Model):
    deviceId = models.IntegerField('Device ID')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    user_responsible = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_usable = models.BooleanField("Is Usable")
    public_name = models.CharField("Public Name", max_length=150)
    internal_name = models.CharField("Internal Name", max_length=30)
    build = models.ForeignKey(Build, on_delete=models.CASCADE, null=True)
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE, null=True)
    sku_type = models.ForeignKey(SkuType, models.CASCADE, null=True)
    serial_number = models.CharField("Serial Number", max_length=30)
    ss_sd = models.CharField('SS/SD', max_length=2)
    imei1 = models.CharField('IMEI 1', max_length=20)
    imei2 = models.CharField('IMEI 2', max_length=20)
    hardware_type = models.ForeignKey(HardwareType, on_delete=models.CASCADE, null=True)
    is_secure = models.BooleanField('Is Secure')
    cid = models.SmallIntegerField('CID')
    android_version = models.ForeignKey(AndroidVersion, on_delete=models.CASCADE, null=True)
    ram = models.CharField('RAM', max_length=30)
    rom = models.CharField('ROM', max_length=30)
    camera_frontal = models.CharField('Camera Frontal', max_length=30)
    camera_rear = models.CharField('Camera Transeira', max_length=30)
    is_nfc = models.BooleanField('NFC?')
    is_fingerprint = models.BooleanField('Fingerprint?')
    device_situacao = models.ForeignKey(DeviceStatus, on_delete=models.CASCADE, null=True)
    part_number = models.CharField('Part Number', max_length=20)
    chipset = models.CharField('Chipset', max_length=20)
    comment = models.CharField('Comments', max_length=400)
    danfe = models.CharField('DANFE', max_length=10)
    is_avaliable = models.BooleanField('Is Available')
    last_update = models.DateTimeField('Last Update', auto_now=True)
    is_doogfooding = models.BooleanField('DoogFooding?')

    def __str__(self):
        return self.serial_number


class Accessory(models.Model):
    type = models.ForeignKey(AccessoryType, on_delete=models.CASCADE, null=True)
    description = models.CharField('Description', max_length=154)
    serial_number = models.CharField('Serial Number', max_length=20)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    part_number = models.CharField('Part Number', max_length=30)
    hardware_version = models.CharField('Hardware Version', max_length=20)
    data_added = models.DateField('Date Added', auto_now=True)
    location = models.CharField('Current Location', max_length=20)
    invoice = models.CharField('Invoice', max_length=20)
    is_usable_testing = models.BooleanField('Is Usable Testing')
    comments = models.CharField('Comments', max_length=400)

    def __str__(self):
        return self.description


class SimCard(models.Model):
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE, null=True)
    zone = models.CharField('Zone', max_length=20)
    phone_number = models.CharField('Number', max_length=20)
    pin1 = models.CharField('PIN', max_length=4)
    pin2 = models.CharField('PIN2', max_length=4)
    puk1 = models.CharField('PUK', max_length=10)
    puk2 = models.CharField('PUK2', max_length=10)
    iccid = models.CharField('ICCID', max_length=30)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comments = models.CharField('Comments', max_length=400)
    is_account = models.BooleanField('Account?')
    login = models.CharField('Login', max_length=254)
    cloud_password = models.CharField('Cloud Password', max_length=254)
    is_caller_name_id = models.BooleanField('Caller Name ID?')
    is_vvm = models.BooleanField('VVM?')
    is_volte = models.BooleanField('VOLTE?')
    is_vowifi = models.BooleanField('VOWIFI')
    is_hotspot = models.BooleanField('Hotspot')
    vvm_password = models.CharField('VVM Password', max_length=254)
    serial_number = models.CharField('Serial Number', max_length=30)

    def __str__(self):
        return self.phone_number


class Danfe(models.Model):
    numero_nota_fiscal = models.CharField('No. NF', max_length=10)
    data_emissao = models.DateField('Data Emissão')
    data_entrada = models.DateField('Data Entrada', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.numero_nota_fiscal


class DanfeItem(models.Model):
    danfe = models.ForeignKey(Danfe, on_delete=models.CASCADE)
    description = models.CharField('Product Description', max_length=254)
    ncm = models.CharField('NCM', max_length=20)
    cst = models.SmallIntegerField('CST')
    cfop = models.SmallIntegerField('CFOP')
    qty = models.FloatField('Quantity')

    def __str__(self):
        return self.description

