---
title: "ModelDoc::ShowConfiguration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ShowConfiguration.htm"
---

# ModelDoc::ShowConfiguration

This method is obsolete and has been superseded by [ModelDoc::ShowConfiguration2](ModelDoc__ShowConfiguration2.htm).

Description

This method displays the named configuration. Configurations allow you to save certain display characteristics with each of the assembly components and then retrieve that configuration at some point in the future. This method allows you to retrieve a previously saved configuration.

Syntax (OLE Automation)

retval = ModelDoc.ShowConfiguration ( configurationName)

| Input: | (BSTR) configurationName | Name of the configuration to display |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the configuration was activated successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc->ShowConfiguration ( configurationName )

| Input: | (BSTR) configurationName | Name of the configuration to display |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the configuration was activated successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
