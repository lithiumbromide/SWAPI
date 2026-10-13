---
title: "Write Parasolid Partition Stream to File Example (C++)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Write_Parasolid_Partition_Stream_to_File_Example_CPlusPlus_COM.htm"
---

# Write Parasolid Partition Stream to File Example (C++)

This example shows how to write a Parasolid partition stream to a file using the SOLIDWORKS Document Manager API.

```vb
#import 'C:\Program Files\Common Files\SOLIDWORKS Shared\swdocumentmgr.dll'  raw_interfaces_only, raw_native_types, no_namespace, named_guids //Change as necessary
```

```vb
wchar_t* filename = "87-part.sldprt"
wchar_t* outputDir = "c:\\caddocs\\";

ISwDMClassFactoryPtr swClassFact;
 swClassFact.CreateInstance(
 __uuidof(SwDMClassFactory) );
 if (!(ISwDMClassFactory*)swClassFact)
 return 0;

 ISwDMApplicationPtr swDocMgr(
 swClassFact->GetApplication("your_license_key") ); //Specify your license key
 if (!(ISwDMApplication*)swDocMgr)
 return 0;

 SwDmDocumentOpenError error;
 ISwDMDocumentPtr swDoc( swDocMgr->GetDocument(
 filename, swDmDocumentPart, TRUE, &error ) );
 if (!(ISwDMDocument*)swDoc)
 return 0;

 ISwDMConfigurationMgrPtr swCfgMgr(
 swDoc->ConfigurationManager );
 if (!(ISwDMConfigurationMgr*)swCfgMgr)
 return 0;

 _variant_t names( swCfgMgr->GetConfigurationNames() );
 SAFEARRAY* nameArray = names.parray;
 for (int i=0; i<nameArray->rgsabound[0].cElements; ++i)
 {
 _bstr_t str( ((BSTR*)(nameArray->pvData))[i] );

 ISwDMConfigurationPtr swCfg(
 swCfgMgr->GetConfigurationByName(str) );
 ISwDMConfiguration2* pswCfg2;
 if (swCfg)
swCfg->QueryInterface( __uuidof(ISwDMConfiguration2), (void **)&pswCfg2 );
else
return 0;

 {
 CString dir( outputDir );
 dir += "\\";
 dir += str;
 dir += ".xmp_bin";
 pswCfg2->GetPartitionStream( (LPCTSTR)dir );
 }
 }
```
