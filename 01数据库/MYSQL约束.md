##mysql约束之alter总结

**ALTER TABLE** 

- MODIFY 修改
- ADD  增加
- DROP 删除

---

- 非空 NOT NULL
- UNIQUE KEY  唯一
- DEFUALUT 默认
- AUTO_INCREMENT  (必须与主键一起使用)

---
实例演示：

**<1> 创建数据表tb1**

    mysql> create table tb1(id int);
    Query OK, 0 rows affected (0.04 sec)
    
    mysql> desc tb1;
    +-------+---------+------+-----+---------+-------+
    | Field | Type    | Null | Key | Default  | Extra |
    +-------+---------+------+-----+---------+-------+
    | id    | int(11) | YES  |     | NULL    |        |
    +-------+---------+------+-----+---------+-------+

**<2> 为tb1添加非空约束 not null**

    mysql> alter table tb1
    -> modify id int not null
    -> ;
    Query OK, 0 rows affected (0.07 sec)
    Records: 0  Duplicates: 0  Warnings: 0
    
    mysql> desc tb1;
    +-------+---------+------+-----+---------+-------+
    | Field | Type    | Null | Key | Default | Extra |
    +-------+---------+------+-----+---------+-------+
    | id    | int(11) | NO   |     | NULL    |       |
    +-------+---------+------+-----+---------+-------+
    1 row in set (0.00 sec)

**注意：** 删除非空约束使用同样方法

**<3> 为tb1添加唯一键 unique key**

    mysql> alter table tb1
    -> add unique key (id)
    -> ;
    Query OK, 0 rows affected (0.06 sec)
    Records: 0  Duplicates: 0  Warnings: 0
    
    mysql> desc tb1;
    +-------+---------+------+-----+---------+-------+
    | Field | Type    | Null | Key | Default | Extra |
    +-------+---------+------+-----+---------+-------+
    | id    | int(11) | NO   | PRI | NULL    |       |
    +-------+---------+------+-----+---------+-------+
    1 row in set (0.00 sec)

**注意 ：** not null + unique key 具有 primary key的功能，当表中没有primary key 时， not null + unique key =  primary key

但是我们运行show create table tb1\G 查看详细信息时可以依然看到为 nunque key。

    mysql> show create table tb1\G
    ********************** 1. row **********************
    Table: tb1
    Create Table: CREATE TABLE `tb1` (
      `id` int(11) NOT NULL,
      UNIQUE KEY `id` (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    1 row in set (0.00 sec)

    
**<4> 为tb1添加主键 primary key（在一张表中只能有一个主键）**

    mysql> alter table tb1
    -> add primary key (id)
    -> ;
    Query OK, 0 rows affected (0.06 sec)
    Records: 0  Duplicates: 0  Warnings: 0
    
    mysql> desc tb1;
    +-------+---------+------+-----+---------+-------+
    | Field | Type    | Null | Key | Default | Extra |
    +-------+---------+------+-----+---------+-------+
    | id    | int(11) | NO   | PRI | NULL    |       |
    +-------+---------+------+-----+---------+-------+
    1 row in set (0.00 sec)

**注意：** 虽然此处表结构表面上未发生变化，但是我们运行show create table tb1\G 查看详细信息就可以发现已经添加上主键了。

    mysql> show create table tb1\G
    *************************** 1. row ***************************
    Table: tb1
    Create Table: CREATE TABLE `tb1` (
      `id` int(11) NOT NULL,
      PRIMARY KEY (`id`),
      UNIQUE KEY `id` (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    1 row in set (0.00 sec)

**<5> 删除主键 primary key**

    mysql> alter table tb1
    -> drop primary key
    -> ;
    Query OK, 0 rows affected (0.05 sec)
    Records: 0  Duplicates: 0  Warnings: 0
    
    mysql> show create table tb1\G
    *************************** 1. row ***************************
       Table: tb1
    Create Table: CREATE TABLE `tb1` (
      `id` int(11) NOT NULL,
      UNIQUE KEY `id` (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    1 row in set (0.00 sec)

**注意：** 因为主键是非空且唯一的，所以删除时直接删除主键即可，不用跟具体的列名。

**<5> 删除唯一键 unique key**

    mysql> alter table tb1
    -> drop key id
    -> ;
    Query OK, 0 rows affected (0.02 sec)
    Records: 0  Duplicates: 0  Warnings: 0
    
    mysql> show create table tb1\G
    *************************** 1. row ***************************
       Table: tb1
    Create Table: CREATE TABLE `tb1` (
      `id` int(11) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    1 row in set (0.00 sec)
    
    mysql> desc tb1;
    +-------+---------+------+-----+---------+-------+
    | Field | Type    | Null | Key | Default | Extra |
    +-------+---------+------+-----+---------+-------+
    | id    | int(11) | NO   |     | NULL    |       |
    +-------+---------+------+-----+---------+-------+
    1 row in set (0.00 sec)

**注意：**add操作是需要在列名后加（），drop不需要


**<6> 把id这一列设置为自增长**

    mysql> desc tb1;
    +-------+---------+------+-----+---------+-------+
    | Field | Type    | Null | Key | Default | Extra |
    +-------+---------+------+-----+---------+-------+
    | id    | int(11) | NO   |     | NULL    |       |
    +-------+---------+------+-----+---------+-------+
    1 row in set (0.00 sec)
    
    mysql> alter table tb1
    -> modify id int primary key auto_increment
    -> ;
    Query OK, 0 rows affected (0.04 sec)
    Records: 0  Duplicates: 0  Warnings: 0
    
    mysql> desc tb1;
    +-------+---------+------+-----+---------+----------------+
    | Field | Type    | Null | Key | Default | Extra          |
    +-------+---------+------+-----+---------+----------------+
    | id| int(11)     | NO   | PRI | NULL    | auto_increment |
    +-------+---------+------+-----+---------+----------------+
    1 row in set (0.00 sec)

**<7> 添加外键 foreign key**

**首先，我们来创建tb2**

    mysql> create table tb2(
    -> s_id int primary key,
    -> name varchar(20) not null
    -> );
    Query OK, 0 rows affected (0.03 sec)

**其次，我们假设后期需要用到tb2关联tb1，我们添加foreign key**

    mysql> alter table tb2
    -> add constraint tb2_1_fk foreign key (s_id) references tb1 (id)
    -> ;
    Query OK, 0 rows affected (0.05 sec)
    Records: 0  Duplicates: 0  Warnings: 0
**注意：** constraint tb2_1_fk 表示将外键名称定为tb2_1_fk，如果我们在添加时不定义，系统就会自动分配外键名称。

**最后我们查询表详细信息**

    mysql> show create table tb2\G
    *************************** 1. row ***************************
       Table: tb2
     Create Table: CREATE TABLE `tb2` (
      `s_id` int(11) NOT NULL,
      `name` varchar(20) NOT NULL,
      PRIMARY KEY (`s_id`),
      CONSTRAINT `tb2_1_fk` FOREIGN KEY (`s_id`) REFERENCES `tb1` (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    1 row in set (0.00 sec)

**<8> 删除外键 foreign key**

    mysql> alter table tb2
    -> drop foreign key tb2_1_fk;
    Query OK, 0 rows affected (0.05 sec)
    Records: 0  Duplicates: 0  Warnings: 0
    
    mysql> show create table tb2\G
    *************************** 1. row ***************************
       Table: tb2
    Create Table: CREATE TABLE `tb2` (
      `s_id` int(11) NOT NULL,
      `name` varchar(20) NOT NULL,
      PRIMARY KEY (`s_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    1 row in set (0.00 sec)

**<9> 设置初始默认值 default**

    mysql> alter table tb2
    -> add age int not null default 18;
    Query OK, 0 rows affected (0.04 sec)
    Records: 0  Duplicates: 0  Warnings: 0
    
    mysql> desc tb2;
    +-------+-------------+------+-----+---------+-------+
    | Field | Type        | Null | Key | Default | Extra |
    +-------+-------------+------+-----+---------+-------+
    | s_id  | int(11)     | NO   | PRI | NULL    |       |
    | name  | varchar(20) | NO   |     | NULL    |       |
    | age   | int(11)     | NO   |     | 18      |       |
    +-------+-------------+------+-----+---------+-------+
    3 rows in set (0.01 sec)

