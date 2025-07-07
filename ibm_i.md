### This is dealing with version 7.3 AS400 Access Client Slutions

Documentation: https://ibmi-oss-docs.readthedocs.io/en/latest/yum/README.html

1. Check Access: 
-- cl
DSPUSRPRF USRPRF(YOUR_USERNAME)

2. install yum /python etc for Open Source Package Managment
--cl
CALL QP2TERM

-- /QOpenSys/user/bin/-sh
sh /tmp/bootstrap.sh
export PATH=/QOpenSys/pkgs/bin:$PATH
-- verify
yum --version
yum install python3-pip

3. - Change TCP/IP Domain
--cl
CFGTCP
12
CHGTCPDMN 

STRTCPSVR *DNS
PING RMTSYS('public.dhe.ibm.com')

