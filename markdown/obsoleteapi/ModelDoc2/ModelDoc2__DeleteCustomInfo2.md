---
title: "ModelDoc2::DeleteCustomInfo2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__DeleteCustomInfo2.htm"
---

# ModelDoc2::DeleteCustomInfo2

This method is obsolete and has been superseded by [ModelDocExtension::CustomPropertyManager](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__CustomPropertyManager.htm).

Description

This method deletes custom information that has been defined for the document or the specified configuration.

Syntax (OLE Automation)

retval = ModelDoc2.DeleteCustomInfo2( configuration, FieldName )

| Input: | (BSTR) configuration | Name of the configuration (see Remarks ) |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of custom information |
| Return: | (BOOL) retval | TRUE if deleted, FALSE if not |

Syntax (COM)

status = ModelDoc2->DeleteCustomInfo2( configuration, FieldName, &retval)

| Input: | (BSTR )configuration | Name of the configuration (see Remarks ) |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of custom information |
| Output: | (VARIANT_BOOL) retval | TRUE if deleted, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The configuration name should be the name of a configuration in the document. If the custom information is found in the specified configuration, then this method deletes that custom information. If the name is an empty string, then this method deletes the custom information from the document.
