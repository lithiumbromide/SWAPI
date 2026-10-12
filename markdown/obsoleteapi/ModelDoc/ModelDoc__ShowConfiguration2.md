---
title: "ModelDoc::ShowConfiguration2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ShowConfiguration2.htm"
---

# ModelDoc::ShowConfiguration2

This method is obsolete and has been superseded by [ModelDoc2::ShowConfiguration2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ShowConfiguration2.htm).

Description

This method displays the named configuration. Configurations allow you to save certain display characteristics with each of the assembly components and then retrieve that configuration at some point in the future. This method allows you to retrieve a previously saved configuration.

Syntax (OLE Automation)

retval = ModelDoc.ShowConfiguration2 ( configurationName)

| Input: | (BSTR) configurationName | Name of the configuration to display |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the configuration was activated successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc->ShowConfiguration2 ( configurationName, &retval )

| Input: | (BSTR) configurationName | Name of the configuration to display |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the configuration was activated successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
