---
title: "ModelDoc2::DeleteCustomInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__DeleteCustomInfo.htm"
---

# ModelDoc2::DeleteCustomInfo

This method is obsolete and has been superseded by [ModelDoc2::DeleteCustomInfo2](ModelDoc2__DeleteCustomInfo2.htm).

Description

This method deletes a custom info field that has been defined for the document.

Syntax (OLE Automation)

FieldType = ModelDoc2.DeleteCustomInfo( FieldName )

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if deleted, FALSE if not |

Syntax (COM)

status = ModelDoc2->DeleteCustomInfo( FieldName, &retval)

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if deleted, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
