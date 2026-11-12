---
title: "ModelDoc::IRelease3rdPartyStorage"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__IRelease3rdPartyStorage.htm"
---

# ModelDoc::IRelease3rdPartyStorage

This method is obsolete and has been superseded by [ModelDoc2::IRelease3rdPartyStorage](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IRelease3rdPartyStorage.htm).

Description

This method closes the specified storage stream.

Syntax (OLE Automation)

Not Available.

Syntax (COM)

status = ModelDoc-> IRelease3rdPartyStorage( stringIn )

| Input: | (BSTR) stringIn | Name of the storage stream to close |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use this method with [ModelDoc::IGet3rdPartyStorage](ModelDoc__IGet3rdPartyStorage.htm) f you are not using the LoadFromStorageNotify event. You need must call this method even when the call to ModelDoc::IGet3rdPartyStorage returns a NULL stream. For more information, see ModelDoc::IGet3rdPartyStorage.

NOTE: If you are using serialization, then you should be careful with the standard MFC macros; otherwise, you might get messages like Unexpected File Format after your application is unloaded. One way of using IMPLEMENT_SERIAL is:

IMPLEMENT_SERIAL( CCustomAttr, CObject, VERSIONABLE_SCHEMA|0 )
