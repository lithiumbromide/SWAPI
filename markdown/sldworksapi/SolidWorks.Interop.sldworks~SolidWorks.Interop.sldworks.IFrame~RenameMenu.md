---
title: "RenameMenu Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "RenameMenu"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu.html"
---

# RenameMenu Method (IFrame)

Renames a menu item.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RenameMenu( _
   ByVal MenuItemString As System.String, _
   ByVal NewName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim MenuItemString As System.String
Dim NewName As System.String

instance.RenameMenu(MenuItemString, NewName)
```

### C#

```csharp
void RenameMenu(
   System.string MenuItemString,
   System.string NewName
)
```

### C++/CLI

```cpp
void RenameMenu(
   System.String^ MenuItemString,
   System.String^ NewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MenuItemString`: Name of the menu item
- `NewName`: New name of this menu item

## VBA Syntax

See [Frame::RenameMenu](ms-its:sldworksapivb6.chm::/sldworks~Frame~RenameMenu.html).

## Remarks

Use [ISldWorks::GetMenuStrings](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetMenuStrings.html) to get MenuItemString.

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[IFrame::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.html)
[IFrame::AddMenuItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.html)
[IFrame::GetSubMenuCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.html)
[IFrame::GetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.html)
[IFrame::IGetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetSubMenus.html)
[IFrame::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.html)
[ISldWorks::GetMenuStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMenuStrings.html)
