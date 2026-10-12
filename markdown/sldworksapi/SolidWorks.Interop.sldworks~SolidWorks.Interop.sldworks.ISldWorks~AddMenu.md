---
title: "AddMenu Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddMenu"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.html"
---

# AddMenu Method (ISldWorks)

Adds a menu item to a SOLIDWORKS menu for DLL applications.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddMenu( _
   ByVal DocType As System.Integer, _
   ByVal Menu As System.String, _
   ByVal Position As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DocType As System.Integer
Dim Menu As System.String
Dim Position As System.Integer
Dim value As System.Integer

value = instance.AddMenu(DocType, Menu, Position)
```

### C#

```csharp
System.int AddMenu(
   System.int DocType,
   System.string Menu,
   System.int Position
)
```

### C++/CLI

```cpp
System.int AddMenu(
   System.int DocType,
   System.String^ Menu,
   System.int Position
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocType`: Document type to add the menu item as defined by [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `Menu`: Name of menu item to add, including any parent menu names, e.g., subMenuString@menuString
- `Position`: Specifies the position where to add the new menu item; 0 = first position and 1 = end of the parent menu (see **Remarks**)

### Return Value

1 if menu item is added successfully added or 0 if adding the menu item failed

## VBA Syntax

See [SldWorks::AddMenu](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddMenu.html).

## Examples

[Add Menu and Menu Item (C#)](Add_Menu_and_Menu_Item_Example_CSharp.htm)
[Add Menu and Menu Item (VB.NET)](Add_Menu_and_Menu_Item_Example_VBNET.htm)

## Remarks

If the name of a parent menu is not specified in Menu, then:

- the menu item appears on the **Tools** menu below the **XPress products** menu item.
- Position is ignored.

Menus items are automatically created at the end of the parent menu when using [ISldWorks::AddMenuItem5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem5.html). Therefore, if your menu structure is created using sequential calls to SldWorks::AddMenuItem5, then all the menu items are positioned based on their order of creation.

This method is only required when a menu needs to be placed into an existing menu at a specific position.

Read about [Add-in Shortcut Menus](ms-its:sldworksapiprogguide.chm::/OVERVIEW/Add-in_Shortcut_Menus.htm).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem2.html)
[ISldWorks::AddToolbar4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.html)
[ISldWorks::AddToolbarCommand2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2.html)
[ISldWorks::RemoveFromMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromMenu.html)
[ISldWorks::RemoveFromPopupMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromPopupMenu.html)
[ISldWorks::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.html)
[ISldWorks::RemoveMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.html)
[ISldWorks::RemoveToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2.html)
[ISldWorks::GetLocalizedMenuName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLocalizedMenuName.html)

## Availability

SOLIDWORKS 99, datecode 1999207
