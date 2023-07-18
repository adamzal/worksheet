from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class IndirectWeeklyRow(models.Model):

    class Day(models.TextChoices):
        SUNDAY = '1', _('Sunday')
        MONDAY = '2', _('Monday')
        TUESDAY = '3', _('Tuesday')
        WEDNESDAY = '4', _('Wednesday')
        THURSDAY = '5', _('Thursday')
        FRIDAY = '6', _('Friday')
        SATURDAY = '7', _('Saturday')

    class Activity(models.TextChoices):
        INTAKE_FLT_DUTIES = '01', _('FLT duties')
        INTAKE_YARD_FLT = '02', _('Yard FLT')
        INTAKE_DIC_DUTIES = '03', _('DIC duties')
        INTAKE_UNLOCATED_CONTRACT_INDIRECT = '04', _('Unlocatedcontract indirect')
        INTAKE_DUMP_CHUTE_PENALTY_BOX = '05', _('Dump chute penalty box')
        INTAKE_PALLETISER = '06', _('Palletiser')
        INTAKE_CUSHION_MANUFACTURING_CHECKING = '07', _('Cushion manufacturing checking')
        INTAKE_LOC_MAN_DUTIES = '08', _('Loc man duties')
        INTAKE_OTHER = '09', _('Other') 

        RETAIL_FLT_DUTIES = '10', _('FLT duties')
        RETAIL_LOC_MAN_DUTIES = '11', _('Loc man duties')
        RETAIL_PALLET_PREP_MEZZ = '12', _('Pallet prep - mezz')
        RETAIL_PALLET_COLLAR_REPAIR = '13', _('Pallet collar repair')
        RETAIL_PALLET_SWEEP_P1_COLLECTION = '14', _('Pallet sweep / P1 collection')
        RETAIL_DROPS_AND_SWEEPS = '15', _('Drops and sweeps')
        RETAIL_VNA_D_WALK_DESPATCH = '16', _('VNA / D walk despatch')
        RETAIL_OTHER = '17', _('Other')

        ONLINE_FLT_DUTIES = '18', _('FLT duties')
        ONLINE_NO_STOCKS_MLS_PRINT_SERVICES = '19', _('No stocks, Mls & print services')
        ONLINE_LOC_MAN_DUTIES = '20', _('Loc man duties')
        ONLINE_MOVING_STOCK_BACK_WALL = '21', _('Moving stock - back wall')
        ONLINE_MOVING_STOCK_VNA = '22', _('Moving stock - VNA')
        ONLINE_BEAUTY_LOC_MAN_DUTIES = '23', _('Beauty loc man duties')
        ONLINE_BEAUTY_BOX_MAKER = '24', _('Beauty box maker')
        ONLINE_BEAUTY_SERVICE_HAND = '25', _('Beauty service hand')
        ONLINE_OTHER = '26', _('Other')

        CUSHIONS_FLT_DUTIES = '27', _('FLT duties')
        CUSHIONS_SERVICE_HAND = '28', _('Service hand')
        CUSHIONS_OTHER = '29', _('Other')

    class Reason(models.TextChoices):
        UNPAID_BREAK = '99', _('Unpaid break')


    week = models.ForeignKey(Week, on_delete=models.CASCADE)

    day = models.CharField(max_length=1, choices=Day.choices)
    activity = models.CharField(max_length=2, choices=Activity.choices)
    time_from = models.DateTimeField()
    time_to = models.DateTimeField()
    minutes = models.PositiveIntegerField()
    reason = models.CharField(max_length=2, choices=Reason.choices)
