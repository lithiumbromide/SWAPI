---
title: "AddMenu Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "AddMenu"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.html"
---

# AddMenu Method (IFrame)

Adds a menu item.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddMenu( _
   ByVal Menu As System.String, _
   ByVal Position As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim Menu As System.String
Dim Position As System.Integer
Dim value As System.Boolean

value = instance.AddMenu(Menu, Position)
```

### C#

```csharp
System.bool AddMenu(
   System.string Menu,
   System.int Position
)
```

### C++/CLI

```cpp
System.bool AddMenu(
   System.String^ Menu,
   System.int Position
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Menu`: Name of the menu item to add; including parent menu names, e.g., subMenuString@menuString (see **Remarks**)
- `Position`: Position of the existing menu item before which to insert the new menu item; the first menu item is at position 0; if Position is 1, the new menu item is appended to the end of the menu (see **Remarks**)

### Return Value

True if menu item was successfully added, false if not

## VBA Syntax

See [Frame::AddMenu](ms-its:sldworksapivb6.chm::/sldworks~Frame~AddMenu.html).

## Remarks

If the name of a parent menu name is not specified in Menu, then:

- the menu item appears on the Tools menu below the **XPress products** menu item.
- Position is ignored.

This method is only valid when the application is implemented as a DLL, not as an EXE.

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[IFrame::AddMenuItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.html)
[IFrame::AddMenuPopupItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem.html)
[IFrame::GetSubMenuCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.html)
[IFrame::GetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.html)
[IFrame::IGetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetSubMenus.html)
[IFrame::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.html)
[IFrame::RenameMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu.html)
[ISldWorks::GetLocalizedMenuName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLocalizedMenuName.html)
[IFrame::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem2.html)
[IFrame::RemoveMenuPopupIcon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenuPopupIcon.html)
