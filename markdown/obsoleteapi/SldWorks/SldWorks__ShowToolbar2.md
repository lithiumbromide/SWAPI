---
title: "SldWorks::ShowToolbar2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__ShowToolbar2.htm"
---

# SldWorks::ShowToolbar2

This method is obsolete. SolidWorks manages the display of the toolbars based on the user's action; therefore, this method is not needed. There are no alternative methods available to use.

Description

This method displays a toolbar that was created with SldWorks::AddToolbar3.

Syntax (OLE Automation)

Status = SldWorks.ShowToolbar2 ( Cookie, ToolbarID )

| Input: | (long) Cookie | Resource ID of the toolbar; this is the same cookie that you specified in SwAddin::ConnectToSW |
| --- | --- | --- |
| Input: | (long) ToolbarID | Toolbar ID |
| Output: | (VARIANT_BOOL) Status | TRUE if successful, FALSE if unsuccessful |

Syntax (COM)

status = SldWorks->ShowToolbar2 ( Cookie, ToolbarID, &Status )

| Input: | (long) Cookie | Resource ID of the toolbar; this is the same cookie that you specified in SwAddin::ConnectToSW |
| --- | --- | --- |
| Input: | (long) ToolbarID | Toolbar ID |
| Output: | (VARIANT_BOOL) Status | TRUE if successful, FALSE if unsuccessful |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For information about using this method with the SwAddin object, see Using SwAddin to Create a SolidWorks Add-in.
