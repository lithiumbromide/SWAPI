---
title: "ModelDoc::DeleteCustomInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DeleteCustomInfo.htm"
---

# ModelDoc::DeleteCustomInfo

This method is obsolete and has been superseded by [ModelDoc2::DeleteCustomInfo](../ModelDoc2/ModelDoc2__DeleteCustomInfo.htm).

Description

This method deletes a custom property field that has been defined for the document.

Syntax (OLE Automation)

FieldType = ModelDoc.DeleteCustomInfo( FieldName )

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if deleted, FALSE if not |

Syntax (COM)

status = ModelDoc->DeleteCustomInfo( FieldName, &retval)

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if deleted, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
