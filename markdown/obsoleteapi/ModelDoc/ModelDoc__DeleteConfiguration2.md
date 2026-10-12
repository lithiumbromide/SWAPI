---
title: "ModelDoc::DeleteConfiguration2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DeleteConfiguration2.htm"
---

# ModelDoc::DeleteConfiguration2

This method is obsolete and has been superseded by [ModelDoc2::DeleteConfiguration2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__DeleteConfiguration2.htm).

Description

This method deletes a configuration. The configuration you delete cannot be the active configuration.

Syntax (OLE Automation)

retval = ModelDoc.DeleteConfiguration2 ( configurationName)

| Input: | (BSTR) configurationName | Name of the configuration to delete |
| --- | --- | --- |
| Return: | VARIANT_BOOL retval | TRUE if successfully deleted, FALSE if not |

Syntax (COM)

status = ModelDoc->DeleteConfiguration2 ( configurationName, &retval )

| Input: | (BSTR) configurationName | Name of the configuration to delete |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully deleted, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
