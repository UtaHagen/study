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

4. Create cl program
--cl create a library
   CRTLIB LIB(MYLIB) 
--cl create a source fule
   CRTSRCPF FILE(MYLIB/QCLSRC) RCDLEN(112) TEXT('CL source file')
--cl edit the member in SEU interface
   WRKMBRPDM FILE(DBRXData/QCLSRC)

5. WOrk with Members
Press F6 to create a new ember
source member: name
source type: clp
sample code:
PGM
  CPYTOIMPF FROMFILE(database/file) TOSTMF('/new_folder/file.csv') +
            MBROPT(*REPLACE) RCDDLM(*CRLF) DTAFMT(*DLM) +
            STRDLM(*DBLQUOTE) ADDCOLNAM(*SQL)
ENDPGM
to add a new line, type I in the 0001.00/0002.00/0003.00 press enter
6. Compile a member as a program
Super annoying: Turn off batch job by Press F18 and change Y to N
back to SEU type 14 for Opt.
For any trouble shooting the error use WRKMSG

8. Test it use: CALL PGM(Library/program_name)

9. Special case DDM
    <img width="776" height="498" alt="image" src="https://github.com/user-attachments/assets/785aea8b-1d4d-42c8-b227-02e85a461181" />


