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
######   WRKMBRPDM FILE(DBRXData/QCLSRC)

5. Work with Members
Press F6 to create a new ember
source member: name
source type: clp
sample code:
PGM                                                                   
  CPYTOIMPF FROMFILE(MPUBFILE/MITNFL) TOSTMF('/XIALIN/MITNFL.CSV') +  
            MBROPT(*REPLACE) RCDDLM(*CRLF) DTAFMT(*DLM) FLDDLM('|') +             
            STRDLM(*DBLQUOTE) ADDCOLNAM(*SQL) STMFCCSID(1208)                  
ENDPGM                                                                
to add a new line, type I in the 0001.00/0002.00/0003.00 press enter
###### Best practice for csv, USE |!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
7. Compile a member as a program
Super annoying: Turn off batch job by Press F18 and change Y to N
back to SEU type 14 for Opt.
#### For any trouble shooting the error use WRKMSG

8. Test it use: CALL PGM(Library/program_name)
### WRKMBRPDM -- go to SEU
WRKSBMJOB 

10. Special case DDM

find table schema: in sql scripts
SELECT 
COLUMN_NAME, DATA_TYPE, LENGTH, NUMERIC_SCALE
FROM QSYS2.SYSCOLUMNS
WHERE TABLE_NAME = 'MSTAF1_UK';

-- cl STRSEU SRCFILE(DBRXDATA/QDDSSRC) SRCMBR(MSTAF1_UK) TYPE(PF)

<img width="776" height="498" alt="image" src="https://github.com/user-attachments/assets/785aea8b-1d4d-42c8-b227-02e85a461181" />

--cl CRTPF FILE(DBRXDATA/MSTAF1_UK) SRCFILE(DBRXDATA/QDDSSRC)

--cl CPYF FROMFILE(MPUBFILE/MSTAF1_UK) TOFILE(DBRXDATA/MSTAF1_UK) MBROPT(*REPLACE) FMTOPT(*NOCHK)     

CPYTOIMPF FROMFILE(DBRXDATA/MSTAF1_UK) TOSTMF('/XIALIN/MSTAF1_UK.CSV')  
MBROPT(*REPLACE) RCDDLM(*CRLF) DTAFMT(*DLM) ADDCOLNAM(*SYS) STMFCCSID(1208) STRDLM(*DBLQUOTE) 

Edit the newly created physical file:
--cl WRKMBRPDM FILE(DBRXDATA/QDDSSRC)

DSPPFM DBRXDATA/MSTAF1_UK for checking the created physical file

View the physical phile:
-- cl DSPPFM DBRXDATA/MSTAF1_UK
11. Schedule the Job
    
-- cl
WRKJOBSCDE
Press F6 Add
<img width="1396" height="582" alt="image" src="https://github.com/user-attachments/assets/d139f0a1-9e84-482d-9a8e-982da1b05c0c" />

12. work with large file:
STRSEU SRCFILE(dbrxdata/QCLSRC) SRCMBR(MYRSQL) TYPE(SQL)

RUNSQLSTM SRCFILE(dbrxdata/QCLSRC) SRCMBR(MYRSQL)

STRSQL
