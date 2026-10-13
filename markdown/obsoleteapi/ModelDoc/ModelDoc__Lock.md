---
title: "ModelDoc::Lock"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__Lock.htm"
---

# ModelDoc::Lock

This method is obsolete and has been superseded by [ModelDoc2::Lock](sldworksAPI.chm::/ModelDoc2/ModelDoc2__Lock.htm).

Description

This method blocks the modifying commands in the user interface, effectively locking the application. This method also changes text on the status bar to Processing….

Syntax (OLE Automation)

void ModelDoc.Lock ()

Syntax (COM)

status = ModelDoc->Lock ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

Use this method with ModelDoc::UnLock .
