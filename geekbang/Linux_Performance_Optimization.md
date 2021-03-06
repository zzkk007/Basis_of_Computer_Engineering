"----------------------------------------------------------------------"

          本篇是学习极客时间倪朋飞专栏<Linux 性能优化实战>学习笔记

"----------------------------------------------------------------------"

"""01| 如何学习 Linux 性能优化"""

    1、性能的指标是什么？
    
        “高并发” 和 “响应快” 正对应性能优化的两个核心指标--“吞吐” 和 “延时”。
        这两个指标从应用负载的视角来考察性能，直接影响了产品终端的用户体验。
        根他们对应的，是从系统资源的视角出发的指标，比如资源使用率、饱和度等。
        
        性能问题的本质，就是系统资源已经到达瓶颈，但请求处理却还不够快，无法支撑更多请求。
        
        性能分析，其实就是找出应用或系统的瓶颈，并设法去避免或者缓解它们。


"""02|基础篇: 到底应该怎么理解平衡负载"""
        
    每次发现系统变慢时，我们通常第一件事，就是执行 top 或者 uptime 命令，
    来了解系统的负载情况。
    
    debian:~$ uptime
    17:01:58 up 518 days, 26 min,  3 users,  load average: 0.00, 0.01, 0.05
    
        17:01:58            : 当前时间
        up 518 days, 42 min : 系统运行时间
        3 users             : 正在登陆用户数
        load average: 0.00, 0.01, 0.05 : 分别是过去 1 分钟、5分钟、15分钟的平均负载(Load Average)。
        
             
    1、平均负载：
        
        简单来说，平均负载是指单位时间内，系统处于可运行状态和不可中断状态的平均进程数，也就是平均活跃进程数。
        它和 CPU 使用 率并没有直接关系。
        
        所谓的可运行状态的进程，是指正在使用 CPU 或者正在等待 CPU 的进程，也就是我们常用 ps 命令看到的，
        处于 R 状态(Running 或 Runnable) 的进程。
        
        不可中断状态的进程则是正处于内核态关键流程的进程，并且这些流程是不可打断的，
        比如最常见的是等待硬件设备的 I/O 响应，也就是我们在 ps 命令中看到 D 状态
        (Uninterruptible Sleep, 也称为 Disk Sleep)的进程。
        不可中断状态实际上是系统对进程和硬件设备的一种保护机制。
        
        因此，平均负载其实就是平均活跃进程数，平均活跃进程数，直观上的理解就是单位时间内的活跃进程数，
        但它实际上是活跃进程数的指数衰减平均值。
        
        既然平均的是活跃进程数，那么最理性的，就是每个 CPU 上刚好运行这一个进程，这样的 CPU 都得到充分利用。
        比如当平均负载为 2 时，意味着：
            
            在只有 2 个 CPU 的系统上，意味着所有 CPU 都刚好被完全占用。
            在 4 个CPU 的系统上，意味着 CPU 有 50% 的空闲
            而在只有 1 个 CPU 的系统中，则意味着有一半的进程竞争不到 CPU。
            
    2、 平均负载为多少时合理：
    
    
    
    
                
            
                
        
        












        
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    