---
title: "IFrame Interface Methods"
project: "SOLIDWORKS API Help"
interface: "IFrame_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_methods.html"
---

# IFrame Interface Methods

For a list of all members of this type, see [IFrame members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddMenu | Adds a menu item. |
| Method | AddMenuItem | Obsolete. Superseded by IFrame::AddMenuItem2 . |
| Method | AddMenuItem2 | Adds a menu item and bitmap or a separator to an existing menu. |
| Method | AddMenuPopupIcon | Adds an icon to a context-sensitive menu of a C++ SOLIDWORKS add-in. |
| Method | AddMenuPopupIcon2 | Obsolete. Superseded by IFrame::AddMenuPopupIcon3 . |
| Method | AddMenuPopupIcon3 | Adds an icon to a context-sensitive menu of a SOLIDWORKS add-in. |
| Method | AddMenuPopupItem | Obsolete. Superseded by IFrame::AddMenuPopupItem2 . |
| Method | AddMenuPopupItem2 | Adds a menu item or separator to a shortcut menu (i.e., a right-click pop-up menu). |
| Method | GetHWnd | Obsolete. Superseded by IFrame::GetHWndx64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Gets the window handle for the main frame. |
| Method | GetHWndx64 | Gets the window handle for the main frame in 64-bit applications. |
| Method | GetMenu | Obsolete. Superseded by IFrame::GetMenux64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Gets the menu handle for the main frame. |
| Method | GetMenuState | Obsolete. Superseded by IFrame::AddMenuItem2 . |
| Method | GetMenux64 | Gets the menu handle for the main frame in 64-bit applications. |
| Method | GetModelWindowCount | Gets the number of child model windows for this frame. |
| Method | GetStatusBarPane | Gets a pointer to one of up to five panes on the right side of the status bar. |
| Method | GetSubMenuCount | Gets the number of submenus for this frame. |
| Method | GetSubMenus | Gets the submenus for this frame. |
| Method | IGetModelWindows | Gets the child model windows for this frame. |
| Method | IGetSubMenus | Gets the submenus for this frame. |
| Method | RemoveMenu | Removes a menu item. |
| Method | RemoveMenuPopupIcon | Removes an icon from a context-sensitive shortcut (popup) menu. |
| Method | RenameMenu | Renames a menu item. |
| Method | SetStatusBarText | Displays a text string in the main status bar area to the left of the status bar. |
| Method | ShowModelWindow | Shows a client model window. |

[Top](#topBookmark)

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
