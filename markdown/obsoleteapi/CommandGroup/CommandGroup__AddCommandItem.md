---
title: "CommandGroup::AddCommandItem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CommandGroup/CommandGroup__AddCommandItem.htm"
---

# CommandGroup::AddCommandItem

This method is obsolete and has been superseded by [CommandGroup::AddCommandItem2](sldworksAPI.chm::/CommandGroup/CommandGroup__AddCommandItem2.htm).

Description

This method adds a combination menu and toolbar item to a CommandGroup.

Syntax (OLE Automation)

*CmdIndex = CommandGroup.AddCommandItem ( Name, Position, HintString, ToolTip, ImageListIndex, CallbackFunction, EnableMethod, userID)

| Input: | (BSTR) Name | Name of the item to add to the CommandGroup |
| --- | --- | --- |
| Input: | (long) Position | Position of the item within the CommandGroup NOTE: Specify 0 to add this item to the beginning of the CommandGroup, or specify -1 to add it to the end of the CommandGroup. This argument specifies the position of the item in relation to its immediate parent item. |
| Input: | (BSTR) HintString | Text displayed in the SolidWorks status bar when the pointer is on the item |
| Input: | (BSTR) ToolTip | ToolTip displayed when the pointer is on the item |
| Input: | (long) ImageListIndex | Index number of the image for the item in the parent CommandGroup (see Remarks ) |
| Input: | (BSTR) CallbackFunction | Function to call when this item is selected |
| Input: | (BSTR) EnableMethod | Optional function that controls the state of the item; if specified, then SolidWorks calls this function before displaying the item If your method returns... Then the SolidWorks software... 0 Deselects and disables the item 1 Deselects and enables the item; this is the default state if no update function is specified 2 Selects and disables the item 3 Selects and enables the item |
| If your method returns... | Then the SolidWorks software... |  |
| 0 | Deselects and disables the item |  |
| 1 | Deselects and enables the item; this is the default state if no update function is specified |  |
| 2 | Selects and disables the item |  |
| 3 | Selects and enables the item |  |
| Input: | (long) userID | User-defined command ID or 0 if not used |
| Output: | (long ) *CmdIndex | Index of the item within the CommandGroup as assigned by SolidWorks |

Syntax (COM)

status = CommandGroup->AddCommandItem ( Name, Position, HintString, ToolTip, ImageListIndex, CallbackFunction, EnableMethod, userID, &CmdIndex)

| Input: | (BSTR) Name | Name of the item to add to the CommandGroup |
| --- | --- | --- |
| Input: | (long) Position | Position of the item within the CommandGroup NOTE: Specify 0 to add this item to the beginning of the CommandGroup, or specify -1 to add this item to the end of the CommandGroup. This argument specifies the position of the item in relation to its immediate parent item. |
| Input: | (BSTR) HintString | Text displayed in the SolidWorks status bar when the pointer is on the item |
| Input: | (BSTR) ToolTip | ToolTip displayed when the pointer is on the item |
| Input: | (long) ImageListIndex | Index number of the image for the item in the parent CommandGroup (see Remarks ) |
| Input: | (BSTR) CallbackFunction | Function to call when this item is selected |
| Input: | (BSTR) EnableMethod | Optional function that controls the state of the item; if specified, then SolidWorks calls this function before displaying the item If your method returns... Then the SolidWorks software... 0 Deselects and disables the item 1 Deselects and enables the item; this is the default state if no update function is specified 2 Selects and disables the item 3 Selects and enables the item |
| If your method returns... | Then the SolidWorks software... |  |
| 0 | Deselects and disables the item |  |
| 1 | Deselects and enables the item; this is the default state if no update function is specified |  |
| 2 | Selects and disables the item |  |
| 3 | Selects and enables the item |  |
| Input: | (long) userID | User-defined command ID or 0 if not used |
| Output: | (long ) *CmdIndex | Index of the item within the CommandGroup as assigned by SolidWorks |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

ImageListIndex is 0-based. The size of the index is equal to number of the images in the large or small bitmap file for that CommandGroup. See CommandGroup::LargeIcontList and CommandGroup::SmallIconList for details.
