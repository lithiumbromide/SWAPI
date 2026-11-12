---
title: "SldWorks::AddMenuItem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__AddMenuItem.htm"
---

# SldWorks::AddMenuItem

This method is obsolete and has been superseded by [SldWorks::AddMenuItem2](SldWorks__AddMenuItem2.htm).

Description

This method adds a menu item to the SolidWorks interface.

Syntax (OLE Automation)

retval = SldWorks.AddMenuItem ( docType, menu, position, callbackModuleAndFcn )

| Input: | (long) docType | Document type to which to add the menu item |
| --- | --- | --- |
| Input: | (BSTR) menuItem | Menu string (for example, "menuItem@subMenuString@menuString" ); menus and submenusare created if they do not already exist |
| Input: | (long) Position | Specifies the position at which to add the new menu item; first item is at position 0; if Position is –1, the new menu item is added to the bottom of the list.; this argument specifies the position of the menu item in relation to its immediate parent menu |
| Input: | (BSTR) callbackFcnAndModule | Function to call when end-user clicks the menu item |
| Return: | (long) retval | 1 if menu item is successfully added, 0 if failure |

Syntax (COM)

status = SldWorks->AddMenuItem ( docType, menuItem, position, callbackModuleAndFcn, &retval )

| Input: | (long) docType | Document type to which to add the menu item |
| --- | --- | --- |
| Input: | (BSTR) menuItem | Menu string (for example, "menuItem@subMenuString@menuString" ); menus and submenusare created if they do not already exist |
| Input: | (long) position | Specifies the position at which to add the new menu item; first item is at position 0; if Position is –1, the new menu item is added to the bottom of the list.; this argument specifies the position of the menu item in relation to its immediate parent menu |
| Input: | (BSTR) callbackFcnAndModule | Function to call when end-user clicks the menu item |
| Output: | (long) retval | 1 if menu item is successfully added, 0 if failure |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This capability only operates when your application is implemented as a DLL, not as an executable (.exe). In addition, any function exposed as a callback from a menu item, must be declared as an export or included in your .def file.

You can add a new menu to any one of the four SolidWorks frames (Main Frame, Part Frame, Assembly Frame, or Drawing Frame). To do call this method with the appropriate argument in the docType parameter. For example, if you want your menu to be available when a part document is active, then call this method and pass swDocPART as the first argument. After adding your menu to the Part Frame, you do not need to do it again during the current SolidWorks session. Once a part document is activated by the end-user, your menu option is automatically displayed.

The menuItem argument should be the complete menu string including the main menu and any submenus. If a menu or submenu does not exist, then it is automatically created with a position at the end of the specified parent menu. There is no need to explicitly call SldWorks::AddMenu to add the actual menu or submenu unless you must add that menu or submenu at a specific position. It is recommended that you add our main menu using SldWorks::AddMenu so it can be placed between the existing Tools and Window menu items that appear in the SolidWorks menu bar. Submenus are created at the end of the parent menu. Therefore, if your menu structure is created in order using sequential calls, then all the menu items are positioned based on their order of creation. However, if a menu or submenu needs to be placed into an existing menu at a specific position, then you must create the submenu using SldWorks::AddMenu.

The callbackFcnAndModule argument specifies which function to call when this menu item is selected by the end-user. The syntax is as follows:

"dllname@function@updatefunction,hintstring"

where:

dllname - name of your library as specified in your project's .def file. The actual DLL filename and the definition in the .def file must be the same.

function - name of the function that gets called when the end-user selects the menu item. This function must also be declared as an export in your .def file.

updatefunction - optional and is used to control the state of the menu item. If specified, this function is called before the menu is displayed. The display of the menu item is controlled by the return value of updateFunction. The following return values have the following affects on the menu item:

return 0 - Menu item is unchecked and disabled.

return 1 - Menu item is unchecked and enabled. This is the default menu state with if no update function is specified.

return 2 - Menu item is checked and disabled.

return 3 - Menu item is checked and enabled.

hintstring - optional and is shown in the SolidWorks status bar when the end-user moves the mouse over this particular menu item. If hintstring is specified, it must be preceded by a comma.

For example:

"Userdll@AddBox@checkUserSelections,Add a box"
