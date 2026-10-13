---
title: "Configuration::GetCustomProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Configuration/Configuration__GetCustomProperties.htm"
---

# Configuration::GetCustomProperties

This method is obsolete and has been superseded by [Configuration::CustomPropertyManager](sldworksAPI.chm::/Configuration/Configuration__CustomPropertyManager.htm).

Description

This method gets all of the custom properties in this configuration.

Syntax (OLE Automation)

numProps = Configuration.GetCustomProperties ( propNames, propValues, propTypes )

| Output: | (VARIANT) propNames | Array of property names |
| --- | --- | --- |
| Output: | (VARIANT) propValues | Array of property values |
| Output: | (VARIANT) propTypes | Array of property types as defined in swCustomInfoType_e |
| Output: | (long) numProps | Number of properties |

Syntax (COM)

status = Configuration->IGetCustomProperties ( numProps, &propNames, &propValues, &propTypes )

| Input: | (long) numProps | Number of properties |
| --- | --- | --- |
| Output: | (BSTR*) propNames | Pointer to an array of property names |
| Output: | (BSTR*) propValues | Pointer to an array of property values |
| Output: | (long*) propTypes | Pointer to an array of property types as defined in swCustomInfoType_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
