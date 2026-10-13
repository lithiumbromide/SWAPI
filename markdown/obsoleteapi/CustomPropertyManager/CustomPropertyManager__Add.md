---
title: "CustomPropertyManager::Add"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomPropertyManager/CustomPropertyManager__Add.htm"
---

# CustomPropertyManager::Add

This method is obsolete and has been superseded by [CustomPropertyManager::Add2](sldworksAPI.chm::/CustomPropertyManager/CustomPropertyManager__Add2.htm).

Description

This method adds a custom property to a weldment or sub-weldment.

Syntax (OLE Automation)

retval = CustomPropertyManager.Add ( FieldName, FieldType, FieldValue)

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Input: | (BSTR) FieldType | Type of custom property (see Remarks ) |
| Input: | (BSTR) FieldValue | Value of custom property |
| Output: | (long*) retval | 1 if custom property is added, 0 if not |

Syntax (COM)

status = CustomPropertyManager->Add ( FieldName, FieldType, FieldValue, &retval)

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Input: | (BSTR) FieldType | Type of custom property (see Remarks ) |
| Input: | (BSTR) FieldValue | Value of custom property |
| Output: | (long*) retval | 1 if custom property is added, 0 if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

FieldType can be one of the following:

- "Text"
- "Date"
- "Number"
- "Yes or no"
