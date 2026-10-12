---
title: "SldWorks::AddMenuItem2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__AddMenuItem2.htm"
---

# SldWorks::AddMenuItem2

This method is obsolete and has been superseded by [SldWorks::AddMenuItem3](sldworksAPI.chm::/SldWorks/SldWorks__AddMenuItem3.htm).

Description

This method adds a menu item to the SolidWorks interface.

Syntax (OLE Automation)

IsMenuItemAdded = SldWorks.AddMenuItem2 ( DocumentType, Cookie, MenuItem, Position, MenuCallback, MenuEnableMethod, HintString )

| Input: | (long) DocumentType | Document type to which to add the menu item |
| --- | --- | --- |
| Input: | (long) Cookie | Identifier of the menu as defined in swMenuIdentifiers_e; this is the same Cookie that you specified in SwAddin::ConnectToSW |
| Input: | (BSTR) MenuItem | Menu string ("menuItem@subMenuString@menuString"); SolidWorks creates menus and submenus only if they do not already exist. |
| Input: | (long) Position | Position at which to add the new menu item The first item is at position 0; if Position is –1, the new menu item is added to the bottom of the list; this argument specifies the position of the menu item in relation to its immediate parent menu |
| Input: | (BSTR) MenuCallback | Function to call when this menu item is selected |
| Input: | (BSTR) MenuEnableMethod | Optional function that controls the state of the menu item If specified, SolidWorks: Calls this function before displaying the menu Display of the menu item is controlled by the return value of MenuEnableMethod If your method returns... Then the SolidWorks softeware... 0 Deselects and disables the menu item 1 Deselects and enables the menu item; this is the default menu state with if no update function is specified 2 Selects and disables the menu item 3 Selects and enables the menu item |
| If your method returns... | Then the SolidWorks softeware... |  |
| 0 | Deselects and disables the menu item |  |
| 1 | Deselects and enables the menu item; this is the default menu state with if no update function is specified |  |
| 2 | Selects and disables the menu item |  |
| 3 | Selects and enables the menu item |  |
| Input: | (BSTR) HintString | Text to show in the SolidWorks status bar when the user moves their mouse over this menu item; if you specify a HintString, it must be preceded by a comma |
| Output: | (VARIANT_BOOL) IsMenuItemAdded | 1 if menu item was successfully added, 0 if failure |

Syntax (COM)

status = SldWorks->AddMenuItem2 ( DocumentType, Cookie, MenuItem, Position, MenuCallback, MenuEnableMethod, HintString, &IsMenuItemAdded )

| Input: | (long) DocumentType | Document type to which to add the menu item |
| --- | --- | --- |
| Input: | (long) Cookie | Identifier of the menu as defined in swMenuIdentifiers_e; this is the same Cookie that you specified in SwAddin::ConnectToSW |
| Input: | (BSTR) MenuItem | Menu string ("menuItem@subMenuString@menuString"); SolidWorks creates menus and submenus only if they do not already exist |
| Input: | (long) Position | Position at which to add the new menu item The first item is at position 0; if Position is –1, the new menu item is added to the bottom of the list; this argument specifies the position of the menu-item in relation to its immediate parent menu |
| Input: | (BSTR) MenuCallback | Function to call when this menu item is selected |
| Input: | (BSTR) MenuEnableMethod | Optional function that controls the state of the menu item If specified, SolidWorks: Calls this function before displaying the menu Display of the menu item is controlled by the return value of MenuEnableMethod If your method returns... Then SolidWorks... 0 Deselects and disables the menu item. 1 Deselects and enables the menu item; This is the default menu state with if no update function is specified 2 Selects and disables the menu item 3 Selects and enables the menu item |
| If your method returns... | Then SolidWorks... |  |
| 0 | Deselects and disables the menu item. |  |
| 1 | Deselects and enables the menu item; This is the default menu state with if no update function is specified |  |
| 2 | Selects and disables the menu item |  |
| 3 | Selects and enables the menu item |  |
| Input: | (BSTR) HintString | Text to show in the SolidWorks status bar when the user moves their mouse over this menu item; if you specify a HintString, it must be preceded by a comma |
| Output: | (VARIANT_BOOL) IsMenuItemAdded | 1 if menu item was successfully added, 0 if failure |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For information about using this method with the SwAddin object, see Using SwAddin to Create a SolidWorks Add-in.

You can add a new menu to any one of the four SolidWorks frames (main, part, assembly, or drawing). To do this, call this method with the appropriate argument in the DocumentType parameter. For example, if you want your menu to be available when a part document is active, then call this method and pass swDocPART as the first argument. After you have added your menu to the part frame, you do not need to do it again during the current SolidWorks session. Once a part document is activated by the user, SolidWorks automatically displays your menu option.

To add a menu separator, specify an empty string for HintString:

```vb
' Adds a menu separator
 bRet = iSldWorks.AddMenuItem2(swDocNONE, iCookie, "@Sample", -1, "DocNONE_Item", "", "")
```
