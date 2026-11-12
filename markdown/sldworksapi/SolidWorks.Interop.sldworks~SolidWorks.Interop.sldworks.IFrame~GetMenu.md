---
title: "GetMenu Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "GetMenu"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetMenu.html"
---

# GetMenu Method (IFrame)

Obsolete. Superseded by [IFrame::GetMenux64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetMenux64.html).

This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016.

The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used.

Gets the menu handle for the main frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMenu() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim value As System.Integer

value = instance.GetMenu()
```

### C#

```csharp
System.int GetMenu()
```

### C++/CLI

```cpp
System.int GetMenu();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Menu handle for the main frame

## VBA Syntax

See [Frame::GetMenu](ms-its:sldworksapivb6.chm::/sldworks~Frame~GetMenu.html).

## Remarks

**All applications are required to be compatible with SOLIDWORKS x64. You must replace all calls to 32-bit only APIs with calls to their 64-bit safe counterparts.**

See [Eliminating 32-bit only API use](sldworksapiprogguide.chm::/Overview/Eliminating_32-Bit_Only_API_Use.htm) for more information.

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[IFrame::GetHWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWnd.html)

## Availability

SOLIDWORKS 2008 SP2, Revision Number 16.2
