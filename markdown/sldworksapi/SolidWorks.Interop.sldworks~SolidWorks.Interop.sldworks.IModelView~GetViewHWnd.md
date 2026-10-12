---
title: "GetViewHWnd Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "GetViewHWnd"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewHWnd.html"
---

# GetViewHWnd Method (IModelView)

Obsolete. Superseded by [IModelView::GetViewHWndx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewHWndx64.html).

This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016.

The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used.

Gets the Microsoft window handle for this model view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetViewHWnd() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Integer

value = instance.GetViewHWnd()
```

### C#

```csharp
System.int GetViewHWnd()
```

### C++/CLI

```cpp
System.int GetViewHWnd();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Microsoft window handle

## VBA Syntax

See [ModelView::GetViewHWnd](ms-its:sldworksapivb6.chm::/sldworks~ModelView~GetViewHWnd.html).

## Remarks

**All applications are required to be compatible with SOLIDWORKS x64. You must replace all calls to 32-bit only APIs with calls to their 64-bit safe counterparts.**

See [Eliminating 32-bit only API use](sldworksapiprogguide.chm::/Overview/Eliminating_32-Bit_Only_API_Use.htm) for more information.

Window handles are not unique across computers.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelWindow::HWnd Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow~HWnd.html)
