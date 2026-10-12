---
title: "DisplayDimension::GetUseDocTextFormat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetUseDocTextFormat.htm"
---

# DisplayDimension::GetUseDocTextFormat

This method is obsolete and has been superseded by [Annotation::GetUseDocTextFormat](sldworksAPI.chm::/Annotation/Annotation__GetUseDocTextFormat.htm).

Description

This method gets whether or not the default dimension text format is used in this document.

Syntax (OLE Automation)

retval = DisplayDimension.GetUseDocTextFormat ( )

| Return: | (BOOL)retval | TRUE if the documents text formatting is used, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = DisplayDimension->GetUseDocTextFormat ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if the documents text formatting is used, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
