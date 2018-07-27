"""
-- 1 自关联查询
	-- 通俗讲，就是自己关联自己,再通过内连接实现数据查询

	--1.1 创建areas表(aid,atilte,pid)
		create table areas(
    aid int primary key,
    atitle varchar(20),
    pid int
	);

	--1.2 向areas插入记录
	   source areas.sql;
		提示： areas.sql要存放在 mysql登录的目录中

	--1.3 查询一共有多少个省
		select * from areas where pid is null;

	--1.4 查询广东省中的所有城市
	--select city.* from areas as city inner join areas as province on city.pid=province.aid where province.atitle='广东省';

	   第一种方式(两条sql语句)：
	      1. 查广东省的id
	        select aid from areas where atitle='广东省';//440000
	      2. 再把省的id作为pid，查出对应的城市信息
	        select * from areas where pid=440000;

	   第二种方式(子查询)：
	   	select * from areas where pid=(select aid from areas where atitle='广东省');

	   第三种方式(自关联)：
	   	select city.* from areas as city  inner join areas as province on city.pid=province.aid  where province.atitle='广东省';



	--1.5 查询属于深圳市的所有的区
	--select a.* from areas as a inner join areas as c on a.pid=c.aid where c.atitle='深圳市';
		select a.* from areas as a  inner join areas as c on a.pid=c.aid  where c.atitle='深圳市';


--2. 初始化数据
	--2.1 创建'京东'数据库 db_jingdong
		create database db_jingdong charset=utf8;
			use db_jingdong;

	--2.2 创建商品表goods(int,name,cate_name,brand_name,price,is_show,is_saleoff)
	create table goods(
    id int unsigned primary key auto_increment not null,
    name varchar(150) not null,
    cate_name varchar(40) not null,
    brand_name varchar(40) not null,
    price decimal(10,3) not null default 0,
    is_show bit not null default 1,
    is_saleoff bit not null default 0
	);


	--2.3 向goods表插入初始数据
insert into goods values(0,'r510vc 15.6英寸笔记本','笔记本','华硕','3399',default,default);
insert into goods values(0,'y400n 14.0英寸笔记本电脑','笔记本','联想','4999',default,default);
insert into goods values(0,'g150th 15.6英寸游戏本','游戏本','雷神','8499',default,default);
insert into goods values(0,'x550cc 15.6英寸笔记本','笔记本','华硕','2799',default,default);
insert into goods values(0,'x240 超极本','超级本','联想','4880',default,default);
insert into goods values(0,'u330p 13.3英寸超极本','超级本','联想','4299',default,default);
insert into goods values(0,'svp13226scb 触控超极本','超级本','索尼','7999',default,default);
insert into goods values(0,'ipad mini 7.9英寸平板电脑','平板电脑','苹果','1998',default,default);
insert into goods values(0,'ipad air 9.7英寸平板电脑','平板电脑','苹果','3388',default,default);
insert into goods values(0,'ipad mini 配备 retina 显示屏','平板电脑','苹果','2788',default,default);
insert into goods values(0,'ideacentre c340 20英寸一体电脑 ','台式机','联想','3499',default,default);
insert into goods values(0,'vostro 3800-r1206 台式电脑','台式机','戴尔','2899',default,default);
insert into goods values(0,'imac me086ch/a 21.5英寸一体电脑','台式机','苹果','9188',default,default);
insert into goods values(0,'at7-7414lp 台式电脑 linux ）','台式机','宏碁','3699',default,default);
insert into goods values(0,'z220sff f4f06pa工作站','服务器/工作站','惠普','4288',default,default);
insert into goods values(0,'poweredge ii服务器','服务器/工作站','戴尔','5388',default,default);
insert into goods values(0,'mac pro专业级台式电脑','服务器/工作站','苹果','28888',default,default);
insert into goods values(0,'hmz-t3w 头戴显示设备','笔记本配件','索尼','6999',default,default);
insert into goods values(0,'商务双肩背包','笔记本配件','索尼','99',default,default);
insert into goods values(0,'x3250 m4机架式服务器','服务器/工作站','ibm','6888',default,default);
insert into goods values(0,'商务双肩背包','笔记本配件','索尼','99',default,default);

selc
--3. sql强化演练( goods 表练习)

	-- 3.1 查询类型 cate_name 为 '超级本' 的商品名称 name 、价格 price ( where )
	select name,price,cate_name from goods where cate_name='超级本';

	-- 3.2 显示商品的种类
		-- 1 分组的方式( group by )
			select cate_name from goods group by cate_name;

		-- 2 去重的方法( distinct )
			select distinct cate_name from goods;

	-- 3.3 求所有产品的平均价格 avg ,并且保留两位小数( round :四舍五入)
		select round(avg(price),2) from goods;

	-- 3.4 显示 每种类型 cate_name (由此可知需要分组)的 平均价格
		select cate_name,round(avg(price),2) from goods group by cate_name;

	-- 3.5 查询 每种类型 的商品中 最贵 max 、最便宜 min 、平均价 avg 、数量 count
	select cate_name,max(price), min(price), round(avg(price),2) as '平均价格',count(*) from goods group by cate_name;


	-- 3.6 查询所有价格大于 平均价格 的商品，并且按 价格降序 排序 order desc

		-- 1 查询平均价格(avg_price)
			select round(avg(price),2) from goods;

		-- 2 使用子查询
			select * from goods where price>(select avg(price) from goods) order by price desc;


	-- 3.7 查询每种类型中最贵的产品信息(难)
	      每种类型最贵价格
	        分组  - max(price)

	      产品信息
	         goods表

		-- 1 查找 每种类型 中 最贵的 价格
		   select cate_name,max(price) from goods group by cate_name;

		-- 2 关联查询 inner join 每种类型 中最贵的产品信息
		   select g.*  from goods as g inner join (select cate_name,max(price) as m_price from goods group by cate_name) as m on g.cate_name=m.cate_name and g.price=m.m_price;


--4. 数据表设计与创建

	-- 4.1 创建"商品分类"表

		第一步	创建表 (商品种类表 goods_cates )
			create table if not exists goods_cates(
    id int unsigned primary key auto_increment,
    name varchar(40) not null
);


		第二步	同步 商品分类表 数据 将商品表的所有 (种类信息) 写入到 (商品种类表) 中
		   1. 直接手动添加
		   2. 通过查询结果来添加到商品列表表中

		-- 按照 分组 的方式查询 goods 表中的所有 种类(cate_name)
		    -- 去重(distinct)
		     select distinct cate_name from goods;
		-- 通过sql语句取得要插入的数据
			insert into goods_cates(name) (select distinct cate_name from goods);

		--(注意) 把查询出来的 结果 写入 goods_cates 表里去 ( insert into ) 只插入name ,且不需要加values


		第三部 同步 商品表 数据 通过 goods_cates 数据表来更新 goods 表

		-- 因为要通过 goods_cates表 更新 goods 表 所以要把两个表连接起来
			select * from goods as g inner join goods_cates as c on g.cate_name=c.name;

		-- 把 商品表 goods 中的 cate_name 全部替换成 商品分类表中的 商品id ( update ... set )
		 update goods as g inner join goods_cates as c on g.cate_name=c.name  set g.cate_name=c.id;

		第四部 修改表结构

		-- 查看表结构(注意 goods表的cate_id 与 goods_cates表的 id 字段 类型需要一致)
		  desc goods_cates;

		-- 修改表结构 alter table 字段名字不同 change,把 cate_name 改成 cate_id int unsigned not null
		 alter table goods change cate_name cate_id int unsigned not null;


	-- 4.2 创建 商品品牌表 goods_brands

		第一步 创建 "商品品牌表" 表
		-- 创建goods_brands表
		create table if not exists goods_brands(
    id int unsigned primary key auto_increment,
    name varchar(40) not null
);

		-- 插入数据 ，数据来自goods表
		-- 按照 分组 的方式查询 goods 表中的所有 种类(brand_name)
		select brand_name from goods group by brand_name;

		--(注意) 把查询出来的 结果 写入 goods_brands 表里去 ( insert into ) 只插入name
		insert into goods_brands(name) (select brand_name from goods group by brand_name);

		第二步 同步数据
		-- 通过goods_brands数据表来更新goods数据表 g.brand_name=b.id
		1. select * from goods as g inner join goods_brands as b on g.brand_name=b.name;
		2. update goods as g inner join goods_brands as b on g.brand_name=b.name set g.brand_name=b.id;



		第三部 修改表结构
		-- 通过alter table语句修改表结构 brand_id int unsigned not null
		alter table goods change brand_name brand_id int unsigned not null;



--5. 外键的使用(了解)

	--5.1 向goods表里插入任意一条数据
	 insert into goods (name,cate_id,brand_id,price) values('联想固态硬盘',10,10,1200);

	--5.2 使用外键约束 foreign key
	-- alter table goods add foreign key (brand_id) references goods_brands(id);
	alter table goods add foreign key(cate_id) references goods_cates(id);
	alter table goods add foreign key(brand_id) references goods_brands(id);

	-- 失败原因 ,因为'联想固态硬盘'这行的数据不满足外键约束 delete
	-- delete from goods where name="联想固态硬盘";
	  delete from goods where id=22;

	--5.3 创建表的同时设置外键 (注意 goods_cates 和 goods_brands 两个表必须事先存在)
	create table goods(
		id int primary key auto_increment not null,
		name varchar(40) default '',
		price decimal(5,2),
		cate_id int unsigned,
		brand_id int unsigned,
		is_show bit default 1,
		is_saleoff bit default 0,
		foreign key(cate_id) references goods_cates(id),
		foreign key(brand_id) references goods_brands(id)
	);


	--5.4 如何取消外键约束


	-- 需要先获取外键约束名称,该名称系统会自动生成,可以通过查看表创建语句来获取名称
         show create table goods;
	-- 获取名称之后就可以根据名称来删除外键约束
	--alter table goods drop foreign key goods_ibfk_1;
	alter table goods drop foreign key goods_ibfk_1;
	alter table goods drop foreign key goods_ibfk_2;

	--5.5 涉及外键的面试
	   在目前主流的数据库设计中,越来越少使用到外键约束
	    原因： 会极大的降低表更新的效率
		如何替代 '通过外键约束实现数据有效性验证'
		解决思想： 可在数据录入时验证(表示层，ui层)，或者在业务层面(python代码)去验证，而不要数据库层面去验证。

"""