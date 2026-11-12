---
title: "SldWorks::RemoveMenuPopupItem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__RemoveMenuPopupItem.htm"
---

# SldWorks::RemoveMenuPopupItem

This method is obsolete and has been superseded by [SldWorks::RemoveMenuPopupItem2](sldworksAPI.chm::/SldWorks/SldWorks__RemoveMenuPopupItem2.htm).

Description

This method removes the specified menu pop-up item. The arguments passed should match the arguments given when this pop-up menu item was created.

Syntax (OLE Automation)

retval = SldWorks.RemoveMenuPopupItem ( DocType, SelectType, Item, CallbackFcnAndModule, CustomNames, Unused)

| Input: | (long) DocType | Document type from which the pop-up menu item is to be removed as defined in swDocumentTypes_e |
| --- | --- | --- |
| Input: | (long) SelectType | Selection type used by the menu item being removed |
| Input: | (BSTR) Item | Description that appears on the pop-up menu being removed |
| Input: | (BSTR) CallbackFcnAndModule | Callback function and module for this menu item as specified when the menu item was added; see Frame::AddMenuPopupItem for details |
| Input: | (BSTR) CustomNames | Semi-colon separated list containing the names of the custom feature types as specified when the menu item was added |
| Input: | (long) Unused | Reserved for future use; pass 0 |
| Return: | (BOOL) retval | TRUE if the menu item is removed successfully, FALSE otherwise |

Syntax (COM)

status = SldWorks->RemoveMenuPopupItem ( DocType, SelectType, Item, CallbackFcnAndModule, CustomNames, Unused, &retval )

| Input: | (long) DocType | Document type from which the pop-up menu item is to be removed as defined in swDocumentTypes_e |
| --- | --- | --- |
| Input: | (long) SelectType | Selection type used by the menu item being removed |
| Input: | (BSTR) Item | Description that appears on the pop-up menu being removed |
| Input: | (BSTR) CallbackFcnAndModule | Callback function and module for this menu item as specified when the menu item was added; see Frame::AddMenuPopupItem for details |
| Input: | (BSTR) CustomNames | Semi-colon separated list containing the names of the custom feature types as specified when the menu item was added |
| Input: | (long) Unused | Reserved for future use; pass 0 |
| Output: | (VARIANT_BOOL) retval | TRUE if the menu item is removed successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The enueration swDocNONE is not valid for DocType.
