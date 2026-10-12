---
title: "CommandGroup::AddSpacer"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CommandGroup/CommandGroup__AddSpacer.htm"
---

# CommandGroup::AddSpacer

This method is obsolete and has been superseded by [CommandGroup::AddSpace2](sldworksAPI.chm::/CommandGroup/CommandGroup__AddSpacer2.htm).

Description

This method adds a spacer between items in a CommandGroup.

Syntax (OLE Automation)

*CmdIndex = CommandGroup.AddSpacer ( Position)

| Input: | (long) Position | Position of the spacer within the CommandGroup NOTE: Specify 0 to add this a spacer to the beginning of the CommandGroup, or specify -1 to add it to the end of the CommandGroup. This argument specifies the position of the spacer in relation to its immediate parent item. |
| --- | --- | --- |
| Output: | (long ) *CmdIndex | Index of the item within the CommandGroup as assigned by SolidWorks |

Syntax (COM)

status = CommandGroup->AddSpacer ( Position, &CmdIndex)

| Input: | (long) Position | Position of the spacer within the CommandGroup NOTE: Specify 0 to add this a spacer to the beginning of the CommandGroup, or specify -1 to add it to the end of the CommandGroup. This argument specifies the position of the spacer in relation to its immediate parent item. |
| --- | --- | --- |
| Output: | (long ) *CmdIndex | Index of the item within the CommandGroup as assigned by SolidWorks |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
