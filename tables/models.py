# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, Integer, String, text
from sqlalchemy.dialects.mysql import CHAR, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class C301(Base):
    __tablename__ = 'c301'
    __table_args__ = {'comment': '电芯活化工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(DateTime, index=True, comment='活化开始时间')
    P002 = Column(DateTime, comment='活化结束时间')
    P003 = Column(VARCHAR(24), comment='活化时间/min\\r\\n')
    P004 = Column(VARCHAR(24), comment='托盘号')
    P005 = Column(VARCHAR(24), comment='库位号')
    P006 = Column(Integer, comment='位置号')
    P007 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class C302(Base):
    __tablename__ = 'c302'
    __table_args__ = {'comment': '电芯化成工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(VARCHAR(24), comment='设备号')
    P002 = Column(VARCHAR(24), comment='治具号')
    P003 = Column(Integer, comment='通道号')
    P004 = Column(Integer, comment='化成工步号')
    P005 = Column(VARCHAR(24), comment='化成工步类型')
    P006 = Column(Float(15), comment='化成工步起始电压')
    P007 = Column(Float(15), comment='化成工步结束电压')
    P008 = Column(Float(15), comment='化成工步结束电流')
    P009 = Column(Float(15), comment='化成工步结束容量')
    P010 = Column(Float(15), comment='化成工步结束压力')
    P011 = Column(Float(15), comment='化成工步结束温度')
    P012 = Column(VARCHAR(255), comment='化成工步时间')
    P013 = Column(DateTime, index=True, comment='化成工步开始时间')
    P014 = Column(DateTime, comment='化成工步结束时间')
    P015 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class C303(Base):
    __tablename__ = 'c303'
    __table_args__ = {'comment': '电芯电压测试1工序'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(VARCHAR(24), comment='托盘条码')
    P002 = Column(Integer, comment='位置')
    P003 = Column(Float(15), comment='电压')
    P004 = Column(Integer, comment='测试次数')
    P005 = Column(DateTime, index=True, comment='测试时间')
    P006 = Column(VARCHAR(24), comment='保留字段')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='批次号')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class C304(Base):
    __tablename__ = 'c304'
    __table_args__ = {'comment': '电芯老化工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(DateTime, index=True, comment='老化开始时间')
    P002 = Column(DateTime, comment='老化结束时间')
    P003 = Column(VARCHAR(24), comment='老化时间/min\\r\\n')
    P004 = Column(VARCHAR(24), comment='托盘号')
    P005 = Column(VARCHAR(24), comment='库位号')
    P006 = Column(Integer, comment='位置号')
    P007 = Column(VARCHAR(24), comment='保留字段')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='批次号')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class C305(Base):
    __tablename__ = 'c305'
    __table_args__ = {'comment': '电芯电压测试2表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(VARCHAR(24), comment='托盘条码')
    P002 = Column(Integer, comment='位置')
    P003 = Column(Float(15), comment='电压')
    P004 = Column(Integer, comment='测试次数')
    P005 = Column(DateTime, index=True, comment='测试时间')
    P006 = Column(Float(15), comment='老化压降')
    P007 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'1'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class C306(Base):
    __tablename__ = 'c306'
    __table_args__ = {'comment': '电芯degas工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(VARCHAR(24), comment='进站料框码')
    P002 = Column(Float(15), comment='注液前称重\\r\\n')
    P003 = Column(Float(15), comment='注液量')
    P004 = Column(Float(15), comment='注液后称重\\r\\n')
    P005 = Column(Float(15), comment='Degas前称重重量')
    P006 = Column(Integer, comment='电芯上料框位置')
    P007 = Column(Float(15), comment='封印厚度1\\r\\n')
    P008 = Column(Float(15), comment='封印厚度2')
    P009 = Column(Float(15), comment='封印厚度3')
    P010 = Column(Float(15), comment='封印厚度4')
    P011 = Column(Float(15), comment='封印厚度5')
    P012 = Column(Float(15), comment='封印厚度6')
    P013 = Column(Float(15), comment='正极侧边电压值')
    P014 = Column(Float(15), comment='正极侧边电阻值')
    P015 = Column(Float(15), comment='负极侧边电压值')
    P016 = Column(Float(15), comment='负极侧边电阻值')
    P017 = Column(VARCHAR(24), comment='腔体号')
    P018 = Column(Float(15), comment='腔体左封头温度')
    P019 = Column(Float(15), comment='腔体右封头温度')
    P020 = Column(Float(15), comment='腔体夹板压力')
    P021 = Column(Float(15), comment='腔体封头压力')
    P022 = Column(Float(15), comment='腔体封印时间\\r\\n')
    P023 = Column(Float(15), comment='腔体封装时真空值')
    P024 = Column(Float(15), comment='腔体保压时间')
    P025 = Column(VARCHAR(24), comment='精封封头编号')
    P026 = Column(Float(15), comment='精封左封头温度')
    P027 = Column(Float(15), comment='精封右封头温度')
    P028 = Column(Float(15), comment='精封封头压力')
    P029 = Column(Float(15), comment='精封封印时间')
    P030 = Column(VARCHAR(24), comment='出站料框码')
    P031 = Column(Integer, comment='出料框内电芯位置')
    P032 = Column(Float(15), comment='Degas后称重重量')
    P033 = Column(Float(15), comment='电芯保液量')
    P034 = Column(Float(15), comment='电芯失液量')
    P035 = Column(DateTime, index=True, comment='下料时间')
    P036 = Column(VARCHAR(24), comment='设备编号')
    P037 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class C307(Base):
    __tablename__ = 'c307'
    __table_args__ = {'comment': '电芯分容工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(VARCHAR(24), comment='设备号')
    P002 = Column(VARCHAR(24), comment='通道号')
    P003 = Column(Integer, comment='分容工步号\\r\\n')
    P004 = Column(VARCHAR(24), comment='分容工步类型')
    P005 = Column(Float(15), comment='分容工步开始电压')
    P006 = Column(Float(15), comment='分容工步结束电压')
    P007 = Column(Float(15), comment='分容工步结束电流')
    P008 = Column(Float(15), comment='分容工步结束容量')
    P009 = Column(VARCHAR(24), comment='分容工步时间')
    P010 = Column(Float(15), comment='分容工步结束温度')
    P011 = Column(DateTime, comment='分容工步开始时间')
    P012 = Column(DateTime, comment='分容工步结束时间')
    P013 = Column(Float(15), comment='分容容量')
    P014 = Column(VARCHAR(24), comment='下料托盘条码')
    P015 = Column(DateTime, index=True, comment='上料时间')
    P016 = Column(DateTime, comment='下料时间')
    P017 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class C308(Base):
    __tablename__ = 'c308'
    __table_args__ = {'comment': '电芯静置1工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(DateTime, index=True, comment='静置开始时间')
    P002 = Column(DateTime, comment='静置结束时间')
    P003 = Column(VARCHAR(24), comment='静置时间')
    P004 = Column(Float(15), comment='静置库位温度')
    P005 = Column(VARCHAR(24), comment='托盘号')
    P006 = Column(String(24), comment='库位号')
    P007 = Column(Integer, comment='位置')
    P008 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class C309(Base):
    __tablename__ = 'c309'
    __table_args__ = {'comment': '电芯OCV1工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(String(24), comment='托盘条码')
    P002 = Column(Float(15), comment='电压')
    P003 = Column(Float(15), comment='内阻')
    P004 = Column(VARCHAR(24), comment='测试结果')
    P005 = Column(DateTime, index=True, comment='测试时间')
    P006 = Column(Integer, comment='位置号')
    P007 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class C310(Base):
    __tablename__ = 'c310'
    __table_args__ = {'comment': '电芯静置2工序'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(DateTime, index=True, comment='静置开始时间')
    P002 = Column(DateTime, comment='静置结束时间')
    P003 = Column(VARCHAR(24), comment='静置时间')
    P004 = Column(Float(15), comment='静置库位温度')
    P005 = Column(VARCHAR(24), comment='托盘号')
    P006 = Column(VARCHAR(24), comment='库位号')
    P007 = Column(Integer, comment='位置')
    P008 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'0'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class C311(Base):
    __tablename__ = 'c311'
    __table_args__ = {'comment': '电芯OCV2工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(VARCHAR(24), comment='托盘条码')
    P002 = Column(Float(15), comment='电压')
    P003 = Column(Float(15), comment='内阻')
    P004 = Column(VARCHAR(24), comment='测试结果')
    P005 = Column(DateTime, index=True, comment='测试时间')
    P006 = Column(Integer, comment='位置号')
    P007 = Column(Float(15), comment='K1')
    P008 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class C312(Base):
    __tablename__ = 'c312'
    __table_args__ = {'comment': '电芯静置3工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(DateTime, index=True, comment='静置开始时间')
    P002 = Column(DateTime, comment='静置结束时间')
    P003 = Column(VARCHAR(24), comment='静置时间')
    P004 = Column(Float(15), comment='静置库位温度')
    P005 = Column(VARCHAR(24), comment='托盘号')
    P006 = Column(VARCHAR(24), comment='库位号')
    P007 = Column(Integer, comment='位置')
    P008 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class C313(Base):
    __tablename__ = 'c313'
    __table_args__ = {'comment': '电芯OCV3工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(VARCHAR(24), comment='托盘条码')
    P002 = Column(Float(15), comment='电压')
    P003 = Column(Float(15), comment='内阻')
    P004 = Column(VARCHAR(24), comment='测试结果')
    P005 = Column(DateTime, index=True, comment='测试时间')
    P006 = Column(Integer, comment='位置号')
    P007 = Column(Float(15), comment='K2')
    P008 = Column(Float(15), comment='K3')
    P009 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class C314(Base):
    __tablename__ = 'c314'
    __table_args__ = {'comment': '电芯DCIR工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(Float(15), comment='电流大小')
    P002 = Column(Float(15), comment='放电时间')
    P003 = Column(VARCHAR(24), comment='托盘条码')
    P004 = Column(DateTime, index=True, comment='测试时间')
    P005 = Column(Float(15), comment='直流内阻值')
    P006 = Column(Float(15), comment='放电前电压')
    P007 = Column(Float(15), comment='放电后电压')
    P008 = Column(VARCHAR(24), comment='测试结果')
    P009 = Column(VARCHAR(24), comment='设备编号')
    P010 = Column(Integer, comment='测试次数')
    P011 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'0'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class C315(Base):
    __tablename__ = 'c315'
    __table_args__ = {'comment': '电芯分选工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(VARCHAR(24), comment='托盘条码')
    P002 = Column(Integer, comment='位置')
    P003 = Column(Float(15), comment='电芯厚度')
    P004 = Column(Float(15), comment='正极边电压')
    P005 = Column(Float(15), comment='负极边电压')
    P006 = Column(VARCHAR(24), comment='电芯厚度测试工位号')
    P007 = Column(VARCHAR(24), comment='绝缘电压测试工位号')
    P008 = Column(VARCHAR(24), comment='二折工位号')
    P009 = Column(Float(15), comment='预热温度')
    P010 = Column(Float(15), comment='预烫时间')
    P011 = Column(VARCHAR(24), comment='档位号')
    P012 = Column(VARCHAR(24), comment='栈板条码')
    P013 = Column(DateTime, index=True, comment='分选时间')
    P014 = Column(Integer, comment='分选次数')
    P015 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class D301(Base):
    __tablename__ = 'd301'
    __table_args__ = {'comment': '电芯活化工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(DateTime, index=True, comment='活化开始时间')
    P002 = Column(DateTime, comment='活化结束时间')
    P003 = Column(VARCHAR(24), comment='活化时间/min\\r\\n')
    P004 = Column(VARCHAR(24), comment='托盘号')
    P005 = Column(VARCHAR(24), comment='库位号')
    P006 = Column(Integer, comment='位置号')
    P007 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class D302(Base):
    __tablename__ = 'd302'
    __table_args__ = {'comment': '电芯化成工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(VARCHAR(24), comment='设备号')
    P002 = Column(VARCHAR(24), comment='治具号')
    P003 = Column(Integer, comment='通道号')
    P004 = Column(Integer, comment='化成工步号')
    P005 = Column(VARCHAR(24), comment='化成工步类型')
    P006 = Column(Float(15), comment='化成工步起始电压')
    P007 = Column(Float(15), comment='化成工步结束电压')
    P008 = Column(Float(15), comment='化成工步结束电流')
    P009 = Column(Float(15), comment='化成工步结束容量')
    P010 = Column(Float(15), comment='化成工步结束压力')
    P011 = Column(Float(15), comment='化成工步结束温度')
    P012 = Column(VARCHAR(255), comment='化成工步时间')
    P013 = Column(DateTime, index=True, comment='化成工步开始时间')
    P014 = Column(DateTime, comment='化成工步结束时间')
    P015 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class D303(Base):
    __tablename__ = 'd303'
    __table_args__ = {'comment': '电芯电压测试1工序'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(VARCHAR(24), comment='托盘条码')
    P002 = Column(Integer, comment='位置')
    P003 = Column(Float(15), comment='电压')
    P004 = Column(Integer, comment='测试次数')
    P005 = Column(DateTime, index=True, comment='测试时间')
    P006 = Column(VARCHAR(24), comment='保留字段')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='批次号')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class D304(Base):
    __tablename__ = 'd304'
    __table_args__ = {'comment': '电芯老化工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(DateTime, index=True, comment='老化开始时间')
    P002 = Column(DateTime, comment='老化结束时间')
    P003 = Column(VARCHAR(24), comment='老化时间/min\\r\\n')
    P004 = Column(VARCHAR(24), comment='托盘号')
    P005 = Column(VARCHAR(24), comment='库位号')
    P006 = Column(Integer, comment='位置号')
    P007 = Column(VARCHAR(24), comment='保留字段')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='批次号')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class D305(Base):
    __tablename__ = 'd305'
    __table_args__ = {'comment': '电芯电压测试2表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(VARCHAR(24), comment='托盘条码')
    P002 = Column(Integer, comment='位置')
    P003 = Column(Float(15), comment='电压')
    P004 = Column(Integer, comment='测试次数')
    P005 = Column(DateTime, index=True, comment='测试时间')
    P006 = Column(Float(15), comment='老化压降')
    P007 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'1'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class D306(Base):
    __tablename__ = 'd306'
    __table_args__ = {'comment': '电芯degas工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(VARCHAR(24), comment='进站料框码')
    P002 = Column(Float(15), comment='注液前称重\\r\\n')
    P003 = Column(Float(15), comment='注液量')
    P004 = Column(Float(15), comment='注液后称重\\r\\n')
    P005 = Column(Float(15), comment='Degas前称重重量')
    P006 = Column(Integer, comment='电芯上料框位置')
    P007 = Column(Float(15), comment='封印厚度1\\r\\n')
    P008 = Column(Float(15), comment='封印厚度2')
    P009 = Column(Float(15), comment='封印厚度3')
    P010 = Column(Float(15), comment='封印厚度4')
    P011 = Column(Float(15), comment='封印厚度5')
    P012 = Column(Float(15), comment='封印厚度6')
    P013 = Column(Float(15), comment='正极侧边电压值')
    P014 = Column(Float(15), comment='正极侧边电阻值')
    P015 = Column(Float(15), comment='负极侧边电压值')
    P016 = Column(Float(15), comment='负极侧边电阻值')
    P017 = Column(VARCHAR(24), comment='腔体号')
    P018 = Column(Float(15), comment='腔体左封头温度')
    P019 = Column(Float(15), comment='腔体右封头温度')
    P020 = Column(Float(15), comment='腔体夹板压力')
    P021 = Column(Float(15), comment='腔体封头压力')
    P022 = Column(Float(15), comment='腔体封印时间\\r\\n')
    P023 = Column(Float(15), comment='腔体封装时真空值')
    P024 = Column(Float(15), comment='腔体保压时间')
    P025 = Column(VARCHAR(24), comment='精封封头编号')
    P026 = Column(Float(15), comment='精封左封头温度')
    P027 = Column(Float(15), comment='精封右封头温度')
    P028 = Column(Float(15), comment='精封封头压力')
    P029 = Column(Float(15), comment='精封封印时间')
    P030 = Column(VARCHAR(24), comment='出站料框码')
    P031 = Column(Integer, comment='出料框内电芯位置')
    P032 = Column(Float(15), comment='Degas后称重重量')
    P033 = Column(Float(15), comment='电芯保液量')
    P034 = Column(Float(15), comment='电芯失液量')
    P035 = Column(DateTime, index=True, comment='下料时间')
    P036 = Column(VARCHAR(24), comment='设备编号')
    P037 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class D307(Base):
    __tablename__ = 'd307'
    __table_args__ = {'comment': '电芯分容工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(VARCHAR(24), comment='设备号')
    P002 = Column(VARCHAR(24), comment='通道号')
    P003 = Column(Integer, comment='分容工步号\\r\\n')
    P004 = Column(VARCHAR(24), comment='分容工步类型')
    P005 = Column(Float(15), comment='分容工步开始电压')
    P006 = Column(Float(15), comment='分容工步结束电压')
    P007 = Column(Float(15), comment='分容工步结束电流')
    P008 = Column(Float(15), comment='分容工步结束容量')
    P009 = Column(VARCHAR(24), comment='分容工步时间')
    P010 = Column(Float(15), comment='分容工步结束温度')
    P011 = Column(DateTime, comment='分容工步开始时间')
    P012 = Column(DateTime, comment='分容工步结束时间')
    P013 = Column(Float(15), comment='分容容量')
    P014 = Column(VARCHAR(24), comment='下料托盘条码')
    P015 = Column(DateTime, index=True, comment='上料时间')
    P016 = Column(DateTime, comment='下料时间')
    P017 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class D308(Base):
    __tablename__ = 'd308'
    __table_args__ = {'comment': '电芯静置1工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(DateTime, index=True, comment='静置开始时间')
    P002 = Column(DateTime, comment='静置结束时间')
    P003 = Column(VARCHAR(24), comment='静置时间')
    P004 = Column(Float(15), comment='静置库位温度')
    P005 = Column(VARCHAR(24), comment='托盘号')
    P006 = Column(String(24), comment='库位号')
    P007 = Column(Integer, comment='位置')
    P008 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class D309(Base):
    __tablename__ = 'd309'
    __table_args__ = {'comment': '电芯OCV1工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(String(24), comment='托盘条码')
    P002 = Column(Float(15), comment='电压')
    P003 = Column(Float(15), comment='内阻')
    P004 = Column(VARCHAR(24), comment='测试结果')
    P005 = Column(DateTime, index=True, comment='测试时间')
    P006 = Column(Integer, comment='位置号')
    P007 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class D310(Base):
    __tablename__ = 'd310'
    __table_args__ = {'comment': '电芯静置2工序'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(DateTime, index=True, comment='静置开始时间')
    P002 = Column(DateTime, comment='静置结束时间')
    P003 = Column(VARCHAR(24), comment='静置时间')
    P004 = Column(Float(15), comment='静置库位温度')
    P005 = Column(VARCHAR(24), comment='托盘号')
    P006 = Column(VARCHAR(24), comment='库位号')
    P007 = Column(Integer, comment='位置')
    P008 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'0'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class D311(Base):
    __tablename__ = 'd311'
    __table_args__ = {'comment': '电芯OCV2工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(VARCHAR(24), comment='托盘条码')
    P002 = Column(Float(15), comment='电压')
    P003 = Column(Float(15), comment='内阻')
    P004 = Column(VARCHAR(24), comment='测试结果')
    P005 = Column(DateTime, index=True, comment='测试时间')
    P006 = Column(Integer, comment='位置号')
    P007 = Column(Float(15), comment='K1')
    P008 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class D312(Base):
    __tablename__ = 'd312'
    __table_args__ = {'comment': '电芯静置3工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(DateTime, index=True, comment='静置开始时间')
    P002 = Column(DateTime, comment='静置结束时间')
    P003 = Column(VARCHAR(24), comment='静置时间')
    P004 = Column(Float(15), comment='静置库位温度')
    P005 = Column(VARCHAR(24), comment='托盘号')
    P006 = Column(VARCHAR(24), comment='库位号')
    P007 = Column(Integer, comment='位置')
    P008 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class D313(Base):
    __tablename__ = 'd313'
    __table_args__ = {'comment': '电芯OCV3工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(VARCHAR(24), comment='托盘条码')
    P002 = Column(Float(15), comment='电压')
    P003 = Column(Float(15), comment='内阻')
    P004 = Column(VARCHAR(24), comment='测试结果')
    P005 = Column(DateTime, index=True, comment='测试时间')
    P006 = Column(Integer, comment='位置号')
    P007 = Column(Float(15), comment='K2')
    P008 = Column(Float(15), comment='K3')
    P009 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class D314(Base):
    __tablename__ = 'd314'
    __table_args__ = {'comment': '电芯DCIR工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(Float(15), comment='电流大小')
    P002 = Column(Float(15), comment='放电时间')
    P003 = Column(VARCHAR(24), comment='托盘条码')
    P004 = Column(DateTime, index=True, comment='测试时间')
    P005 = Column(Float(15), comment='直流内阻值')
    P006 = Column(Float(15), comment='放电前电压')
    P007 = Column(Float(15), comment='放电后电压')
    P008 = Column(VARCHAR(24), comment='测试结果')
    P009 = Column(VARCHAR(24), comment='设备编号')
    P010 = Column(Integer, comment='测试次数')
    P011 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'0'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class D315(Base):
    __tablename__ = 'd315'
    __table_args__ = {'comment': '电芯分选工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(VARCHAR(24), comment='托盘条码')
    P002 = Column(Integer, comment='位置')
    P003 = Column(Float(15), comment='电芯厚度')
    P004 = Column(Float(15), comment='正极边电压')
    P005 = Column(Float(15), comment='负极边电压')
    P006 = Column(VARCHAR(24), comment='电芯厚度测试工位号')
    P007 = Column(VARCHAR(24), comment='绝缘电压测试工位号')
    P008 = Column(VARCHAR(24), comment='二折工位号')
    P009 = Column(Float(15), comment='预热温度')
    P010 = Column(Float(15), comment='预烫时间')
    P011 = Column(VARCHAR(24), comment='档位号')
    P012 = Column(VARCHAR(24), comment='栈板条码')
    P013 = Column(DateTime, index=True, comment='分选时间')
    P014 = Column(Integer, comment='分选次数')
    P015 = Column(VARCHAR(24), comment='批次号')
    mark = Column(VARCHAR(255), server_default=text("'正常电芯'"), comment='标记')
    status = Column(CHAR(1), server_default=text("'0'"), comment='电芯状态（0表示良品，1表示不良品，2表示报废品）')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除字段（0表示正常，1表示删除）')


class DataCode(Base):
    __tablename__ = 'data_code'
    __table_args__ = {'comment': '参数编码设置表'}

    id = Column(BigInteger, primary_key=True)
    operation_number = Column(VARCHAR(24), comment='工序号')
    operation = Column(VARCHAR(255), comment='工序描述')
    parameter_number = Column(VARCHAR(24), comment='参数号')
    parameter = Column(VARCHAR(255), comment='参数描述')
    create_user = Column(BigInteger, comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    update_user = Column(BigInteger, comment='更新人')
    update_time = Column(DateTime, comment='更新时间')
    tombstone = Column(CHAR(1), server_default=text("'0'"), comment='逻辑删除')





