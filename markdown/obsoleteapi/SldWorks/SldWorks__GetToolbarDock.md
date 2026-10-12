---
title: "SldWorks::GetToolbarDock"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__GetToolbarDock.htm"
---

# SldWorks::GetToolbarDock

This method is obsolete and has been superseded by [SldWorks::GetToolbarDock2](sldworksAPI.chm::/SldWorks/SldWorks__GetToolbarDock2.htm).

Description

This method obtains the docking state of the toolbar.

Syntax (OLE Automation)

DockState = SldWorks.GetToolbarDock ( Module, ToolbarID )

| Input: | (BSTR) Module | Name of the module (for example, USERDLL) |
| --- | --- | --- |
| Input: | (long) ToolbarID | ID of the toolbar |
| Return: | (long) DockState | Docking state of the toolbar as defined in swToolbarDockStatePosition_e |

Syntax (COM)

status = SldWorks->GetToolbarDock ( Module, ToolbarID, &DockState )

| Input: | (BSTR) Module | Name of the module (for example, USERDLL) |
| --- | --- | --- |
| Input: | (long) ToolbarID | ID of the toolbar |
| Output: | (long) DockState | Docking state of the toolbar as defined in swToolbarDockStatePosition_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
