---
title: "SldWorks::ShowToolbar"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__ShowToolbar.htm"
---

# SldWorks::ShowToolbar

This method is obsolete. SolidWorks manages the display of the toolbars based on the user's action; therefore, this method is not needed. There are no alternative methods available to use.

Description

This method displays a toolbar that was created with SldWorks::AddToolbar.

Syntax (OLE Automation)

retval = SldWorks.ShowToolbar ( moduleName, toolbarId )

| Input: | (BSTR) moduleName | Name of the module (that is, USERDLL) |
| --- | --- | --- |
| Input: | (long) toolbarId | Toolbar ID |
| Return: | (VARIANT_BOOL)retval | TRUE if successful, FALSE if unsuccessful |

Syntax (COM)

status = SldWorks->ShowToolbar ( moduleName, toolbarId, &retval )

| Input: | (BSTR)moduleName | Name of the module (that is, USERDLL) |
| --- | --- | --- |
| Input: | (long)toolbarId | Toolbar ID |
| Output: | (VARIANT_BOOL)retval | TRUE if successful, FALSE if unsuccessful |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
