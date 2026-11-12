---
title: "CustomPropertyManager::GetType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomPropertyManager/CustomPropertyManager__GetType.htm"
---

# CustomPropertyManager::GetType

This method is obsolete and has been superseded by [CustomPropertyManager::GetType2](sldworksAPI.chm::/CustomPropertyManager/CustomPropertyManager__GetType2.htm).

Description

This method gets the type of the specified custom property.

Syntax (OLE Automation)

retval = CustomPropertyManager.GetType ( FieldName)

| Input: | (BSTR) FieldName | Name of the custom property whose type to get |
| --- | --- | --- |
| Output: | (BSTR*) retval | Type of custom property |

Syntax (COM)

status = CustomPropertyManager->GetType ( FieldName, &retval)

| Input: | (BSTR) FieldName | Name of the custom property whose type to get |
| --- | --- | --- |
| Output: | (BSTR*) retval | Type of custom property |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Type can be one of the following:

- "Text"
- "Date"
- "Number"
- "Yes or no"
