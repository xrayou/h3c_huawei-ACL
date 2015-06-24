#!/etc/bin/env python
#codeing:utf-8

import os

files =  open("/Users/baozhibo/Desktop/qos.txt",'w') #创建文件

for i in range(10,30):#起始VlanId跟IP段
        files.write("vlan " + str(i) + '\n')#创建vlan

        files.write("quit" + '\n')

        files.write("interface Vlanif " + str(i) +'\n')#进入vlan

        files.write("ip address 192.168."  + str(i) + "." + "1" + " 255.255.255.0" + '\n')#创建网关

        files.write("quit" + "\n")

        files.write("acl number 30" + str(i) + '\n')#30开头的acl为允许列表（可自行添加允许的网段）

        files.write("rule permit ip source 192.168." + str(i) + ".0 0.0.0.255 destination 192.168." + str(i) +".0 0.0.0.255 " + '\n')

        files.write("quit" + '\n')

        files.write("acl number 39" + str(i) + '\n')#39开头的acl为拒绝列表（一般拒绝为整个段）此处为匹配流量，所以都用permit，这里的permit只是针对匹配流量，没有真正意义的拒绝与允许的流控制

        files.write("rule permit ip source 192.168." + str(i) + ".0 0.0.0.255 destination 192.168.0.0 0.0.255.255 " + '\n')

        files.write("quit" + '\n')

        files.write("traffic classifier 30" + str(i) + '\n')#创建acl分类项

        files.write("if-match acl 30" + str(i) + '\n')#匹配acl

        files.write("quit" + '\n')

        files.write("traffic classifier 39" + str(i) + '\n')#创建acl分类项

        files.write("if-match acl 39" + str(i) + '\n')#匹配acl

        files.write("quit" + '\n')

        files.write("traffic behavior 30" + str(i) + '\n')#创建流行为

        files.write("permit" + '\n')#流行为

        files.write("quit" + '\n')

        files.write("traffic behavior 39" + str(i) + '\n')#创建流行为

        files.write("deny" + '\n')#流行为

        files.write("quit" + '\n')

        files.write("traffic policy vlan" + str(i) + '\n')#创建策略

        files.write("classifier " + "30" + str(i) + " behavior " + "30" + str(i) + '\n')#acl分类项与流行为绑定

        files.write("classifier " + "39" + str(i) + " behavior " + "39" + str(i) + '\n')#acl分类项与流行为绑定

        files.write("quit" + '\n')

        files.write("vlan " + str(i) + '\n')#进入vlan
        
        #files.write("qos vlan-policy vlan" + str(i) + " vlan " + str(i) + " inbound ")#h3c无需进入vlan进行绑定，注释掉63行和67行

        files.write("traffic-policy vlan" + str(i) + " inbound " + '\n')#跟vlan绑定acl（也可以在端口绑定acl行为）

        files.write("quit" + '\n')
