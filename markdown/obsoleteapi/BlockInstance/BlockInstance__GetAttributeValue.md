---
title: "BlockInstance::GetAttributeValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockInstance/BlockInstance__GetAttributeValue.htm"
---

# BlockInstance::GetAttributeValue

This method is obsolete and has been superseded by [SketchBlockInstance::GetAttributeValue](sldworksAPI.chm::/SketchBlockInstance/SketchBlockInstance__GetAttributeValue.htm).

Description

This method gets the value of the specified attribute for the block instance.

Syntax (OLE Automation)

value = BlockInstance.GetAttributeValue ( tagName )

| Input: | (BSTR) tagName | Tag name of this attribute |
| --- | --- | --- |
| Output: | (BSTR) value | Value of the attribute |

Syntax (COM)

status = BlockInstance->GetAttributeValue ( tagName, &value )

| Input: | (BSTR) tagName | Tag name of this attribute |
| --- | --- | --- |
| Output: | (BSTR) value | Value of the attribute |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns the string value of an attribute. (Attributes are notes that have tag names and are not read-only.)
