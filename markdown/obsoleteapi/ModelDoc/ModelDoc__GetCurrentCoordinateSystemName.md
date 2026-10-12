---
title: "ModelDoc::GetCurrentCoordinateSystemName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetCurrentCoordinateSystemName.htm"
---

# ModelDoc::GetCurrentCoordinateSystemName

This method is obsolete and has been superseded by [ModelDoc2::GetCurrentCoordinateSystemName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetCurrentCoordinateSystemName.htm).

Description

This method returns the name of the current coordinate system or an empty string for the default coordinate system.

Syntax (OLE Automation)

Name = ModelDoc.GetCurrentCoordinateSystemName( )

| Return: | (BSTR) Name | Name of the current coordinate system |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetCurrentCoordinateSystemName( &Name )

| Output: | (BSTR) Name | Name of the current coordinate system |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The current coordinate system may be set by the user in the Save As dialog and in the Tools, Measure dialog.
