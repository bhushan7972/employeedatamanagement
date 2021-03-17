
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class DepartmentMaster(models.Model):
    DepartmentMaster = models.UUIDField()
    is_DepartmentMaster = models.BooleanField(default=False)
    Department=models.CharField(max_length=100)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    CreatedBy= models.UUIDField()
    ModifiedBy= models.UUIDField()
    ModifiedDate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.DepartmentMaster

class DeductionMaster(models.Model):
    DeductionID = models.UUIDField()
    Deduction   = models.CharField(max_length=100)
    IsConsider  = models.BooleanField(default=False)
    SortNo      = models.IntegerField()
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy   = models.UUIDField()
    ModifiedBy  = models.UUIDField()
    ModifiedDate = models.DateTimeField()
    IsActive    = models.BooleanField(default=False)


class CurrencyMaster(models.Model):
    CurrencyID = models.IntegerField()
    CurrencyCode = models.CharField(max_length=10)
    CurrencySymbol = models.CharField(max_length=50)
    IsActive = models.BooleanField(default=False)

    def __str__(self):
        return self.CurrencyID



class CompanyMaster(models.Model):
    CompanyID = models.UUIDField()
    CompanyName = models.CharField(max_length=100)
    CompanyLogo = models.CharField(max_length=100)
    EmailAddress = models.CharField(max_length=100)
    CountryId   = models.UUIDField()
    StateId     = models.CharField()
    City       = models.CharField()
    Address    = models.CharField(max_length=100)
    MobileNo  = models.CharField(max_length=100)
    PhoneNo   = models.CharField(max_length=100)
    HotlineNo = models.CharField(max_length=100)
    FaxNo    = models.CharField(max_length=100)
    Website  = models.CharField(max_length=100)
    ModifiedBy = models.UUIDField()
    ModifiedDate = models.DateTimeField()
    IsActive  = models.BooleanField(default=False)
    UserEmailId = models.CharField(max_length=100)
    UserEmailPassword = models.CharField(max_length=100)
    IsEnableSSL = models.BooleanField(default=False)
    SMTPHost = models.CharField(max_length=100)
    SMTPPort = models.IntegerField()
    FromEmailId = models.CharField(max_length=100)
    ReceiveEmailIds = models.CharField(max_length=100)

class AllowanceMaster(models.Model):
    AllowanceID = models.UUIDField(primary_key=True)
    Allowance = models.CharField(max_length=50)
    IsConsider= models.BooleanField(default=False)
    SortNo = models.IntegerField()
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.UUIDField()
    ModifiedBy = models.UUIDField()
    ModifiedDate = models.DateTimeField(auto_now_add=True)
    IsActive = models.BooleanField(default=False)
    Percentage = models.FloatField()

    def __str__(self):
        return self.AllowanceID

class EmployeeAttendanceDevice(models.Model):
    EmployeeAttendanceID = models.UUIDField(primary_key=True)
    EmployeeId = models.UUIDField()
    DeviceId = models.UUIDField()
    EnrollNo = models.CharField(max_length=100)
    AttendanceDate = models.DateField()
    AttendanceDateTime = models.DateTimeField()
    PunchTime = models.BinaryField()
    VerifyMethod = models.CharField(max_length=500, blank=False, null=False)
    PunchMethod  = models.CharField(max_length=500 )
    CreatedDate = models.DateTimeField()
    ModifiedDate = models.DateTimeField()
    CreatedBy = models.UUIDField()
    ModifiedBy = models.UUIDField()
    IsActive =  models.BooleanField(default = False)
    def __str__(self):
        s = str(self.EmployeeAttendanceID)
        return (s)

class EmployeeGradeMaster(models.Model):
    EmployeeGradeID = models.UUIDField(primary_key=True)
    EmployeeGrade = models.CharField(max_length=50)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.UUIDField()
    ModifiedBy = models.UUIDField()
    ModifiedDate = models.DateTimeField(auto_now=True)
    IsActive = models.BooleanField(default=False)
    def __str__(self):
        return self.EmployeeGradeID

class EmployeeDeviceMap(models.Model):

    EmployeeDeviceID = models.UUIDField(primary_key=True)
    EmployeeId = models.UUIDField()
    DeviceId = models.UUIDField()
    EnrollNo = models.CharField(max_length=50)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    IsActive = models.BooleanField(default=False)

    def __str__(self):
        s = str(self.EmployeeDeviceID)
        return (s)

class EmployeePaidDeductionMap(models.Model):
    EmployeePaidDeductionMapID = models.UUIDField(primary_key=True)
    EmployeePaidSalaryId = models.UUIDField()
    EmployeeId = models.UUIDField()
    DeductionId = models.UUIDField()
    Amount = models.DecimalField()
    PaidAmount = models.DecimalField()
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.UUIDField()
    ModifiedBy = models.UUIDField()
    ModifiedDate =  models.DateTimeField(auto_now=True)
    IsActive = models.BooleanField(default=False)
    def __str__(self):
        return self.EmployeePaidDeductionMapID


class EmployeePaidAllowanceMap(models.Model):
    EmployeePaidAllowanceMapID = models.UUIDField(primary_key=True)
    EmployeePaidSalaryId = models.UUIDField()
    EmployeeId = models.UUIDField()
    AllowanceId = models.UUIDField()
    Amount = models.DecimalField()
    PaidAmount = models.DecimalField()
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.UUIDField()
    ModifiedBy = models.UUIDField()
    ModifiedDate = models.DateTimeField(auto_now=True)
    IsActive = models.BooleanField(default=False)

    def __str__(self):
        return self.EmployeePaidAllowanceMapID

class ShiftMaster(models.Model):

    ShiftID = models.UUIDField(primary_key=True)
    Shift = models.CharField(max_length=50)
    FromTime = models.CharField(max_length=20)
    ToTime = models.CharField(max_length=20)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.UUIDField()
    ModifiedBy = models.UUIDField()
    ModifiedDate = models.DateTimeField(auto_now_add=True)
    IsActive = models.BooleanField(default=False)

    def __str__(self):
        s = str(self.ShiftID)
        return (s)


class ModuleMaster(models.Model):
    ModuleID = models.UUIDField(primary_key=True)
    EnumName  = models.CharField(max_length=500 )
    Name   = models.CharField(max_length=500 )
    ParentId  = models.UUIDField()
    TreeLevel = models.IntegerField(max_length=500)
    IsActive = models.BooleanField(default = False)
    SortOrder = models.IntegerField(max_length=500)
    def __str__(self):
        s = str(self.ModuleID)
        return (s)

class  EmployeeLeaveCategory(models.Model):
    EmployeeLeaveCategoryMapID = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    EmployeeId = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    LeaveCategoryId = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    StartDate =models.DateTimeField(auto_now_add=True)
    EndDate = models.DateTimeField(auto_now_add=True)
    TotalDay = models.DecimalField(max_length=10)
    IsFirstHalfDay  = models.BooleanField(default=False)
    IsLastHalfDay  = models.BooleanField(default=False)
    Reason =models.CharField(max_length=1000)
    Comments=models.CharField(max_length=1000)
    ApplyDate = models.DateTimeField(auto_now_add=True)
    ApprovedBy =models.CharField(max_length=150)
    ApproveDate = models.DateTimeField(auto_now_add=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy =  models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    ModifiedBy =  models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    ModifiedDate = models.DateTimeField(auto_now_add=True)
    IsActive = models.BooleanField(default=False)
    IsApprove = models.BooleanField(default=False)

    def __str__(self):
        return self.EmployeeID
class EmployeeTypeMaster(models.Model):
    EmployeeTypeID   = models.UUIDField()
    EmployeeType     = models.CharField(max_length=100)
    NoOfLeavePerMonth = models.DecimalField()
    CreatedDate  =   models.DateTimeField(auto_now=True)
    CreatedBy    =   models.UUIDField()
    ModifiedBy   =   models.UUIDField()
    ModifiedDate =  models.DateTimeField(auto_now=True)
    IsActive    = models.BooleanField(default=False)

class FinancialYearMaster(models.Model):
    FinancialYearID = models.UUIDField()
    Year            = models.IntegerField()
    FinancialYear   = models.CharField(max_length=100)
    CreatedDate     = models.DateTimeField(auto_now=True)
    CreatedBy       = models.UUIDField()
    ModifiedBy      = models.UUIDField()
    ModifiedDate    = models.DateTimeField(auto_now=True)
    IsActive        = models.BooleanField(default=False)
    StartMonth      = models.IntegerField()
    EndMonth        = models.IntegerField()

class HolidayMaster(models.Model):
    HolidayID  = models.UUIDField()
    Title       =models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    StartDate   = models.DateTimeField()
    EndDate     = models.DateTimeField()
    CreatedDate = models.DateTimeField(auto_now=True)
    CreatedBy   = models.UUIDField()
    ModifiedBy  = models.UUIDField()
    ModifiedDate = models.DateTimeField(auto_now=True)
    IsActive    = models.BooleanField(default=False)


class StateMaster(models.Model):
    StateID = models.UUIDField(primary_key=True)
    CountryId = models.UUIDField()
    StateName = models.CharField(max_length=40)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    IsActive = models.BooleanField(default=False)

    def __str__(self):
        s = str(self.StateID)
        return (s)


class InvoiceMaster(models.Model):
    InvoiceID=models.IntegerField(max_length=10)
    InvoiceNo=models.IntegerField(max_length=10)
    InvoiceDate = models.DateTimeField(auto_now_add=True)
    CurrencyId = models.IntegerField(max_length=10)
    PartyName  = models.CharField(max_length=100)
    PartyAddress  = models.CharField(max_length=1000)
    Description  = models.CharField(max_length=200)
    SubTotal = models.DecimalField(max_length=12)
    ServiceTax = models.DecimalField(max_length=12)
    GrandTotal = models.DecimalField(max_length=12)
    SubTotalINR = models.DecimalField(max_length=12)
    ServiceTaxINR = models.DecimalField(max_length=12)
    GrandTotalINR = models.DecimalField(max_length=12)
    IsFixed = models.BooleanField(default=False)
    IsPaid = models.BooleanField(default=False)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy  = models.UUIDField()
    ModifiedBy  = models.UUIDField()
    ModifiedDate = models.DateTimeField(auto_now_add=True)
    IsActive = models.BooleanField(default=False)

    def __str__(self):
        return self.InvoiceID

class EmployeeMaster(models.Model):
    EmployeeID= models.UUIDField()
    EmployeeTypeId= models.UUIDField()
    EmployeeGradeId= models.UUIDField()
    DepartmentId= models.UUIDField()
    DesignationId= models.UUIDField()
    ShiftId= models.UUIDField()
    FirstName=models.CharField(max_length=100)
    MiddleName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    BirthDate=models.DateTimeField(blank=True)
    FatherName=models.CharField(max_length=100)
    Gender= models.BooleanField(default=False)
    MaratialStatus= models.CharField(max_length=20)
    Cast=models.CharField(max_length=20)
    PhotoName=models.CharField(max_length=20)
    CountryId= models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    StateId = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    City=models.CharField(max_length=50,blank=False,null=False)
    Address=models.CharField(max_length=1000,blank=False,null=False)
    PinCode=models.CharField(max_length=10,blank=False,null=False)
    MobileNo=models.CharField(max_length=15,blank=False,null=False)
    PhoneNo=models.CharField(max_length=15,blank=False,null=False)
    JoinDate=models.DateTimeField()
    EmployeeNo=models.IntegerField(max_length=10)
    PFNo=models.CharField(max_length=50,blank=False,null=False)
    Email=models.CharField(max_length=200,blank=False,null=False)
    BankName=models.CharField(max_length=50,blank=False,null=False)
    BranchName=models.CharField(max_length=50,blank=False,null=False)
    AccountName=models.CharField(max_length=150,blank=False,null=False)
    AccountNo=models.CharField(max_length=50,blank=False,null=False)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    CreatedBy= models.UUIDField()
    ModifiedBy= models.UUIDField()
    ModifiedDate=models.DateTimeField(auto_now_add=True)
    IsActive=models.BooleanField(default=False)
    IsLeave=models.BooleanField(default=False)
    LeaveDate=models.DateTimeField()
    LeaveDescription=models.CharField(min_length=20,max_length=50,blank=False,null=False)
    Previlage=models.CharField(min_length=40,max_length=100,blank=False,null=False)
    Password=models.CharField(min_length=40,max_length=100,blank=False,null=False)
    FaceTemplate=models.CharField(min_length=40,max_length=100,blank=False,null=False)
    IsHavingFace= models.BooleanField(default=False)
    FaceLength=models.IntegerField(max_length=10)
    FingureTemplate=models.CharField(min_length=40,max_length=100,blank=False,null=False)
    finger_template_data_bw=models.BinaryField()
    finger_template_data_tft=models.BinaryField()
    finger_template_data_tft1=models.BinaryField()
    finger_template_data_tft2=models.BinaryField()
    finger_template_data_tft3=models.BinaryField()
    finger_template_data_tft4=models.BinaryField()
    finger_template_data_tft5=models.BinaryField()
    finger_template_data_tft6=models.BinaryField()
    finger_template_data_tft7=models.BinaryField()
    finger_template_data_tft8=models.BinaryField()
    finger_template_data_tft9=models.BinaryField()
    finger_template_data_bw1=models.BinaryField()
    finger_template_data_bw2=models.BinaryField()
    finger_template_data_bw3=models.BinaryField()
    finger_template_data_bw4=models.BinaryField()
    finger_template_data_bw5=models.BinaryField()
    finger_template_data_bw6=models.BinaryField()
    finger_template_data_bw7=models.BinaryField()
    finger_template_data_bw8=models.BinaryField()
    finger_template_data_bw9=models.BinaryField()
    is_having_fingureprint= models.BooleanField(default=False)
    IsSend= models.BooleanField(default=False)
    FaceTemplateData=models.CharField(max_length=50)

    def __str__(self):
        return self.EmployeeID




class InvoiceDetail(models.Model):
    InvoiceDetailID  = models.IntegerField(max_length=10)
    InvoiceId = models.IntegerField(max_length=10)
    ItemDescription = models.CharField(max_length=200)
    ItemDate = models.DateTimeField(auto_now_add=True)
    Hours = models.DecimalField(max_length=10)
    HourRate= models.DecimalField(max_length=10)
    Amount= models.DecimalField(max_length=10)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy =  models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    ModifiedBy =  models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    ModifiedDate  = models.DateTimeField(auto_now_add=True)
    IsActive  = models.BooleanField(default=False)

    def __str__(self):
        return self.InvoiceDetailID



class UserModuleMap(models.Model):
    UserModuleMapID =  models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    UserId =  models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    ModuleId =  models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)

    def __str__(self):
        return self.UserModuleMapID


class EmployeePaidLoan(models.Model):
    EmployeePaidLoanMapID  =  models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    EmployeeLoanMapId =  models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    PaidAmount =models.IntegerField(max_length=10)
    PaidDate   = models.DateTimeField(auto_now_add=True)
    CreatedDate   = models.DateTimeField(auto_now_add=True)
    CreatedBy  =  models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    ModifiedBy  =  models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    ModifiedDate  = models.DateTimeField(auto_now_add=True)
    IsActive  = models.BooleanField(default=False)
    Month = models.CharField(max_length=15)
    Year=models.IntegerField(max_length=10)

    def __str__(self):
        return self.EmployeePaidLoanMapID




class LeaveCategoryMaster(models.Model):
    LeaveCategoryID = models.UUIDField(primary_key=True)
    LeaveCategory = models.CharField(max_length=500 )
    CreatedDate = models.DateTimeField()
    CreatedBy = models.UUIDField()
    ModifiedBy = models.UUIDField()
    ModifiedDate = models.DateTimeField()
    IsActive = models.BooleanField(default = False)
    def __str__(self):
        s = str(self.LeaveCategoryID)
        return (s)
class EmployeeWorkingDay(models.Model):
    EmployeeWorkingDayMapID = models.UUIDField(primary_key=True)
    EmployeeId = models.UUIDField()
    DayName = models.CharField(max_length=500 )
    CreatedDate = models.DateTimeField()
    CreatedBy = models.UUIDField()
    ModifiedBy = models.UUIDField()
    ModifiedDate = models.UUIDField()
    IsActive = models.BooleanField(default = False)
    def __str__(self):
        s = str(self.EmployeeWorkingDayMapID)
        return (s)

class EmployeeSalary(models.Model):
    EmployeeSalaryID = models.UUIDField(primary_key=True)
    EmployeeId =  models.UUIDField()
    Basic = models.DecimalField()
    TotalEarning =  models.DecimalField()
    TotalDeduction =  models.DecimalField()
    TotalSalary =  models.DecimalField()
    CreatedDate = models.DateTimeField()
    CreatedBy =  models.UUIDField()
    ModifiedBy =  models.UUIDField()
    ModifiedDate =  models.DateTimeField()
    IsActive = models.BooleanField(default = False)
    def __str__(self):
        s = str(self.EmployeeSalaryID)
        return (s)

class sysdiagrams(models.Model):
    name = models.CharField(max_length=500 )
    principal_id = models.IntegerField()
    diagram_id =  models.IntegerField()
    version = models.IntegerField()
    definition = models.CharField()
    def __str__(self):
        s = str(self.principal_id)
        return (s)



class DesignationMaster(models.Model):
    DesignationID = models.UUIDField(primary_key=True)
    Designation = models.CharField(max_length=100)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.UUIDField()
    ModifiedBy = models.UUIDField()
    ModifiedDate = models.DateTimeField(auto_now=True)
    IsActive = models.BooleanField(default=False)

    def __str__(self):
        return self.DesignationID


class UserMaster(models.Model):
    UserID      = models.UUIDField()
    RoleId      = models.UUIDField()
    EmployeeId  = models.UUIDField()
    Username    = models.CharField(max_length=100)
    Password    = models.CharField(max_length= 50)
    LastLogin   = models.DateTimeField(auto_now=True)
    CreatedDate = models.DateTimeField(auto_now=True)
    CreatedBy   = models.UUIDField()
    ModifiedBy  = models.UUIDField()
    ModifiedDate = models.DateTimeField(auto_now=True)
    IsActive     = models.BooleanField(default=False)

class EmployeeAllowanceMap(models.Model):
    EmployeeAllowanceMapID  = models.UUIDField()
    EmployeeId              = models.UUIDField()
    AllowanceId             = models.UUIDField()
    Amount                  = models.DecimalField()
    CreatedDate             = models.DateTimeField(auto_now= True)
    CreatedBy               = models.UUIDField()
    ModifiedBy              = models.UUIDField()
    ModifiedDate            = models.DateTimeField(auto_now=True)
    IsActive                = models.BooleanField(default=False)

class EmployeeAttachment(models.Model):
    EmployeeAttachmentMapID = models.UUIDField()
    EmployeeId              = models.UUIDField()
    Name                    = models.CharField(max_length=100)
    Description             = models.CharField(max_length=100)
    AttachmentName          = models.CharField(max_length=100)
    CreatedDate             = models.DateTimeField(auto_now=True)
    CreatedBy               = models.UUIDField()
    ModifiedBy              = models.UUIDField()
    ModifiedDate            = models.DateTimeField(auto_now=True)
    IsActive                = models.BooleanField(default=False)

class  EmployeeDeductionMap(models.Model):
    EmployeeDeductionMapID = models.UUIDField()
    EmployeeId              =models.UUIDField()
    DeductionId             =models.UUIDField()
    Amount                = models.DecimalField()
    CreatedDate           = models.UUIDField()
    CreatedBy             = models.UUIDField()
    ModifiedBy            = models.UUIDField()
    ModifiedDate          = models.DateTimeField(auto_now=True)
    IsActive              = models.BooleanField(default=False)





class DeviceMaster(models.Model):

    DeviceID = models.UUIDField(primary_key=True)
    DeviceName = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    DeviceCode = models.CharField(max_length=40)
    PhoneNo = models.CharField(max_length=40)
    Port = models.IntegerField()
    IPAddress = models.CharField(max_length=40)
    CreatedBy = models.UUIDField()
    CreatedDate = models.DateTimeField(auto_now_add=True)
    ModifiedBy = models.UUIDField()
    ModifiedDate = models.DateTimeField(auto_now_add=True)
    IsActive = models.BooleanField(default=False)

    def __str__(self):
        s = str(self.DeviceName)
        return (s)

class DesignationMaster(models.Model):
    DesignationID = models.UUIDField(primary_key=True)
    Designation = models.CharField(max_length=100)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.UUIDField()
    ModifiedBy = models.UUIDField()
    ModifiedDate = models.DateTimeField(auto_now=True)
    IsActive = models.BooleanField(default=False)

class RoleMaster(models.Model):
    RoleID = models.UUIDField(primary_key=True)
    RoleName = models.CharField(max_length=500 )
    IsActive =  models.BooleanField(default = False)
    def __str__(self):
        s = str(self. RoleID )
        return (s)