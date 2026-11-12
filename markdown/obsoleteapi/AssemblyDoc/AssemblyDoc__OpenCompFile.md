---
title: "AssemblyDoc::OpenCompFile"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__OpenCompFile.htm"
---

# AssemblyDoc::OpenCompFile

This method is obsolete and has been superseded by [SldWorks::ActivateDoc2](sldworksAPI.chm::/SldWorks/SldWorks__ActivateDoc2.htm) and [SldWorks::OpenDoc7](sldworksAPI.chm::/SldWorks/SldWorks__OpenDoc7.htm).

NOTE: If SldWorks::ActivateDoc2 fails because the component is not resolved and unsuppressed, then use SldWorks::OpenDoc7.

Description

This method opens the selected assembly component file.

Syntax (OLE Automation)

void AssemblyDoc.OpenCompFile ()

Syntax (COM)

status = AssemblyDoc->OpenCompFile ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

SolidWorks loads the selected component file or makes it the active document if it is already loaded.
