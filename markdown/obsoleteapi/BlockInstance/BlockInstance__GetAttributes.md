---
title: "BlockInstance::GetAttributes"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockInstance/BlockInstance__GetAttributes.htm"
---

# BlockInstance::GetAttributes

This method is obsolete and has been superseded by [SketchBlockInstance::GetAttributes](sldworksAPI.chm::/SketchBlockInstance/SketchBlockInstance__GetAttributes.htm).

Description

This method gets the attributes for the block.

Syntax (OLE Automation)

retval = BlockInstance.GetAttributes ( )

| Output: | (VARIANT) retval | Attributes for the block |
| --- | --- | --- |

Syntax (COM)

status = BlockInstance->IGetAttributes ( numAttribs, retval )

| Input: | (long) numAttribs | Number of attributes for the block |
| --- | --- | --- |
| Output: | (LPNOTE*) retval | Array of attributes for the block of size numAttribs |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns all notes that are attributes. Attributes are notes that have tag names and are not read-only.
