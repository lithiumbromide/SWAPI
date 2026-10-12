---
title: "SldWorks::AddMenuPopupItem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__AddMenuPopupItem.htm"
---

# SldWorks::AddMenuPopupItem

This method is obsolete and has been superseded by [SldWorks::AddMneuPopupItem2](sldworksAPI.chm::/SldWorks/SldWorks__AddMenuPopupItem2.htm).

Description

This mehod adds a menu item or a separator to a shortcut menu (right-mouse button menu). This capability only operates when the application is implemented as a DLL and not as an executable (.exe).

Syntax (OLE Automation)

retval = SldWorks.AddMenuPopupItem ( docType, selType, Item, CallbackFcnAndModule, CustomNames )

| Input: | (long) DocType | Document type to which to add the menu item |
| --- | --- | --- |
| Input: | (long) selType | Selection type to which to add the menu item |
| Input: | (BSTR) Item | Description that appears on the shortcut menu |
| Input: | (BSTR) CallbackFcnAndModule | Function to call when end-user clicks your menu item (see SldWorks::AddMenuItem) |
| Input: | (BSTR) CustomNames | Names of custom feature types |
| Return: | (BOOL) retval | TRUE if menu item is successfully added, FALSE otherwise |

Syntax (COM)

status = SldWorks->AddMenuPopupItem ( docType, selType, Item, CallbackFcnAndModule, CustomNames, &retval )

| Input: | (long) DocType | Document type to which to add the menu item |
| --- | --- | --- |
| Input: | (long) selType | Selection type to which to add the menu item |
| Input: | (BSTR) Item | Description that appears on the shortcut menu |
| Input: | (BSTR) CallbackFcnAndModule | Function to call when end-user clicks your menu item (see SldWorks::AddMenuItem) |
| Input: | (BSTR) CustomNames | Names of custom feature types |
| Output: | (long)retval | TRUE if menu item is successfully added, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To add a separator the Item argument , set to NULL or an empty string.

If the select type is a custom feature (for example, swSelATTRIBUTES), the menu item appears on the shortcut menu only if the custom feature name is included in CustomNames.

If the select type is swSelEVERYTHING, the menu item appears on the shortcut menu of any standard SolidWorks objects. This does not include the shortuct menu of custom features such as attributes.

The CustomNames argument contains a semi-colon separated list containing the names of the custom feature types. This argument is only applicable if SelType is a custom feature type (for example, swSelATTRIBUTES). If swSelATTRIBUTES, then this field should be the name of the attribute definition.
