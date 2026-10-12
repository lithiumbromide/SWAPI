---
title: "HWnd Property (IModelWindow)"
project: "SOLIDWORKS API Help"
interface: "IModelWindow"
member: "HWnd"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow~HWnd.html"
---

# HWnd Property (IModelWindow)

Obsolete. Superseded by [IModelWindow::HWndx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow~HWndx64.html).

This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016.

The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used.

Gets the handle to this model window.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property HWnd As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelWindow
Dim value As System.Integer

value = instance.HWnd
```

### C#

```csharp
System.int HWnd {get;}
```

### C++/CLI

```cpp
property System.int HWnd {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Handle for this model window

## VBA Syntax

See [ModelWindow::HWnd](ms-its:sldworksapivb6.chm::/sldworks~ModelWindow~HWnd.html).

## Examples

[Switch Documents (C#)](Switch_Documents_Example_CSharp.htm)
[Switch Documents (VB.NET)](Switch_Documents_Example_VBNET.htm)
[Switch Documents (VBA)](Switch_Documents_Example_VB.htm)

## Remarks

**All applications are required to be compatible with SOLIDWORKS x64. You must replace all calls to 32-bit only APIs with calls to their 64-bit safe counterparts.**

See [Eliminating 32-bit only API use](sldworksapiprogguide.chm::/Overview/Eliminating_32-Bit_Only_API_Use.htm) for more information.

## See Also

[IModelWindow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.html)
[IModelWindow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
