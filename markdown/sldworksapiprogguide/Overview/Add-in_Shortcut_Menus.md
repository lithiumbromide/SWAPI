---
title: "Add-in Shortcut Menus"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Add-in_Shortcut_Menus.htm"
---

# Add-in Shortcut Menus

To create and display a shortcut (pop-up) menu in a SOLIDWORKS add-in, create a SOLIDWORKS C++, VB.NET, or C# add-in project in Visual Studio and do the following:

1. In SwAddin.AddCommandManager():

  1. Add a menu and menu item to the SOLIDWORKS main menu by calling [ISldWorks::AddMenu](sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.html) and [ISldWorks::AddMenuItem4](sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem4.html) (C++ add-ins only). When selected, the menu item will launch the shortcut menu.
  2. Add a third-party icon to a context-sensitive menu by calling [IFrame::AddMenuPopupIcon](sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon.html) (C++ add-ins) or [IFrame::AddMenuPopupIcon2](sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon2.html) (VB.NET or C# add-ins). When clicked, the icon will launch the shortcut menu.
  3. Create and register your shortcut menu by calling [ISldWorks::RegisterThirdPartyPopupMenu](sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RegisterThirdPartyPopupMenu.html).
  4. Call [ISldWorks::AddItemToThirdPartyPopupMenu](sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu.html) (C++ add-ins) or [ISldWorks::AddItemToThirdPartyPopupMenu2](sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu2.html) (VB.NET or C# add-ins) one or more times to create one or more menu items in the shortcut menu. Uniquely specify the item argument for each menu item, menu break, and separator bar in the menu. Do not specify the item argument for menu bar icons.
2. In the menu and toolbar callback region of SwAddin:

  1. Implement the callback and enable functions for each shortcut menu item and each menu bar icon that was created in step 1d. See [Add-in Callback and Enable Methods](Add-in_Callbacks.htm).
  2. Implement the callback and enable functions for the menu item and third-party icon that were created in steps 1a and 1b. From the callback functions of the icon and menu item, call [ISldWorks::ShowThirdPartyPopupMenu](sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowThirdPartyPopupMenu.html) to display the shortcut menu at a specific location in the SOLIDWORKS graphics area. See [Add-in Callback and Enable Methods](Add-in_Callbacks.htm).
3. Remove menu items from the shortcut menu at runtime by calling [ISldWorks::RemoveItemFromThirdPartyPopupMenu](sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveItemFromThirdPartyPopupMenu.html) from an event handler of the add-in.
4. In SwAddin.DisconnectFromSW():

  1. Call [ISldWorks::RemoveMenu](sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.html) to remove the menu from the SOLIDWORKS main menu bar, if added in step 1a (C++ add-ins only).
  2. Call [IFrame::RemoveMenuPopupIcon](sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenuPopupIcon.html) to remove the third-party icon from the context-sensitive menu, if added in step 1b.

To learn more about add-ins and their menu items and toolbars:

- [Add-in Icons](Add-in_Icons.htm)
- [Add-in Toolbars](Add-in_Toolbars.htm)
- [Using SwAddin to Create a SOLIDWORKS Add-in](Using_SwAddin_to_Create_a_SolidWorks_Addin.htm)
- [SOLIDWORKS API Add-in Templates and Wizards](SolidWorks_API_Add-Ins,_Project_Templates,_and_Wizards.htm)
