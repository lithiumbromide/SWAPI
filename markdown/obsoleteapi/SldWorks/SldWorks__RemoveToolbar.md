---
title: "SldWorks::RemoveToolbar"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__RemoveToolbar.htm"
---

# SldWorks::RemoveToolbar

This method is obsolete and has been superseded by [SldWorks::RemoveToolbar2](sldworksAPI.chm::/SldWorks/SLDWORKS__REMOVETOOLBAR2.HTM).

Description

This method removes a toolbar that was created with SldWorks::AddToolbar.

Syntax (OLE Automation)

retval = SldWorks.RemoveToolbar ( Module, toolbarId )

| Input: | (BSTR) Module | Name of the module (that is, USERDLL) |
| --- | --- | --- |
| Input: | (long) toolbarId | Toolbar ID |
| Return: | (Boolean)retval | TRUE if successful, FALSE if unsuccessful |

Syntax (COM)

status = SldWorks->RemoveToolbar ( Module, toolbarId, &retval )

| Input: | (BSTR)Module | Name of the module (that is, USERDLL) |
| --- | --- | --- |
| Input: | (long)toolbarId | Toolbar ID |
| Output: | (VARIANT_BOOL)retval | TRUE if successful, FALSE if unsuccessful |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If the SolidWorks application is exiting and your application is still added-in, then you should not call this method. You should, however, clean up all other items such as the Cbitmap objects. Doing so allows your toolbar to get reloaded in the same position when the SolidWorks application is restarted.
