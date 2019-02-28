"--------------------------------------------------------"

           极客时间 林晓斌 《MySQL 实战 45 讲》

"--------------------------------------------------------"

"""01| 基础架构: 一条 SQL 查询语句是如何执行的？"""

    1、MySQL 组成:
    
        MySQL 可以分为 Server 层和存储引擎层两部分。
        
        Server 层包括：连接器、查询缓存(MySQL 8.0删除缓存模块)、分析器、优化器、执行器等。
        涵盖 MySQL 的大多数核心服务功能，以及所有的内置函数(如日期、时间、数学和加密函数等)
        所有跨存储引擎的功能都在这一层实现，比如：存储过程、触发器、视图等。
        
        存储引擎：负责数据的存储和提取。其架构模式是插件式的，支持 InnoDB、MyISAM、Memory 等
        多个存储引擎。MySQL 5.5 默认 InnoDB 存储引擎。    
        不同的存储引擎共用一个 Server 层。也就是从连接器到执行器的部分。
        
    2、连接器:
        
        连接器负责跟客户端建立连接、获取权限、维持和管理连接。
        连接命令一般是这么写：
            
            mysql -h$ip -P$port -u$user -p
            
        数据库里面，长连接是指连接成功后，如果客户端持续有请求，则一直使用同一个连接。
        短连接则是指每次执行完很少的几次查询就断开连接，下一次查询再重新建立一个。
        
        建立连接的过程比较复杂，尽量减少建立连接的动作，也就是尽量使用长连接。
        但是，全部使用长连接，MySQL 占用内存涨得特别快，这是因为 MySQL 在执行过程
        中临时使用的内存是管理在连接对象里面的，这些资源会在断开连接的时候才释放。
        如果长连接积累下来，可能导致内存占用太大，被系统强行杀掉（OOM）,从现象
        上看就是 MySQL 异常重启。
        
        解决办法：
        
            a. 定期断开长连接。
            
            b. 如果你使用的是 MySQL 5.7 或更新版本，可以在每次执行一个比较大的操作后，通过
                执行 mysql_reset_connection 来重新初始化连接资源。这个过程不需要重连和重新
                做权限验证，但是会恢复到刚刚建完时的状态。
                
    3、查询缓存：
    
        MySQL 拿到一个请求后，会先到查询缓存看看，之前是不是执行过这条语句，之前执行过的语句及结果
        可能会以 key-value 对的形式被直接缓存到内存中。key 是查询的语句。value是查询的结果。
        如果语句不在查询缓存中，就会继续后面的执行阶段。执行完成后，执行结构会被存入查询缓存中。
        
        但是建议不要使用缓存，往往弊大于利。
        MySQL 将参数 query_cache_type 设置成 DEMAND, 这样对于默认的 SQL 语句都不使用查询缓存。
        
        MySQL8.0 版本直接将查询缓存整块功能删掉了。
        
    4、分析器：
    
        分析器 先会做“词法分析”。你输入的由多个字符串和空格组成的一条 SQL 语句， MySQL 需要识别
        出里面的字符串分别是什么，代表什么。
        
        然后是“语法分析”。根据“词法分析”结果，语法分析会根据语法分析规则，判断是否满足 MySQL 语法。
        
    5、优化器：
    
        经过 分析器，MySQL 就知道你要做什么了，在开始执行之前，还要经过优化器的处理。
        
        优化器是在表里面有多个索引的时候，决定使用哪个索引；或者在一个语句有多个关联(join)
        的时候，决定各个表的连接顺序。
        
        mysql > select * from t1 join t2 using(ID) where t1.c = 10 and t2.d = 20;
        
        即可以先从表 t1 里面取出 c = 10 的记录的 ID 值，再根据 ID 值关联到表 t2, 再判断 t2 里面 d 的值是否等于 20.        
        也可以先从表 t2 里面取出 d = 20 的记录的 ID 值，再根据 ID 值关联到表 t1, 再判断 t1 里面 c 的值是否等于 10.

        优化器阶段完成后，这个语句的执行方案就确定下来了。然后进行执行器阶段。                     
            
    6. 执行器：
    
        mysql> select *from T where ID = 10;
        
        开始执行的时候，要判断一下你对这个表 T 有没有执行查询的权限，如果没有，就会返回没有权限的错误。
        如果有权限，就开打表继续执行，打开表的时候，执行器就会根据表的引擎定义，去使用这个引擎提供的接口。
        
        比如上面的例子表 T 中，ID 字段没有索引，那么执行器的执行流程是这样的：
        
            a. 调用 InnoDB 引擎接口取这个表的第一行，判断 ID 值是不是 10，如果不是则跳过，
                如果是则将这行存在的结果集中;
                
            b. 调用引擎接口取“下一行”，重复相同的判断逻辑，直到取到这个表的最后一行。
            
            c. 执行器将上述遍历过程中所有满足条件的行组成记录集作为结果集返回给客户端。
            
        至此，这个语句就执行完成了。
        
        对于有索引的表，执行的逻辑也差不多。第一次调用的是“取满足条件的第一行”这个接口，
        之后循环取“满足条件的下一行”这个接口，这些接口都是在引擎中定义好的。
        
        你会在数据库慢日志看到一个 rows_examined 的字段，表示这个语句执行过程中扫描了多少行。
        这个值就是在执行器每次调用引擎获取数据行的时候累加的。
        
        
"""02| 日志系统： 一条 SQL 更新语句是如何执行的"""        

    1、一条更新语句的执行流程是怎么样的呢？
        
        表的创建语句，这个表有一个主键 ID 和一个整型字段 c:
            mysql> create table T(ID int primary key, c int);
        
        如果要将 ID=2 这一行的值加 1，SQL 语句就会这么写：
            mysql> update T set c = c+1 where ID=2;
    
        更新语句的执行流程和查询流程一样，都有经过 连接器、清除缓存(语句会把表T上所有的缓存结果都清空)，
        分析器、执行器。                    
        与查询流程不一样的是，更新流程还涉及两个重用的日志模块，redo log(重做日志) 和 binlog(归档日志)。
        
    2、重要的日志模块：redo log
    
        《孔乙己》文章中，酒店掌柜有一个粉板，专门用来记录客人的赊账记录，如果赊账的人不多，
        就把客户名和账目写在板上，如果赊账人太多，粉板记不下的时候，掌柜还需要一个专门记录
        赊账的账本。
        
        如果有人要赊账或者还账的话，掌柜的一般有两种做法:
            一种做法是把账本翻出来，把这次赊账加上去或者扣除掉。
            另一种做法是现在粉板上记录这次的账，等打烊以后再把账本翻出来核算。
            
        同样，在MySQL 里面也有这个问题，如果每次更新操作都需要写进磁盘，然后磁盘也要找到对应的那条记录，
        然后再更新，整个过程 IO 成本、查找成本都很高。为了解决这个问题， MySQL 的设计者就用类似酒店粉板
        的思路来提升更新效率。
        
        粉板和账本配合的整个过程，其实就是 MySQL 里面经常说的 WAL 技术， WAL 的全称是 Write-Ahead Logging
        它的关键点就是先写日志，再写磁盘，也就是先写粉板，等不忙的时候再写账本。
        
        具体来说，当有一条记录需要更新的时候，InnoDB 引擎就会先把记录写到 redo log (粉板)里面，并更新内存，
        这个时候更新就算完成了。同时，InnoDB 引擎会在适当的时候，将这个操作记录更新到磁盘里面，而这个更新往往
        是在系统比较空闲的时候做。
        
        如果今天赊账不多，掌柜可以等打烊后再整理，但如果某天赊账特别多，粉板写满了，这时候，掌柜只好放下手中
        的活，把粉板中的一部分赊账记录更新到账本中，然后，把这些记录从粉板上擦掉，为记新账腾出新空间。
        
        与此类似，InnoDB 的 redo log 是固定大小的，比如可以配置为一组 4 个文件，每个文件的大小是 1GB，那么
        这块“粉板”总共可以记录 4GB 操作。
        
        有了 redo log, InnoDB 就可以保证即使数据库发送异常重启，之前提交的记录都不会丢失，这个能力成为 crash-safe。
        要理解 crash-safe 这个概念，可以想想赊账记录的例子，只有赊账记录在粉板上或写在账本上，这后即使掌柜的忘记了
        突然停业几天，恢复生意后可以通过账本和粉板上的数据明确赊账账目。
        
        
    3、 重要的日志模块：binlog:
    
        MySQL 有两块：一块是 Server 层有自己的日志，称为 binlog (归档日志)   
        上面的聊到的粉板 redo log 是 InnoDB 引擎特有的日志。
        
        两种日志 redo log 和 binlog 有以下三点不同：
        
            a. redo log 是 InnoDB 引擎特有的; binlog 是 MySQL 的 Server 层实现的，所有引擎都可以使用。
            
            b. redo log 是物理日志，记录的是“在某个数据页上做了什么修改”；
               binlog 是逻辑日志，记录的是这个语句的原始逻辑，比如“给 ID=2 这一行的 c 字段加 1”。
               
            c. redo log 是循环写的，空间固定会用完；binlog 是可以追加写入的。
                “追加写” 是指 binlog 文件写到一定大小后会切换到下一个，并不会覆盖以前的日志。
                
    4、执行器和 InnoDB 引擎在执行这个简单的 update 语句时的内部流程：
    
        a.  执行器先找到引擎取 ID = 2 这一行。 ID 是主键，引擎直接用树搜索找到这一行。
            如果 ID = 2 这一行所在的数据页本来就走内存内，就直接返回给执行器；否则
            需要先从磁盘读入内存，然后再返回。
            
        b.  执行器拿到引擎给的行数据，把这个值加上 1， 比如原来是 N, 现在就是 N+1,
            得到新的一行数据，再调用引擎接口写入这行新数据。
            
        c.  引擎将这行新数据更新到内存中，同时将这个更新操作记录到 redo log 里面，
            此时 redo log 处于 prepare 状态，然后告知执行器执行完成了，随时可以提交事务。
            
        d.  执行器生成这个操作的 binlog，并把 binlog 写入磁盘。
        
        e.  执行器调用引擎的提交事务接口，引擎把刚刚写入的 red log 改成提交（commit）状态，更新完成。
                  
                    
    5、两阶段提交：
    
        那可能注意到了，redo log 的写入拆成了两个步骤：prepare 和 commit,这就是“两阶段提交”
        为什么必须要有“两个阶段提交”呢，是为了让两份日志之间的逻辑一致。
        
        怎么让数据库恢复到半月内任意一秒的状态？
        我们前面说了，binlog 会记录所有的逻辑操作，并且采用“追加写” 的形式，如果 DBA 承诺半个月内
        可以恢复，那么备份系统中一定会保存最近半月的所有 binlog，同时系统会定期做正库备份。
        
        当需要恢复到指定的某个时间某一秒时，
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                    
                   
        
        
            
            
        
               
        
            
    
        
        
















    