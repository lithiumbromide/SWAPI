---
title: "ModelDoc::GetConfigurationByName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetConfigurationByName.htm"
---

# ModelDoc::GetConfigurationByName

This method is obsolete and has been superseded by [ModelDoc2::GetConfigurationByName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetConfigurationByName.htm).

Description

This function returns the Configuration object based on the specified configuration name.

Syntax (OLE Automation)

retval = ModelDoc.GetConfigurationByName ( name )

| Input: | (BSTR) name | Name of the configuration |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the specified Configuration object; this value is NULL if the operation fails |

Syntax (COM)

status = ModelDoc->IGetConfigurationByName ( name, &retval )

| Input: | (BSTR) name | Name of the configuration |
| --- | --- | --- |
| Output: | (LPCONFIGURATION) retval | Pointer to the specified Configuration object; this value is NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If the specified configuration has not been activated, then certain data may be unavailable. For example, attempting to traverse assembly components for a configuration that has not been activated results in a NULL root component being returned from Configuration::GetRootComponent. However, the Configuration object returned is useful for obtaining data that is stored with the Configuration object, such as, the AlternateName value. The specified configuration does not have to be activated to obtain this type of stored information.
