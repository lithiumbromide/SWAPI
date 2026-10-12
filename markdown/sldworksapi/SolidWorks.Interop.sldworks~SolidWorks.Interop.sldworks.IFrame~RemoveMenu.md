---
title: "RemoveMenu Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "RemoveMenu"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.html"
---

# RemoveMenu Method (IFrame)

Removes a menu item.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveMenu( _
   ByVal MenuItemString As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim MenuItemString As System.String

instance.RemoveMenu(MenuItemString)
```

### C#

```csharp
void RemoveMenu(
   System.string MenuItemString
)
```

### C++/CLI

```cpp
void RemoveMenu(
   System.String^ MenuItemString
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MenuItemString`: Name of menu item (see **Remarks**)

## VBA Syntax

See [Frame::RemoveMenu](ms-its:sldworksapivb6.chm::/sldworks~Frame~RemoveMenu.html).

## Remarks

Use [ISldWorks::GetMenuStrings](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetMenuStrings.html) to get MenuItemString.

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[IFrame::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.html)
[IFrame::AddMenuItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.html)
[IFrame::AddMenuPopupItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem.html)
[IFrame::GetSubMenuCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.html)
[IFrame::GetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.html)
[IFrame::IGetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetSubMenus.html)
[IFrame::RenameMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu.html)
[ISldWorks::GetMenuStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMenuStrings.html)
