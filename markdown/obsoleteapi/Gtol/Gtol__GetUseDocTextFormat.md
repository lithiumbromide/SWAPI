---
title: "Gtol::GetUseDocTextFormat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Gtol/Gtol__GetUseDocTextFormat.htm"
---

# Gtol::GetUseDocTextFormat

This method is obsolete and has been superseded by [Annotation::GetUseDocTextFormat](sldworksAPI.chm::/Annotation/Annotation__GetUseDocTextFormat.htm).

Description

This method gets whether or not this Gtol is currently using the document default Gtol text format.

Syntax (OLE Automation)

retval = Gtol.GetUseDocTextFormat ( )

| Return: | (BOOL) retval | TRUE if the documents text formatting is used, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = Gtol->GetUseDocTextFormat ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if the documents text formatting is used, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |
