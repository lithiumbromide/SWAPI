---
title: "ModelDoc::DeleteCustomInfo2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DeleteCustomInfo2.htm"
---

# ModelDoc::DeleteCustomInfo2

This method is obsolete and has been superseded by [ModelDoc2::DeleteCustomInfo2](../ModelDoc2/ModelDoc2__DeleteCustomInfo2.htm).

Description

This method deletes a custom property field that has been defined for the document or the specified configuration.

Syntax (OLE Automation)

retval = ModelDoc.DeleteCustomInfo2( configuration, FieldName )

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of custom property |
| Return: | (BOOL) retval | TRUE if deleted, FALSE if not |

Syntax (COM)

status = ModelDoc->DeleteCustomInfo2( configuration, FieldName, &retval)

| Input: | (BSTR)configuration | Name of the configuration |
| --- | --- | --- |
| Input: | (BSTR)FieldName | Name of custom property |
| Output: | (VARIANT_BOOL)retval | TRUE if deleted, FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The configuration name should be the name of one configuration in the document. If the custom property is found on the given configuration, then this method deletes that custom property. If this name is an empty string, then this method attempts to delete the custom property from the document.
