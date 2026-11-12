---
title: "BlockDefinition::GetBlockInstances"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockDefinition/BlockDefinition__GetBlockInstances.htm"
---

# BlockDefinition::GetBlockInstances

This method is obsolete and has been superseded by [SketchBlockDefinition::GetInstances](sldworksAPI.chm::/SketchBlockDefinition/SketchBlockDefinition__GetInstances.htm).

Description

This method gets the block instances using this definition.

Syntax (OLE Automation)

retval = BlockDefinition.GetBlockInstances ( )

| Output: | (VARIANT) retval | Array of block instances that use this definition |
| --- | --- | --- |

Syntax (COM)

status = BlockDefinition->IGetBlockInstances ( Count, retval )

| Input: | (long) Count | Number of block instances that use this definition |
| --- | --- | --- |
| Output: | (LPBLOCKINSTANCE*) retval | Array of block instances of size Count |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
