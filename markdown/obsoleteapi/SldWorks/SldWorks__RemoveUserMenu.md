---
title: "SldWorks::RemoveUserMenu"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__RemoveUserMenu.htm"
---

# SldWorks::RemoveUserMenu

This method is obsolete and has been superseded by [SldWorks::RemoveMenu](sldworksAPI.chm::/SldWorks/SldWorks__RemoveMenu.htm).

Description

This method removes the menu item or shortcut menu associated with the specified unique menu ID. By specifying the menu ID, you can remove a blank menu item.

Syntax (OLE Automation)

retval = SldWorks.RemoveUserMenu ( docType, menuIdIn, moduleName )

| Input: | (long) docType | Type of document to which this menu item had been added |
| --- | --- | --- |
| Input: | (long) menuIdIn | The ID of the menu item to remove; this menu ID is the same ID returned from your call to SldWorks::AddMenuItem2 or SldWorks::AddMenuPopupItem |
| Input: | (BSTR) moduleName | Name of the module (for example, USERDLL) |
| Return: | (VARIANT_BOOLEAN) retval | TRUE if successful, FALSE if unsuccessful |

Syntax (COM)

status = SldWorks->RemoveUserMenu ( docType, menuIdIn, moduleName, &retval )

| Input: | (long) docType | Type of document to which this menu item had been added |
| --- | --- | --- |
| Input: | (long) menuIdIn | The ID of the menu item to remove; this menu ID is the same ID returned from your call to SldWorks::AddMenuItem2 or SldWorks::AddMenuPopupItem |
| Input: | (BSTR) moduleName | Name of the module (for example, USERDLL) |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if unsuccessful |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
