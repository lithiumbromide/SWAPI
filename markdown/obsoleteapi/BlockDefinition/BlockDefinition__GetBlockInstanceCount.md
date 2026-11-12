---
title: "BlockDefinition::GetBlockInstanceCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockDefinition/BlockDefinition__GetBlockInstanceCount.htm"
---

# BlockDefinition::GetBlockInstanceCount

This method is obsolete and has been superseded by [SketchBlockDefinition::GetInstanceCount](sldworksAPI.chm::/SketchBlockDefinition/SketchBlockDefinition__GetInstanceCount.htm).

Description

This method gets the number of block instances that use this definition.

Syntax (OLE Automation)

retval = BlockDefinition.GetBlockInstanceCount ( )

| Output: | (long) retval | Number of block instances that use this definition |
| --- | --- | --- |

Syntax (COM)

status = BlockDefinition->GetBlockInstanceCount ( &retval )

| Output: | (long) retval | Number of block instances that use this definition |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
