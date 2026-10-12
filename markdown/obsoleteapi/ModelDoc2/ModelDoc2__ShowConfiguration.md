---
title: "ModelDoc2::ShowConfiguration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__ShowConfiguration.htm"
---

# ModelDoc2::ShowConfiguration

This method is obsolete and has been superseded by [ModelDoc2::ShowConfiguration2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ShowConfiguration2.htm).

Description

This method displays the named configuration.

NOTE: Configurations save certain display characteristics with each of the assembly components. This method retrieves a previously saved configuration.

Syntax (OLE Automation)

retval = ModelDoc2.ShowConfiguration ( configurationName)

| Input: | (BSTR) configurationName | Name of the configuration to display |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the configuration is activated successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->ShowConfiguration ( configurationName )

| Input: | (BSTR) configurationName | Name of the configuration to display |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
