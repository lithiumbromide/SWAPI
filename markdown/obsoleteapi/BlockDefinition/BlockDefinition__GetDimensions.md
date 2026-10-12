---
title: "BlockDefinition::GetDimensions"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockDefinition/BlockDefinition__GetDimensions.htm"
---

# BlockDefinition::GetDimensions

This method is obsolete and has been superseded by [SketchBlockDefinition::GetDisplayDimensions](sldworksAPI.chm::/SketchBlockDefinition/SketchBlockDefinition__GetDisplayDimensions.htm).

Description

This method gets the displayed dimensions for the block definition.

Syntax (OLE Automation)

retval = BlockDefinition.GetDimensions ( )

| Output: | (VARIANT) retval | Displayed dimensions in the block definition |
| --- | --- | --- |

Syntax (COM)

status = BlockDefinition->IGetDimensions ( numDimensions, retval )

| Input: | (long) numDimensions | Number of displayed dimensions in the block definition |
| --- | --- | --- |
| Output: | (LPDISPLAYDIMENSION*) retval | Array of displayed dimensions of size numDimensions |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
