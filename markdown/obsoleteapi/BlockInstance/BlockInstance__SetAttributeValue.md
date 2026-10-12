---
title: "BlockInstance::SetAttributeValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockInstance/BlockInstance__SetAttributeValue.htm"
---

# BlockInstance::SetAttributeValue

This method is obsolete and has been superseded by [SketchBlockInstance::SetAttributeValue](sldworksAPI.chm::/SketchBlockInstance/SketchBlockInstance__SetAttributeValue.htm).

Description

This method sets the value of the specified attribute for the block instance.

Syntax (OLE Automation)

retval = BlockInstance.SetAttributeValue ( tagName, value )

| Input: | (BSTR) tagName | Specified attribute |
| --- | --- | --- |
| Input: | (BSTR) value | Value to which to set attribute |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |

Syntax (COM)

status = BlockInstance->SetAttributeValue ( tagName, value, &retval )

| Input: | (BSTR) tagName | Specified attribute |
| --- | --- | --- |
| Input: | (BSTR) value | Value to which to set attribute |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
