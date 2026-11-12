---
title: "HWndx64 Property (IModelWindow)"
project: "SOLIDWORKS API Help"
interface: "IModelWindow"
member: "HWndx64"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow~HWndx64.html"
---

# HWndx64 Property (IModelWindow)

Gets the handle to this model window in 64-bit applications.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property HWndx64 As System.Long
```

### Visual Basic (Usage)

```vb
Dim instance As IModelWindow
Dim value As System.Long

value = instance.HWndx64
```

### C#

```csharp
System.long HWndx64 {get;}
```

### C++/CLI

```cpp
property System.int64 HWndx64 {
   System.int64 get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Handle for this model window

## VBA Syntax

See [ModelWindow::HWndx64](ms-its:sldworksapivb6.chm::/sldworks~ModelWindow~HWndx64.html).

## Remarks

This property is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software.

## See Also

[IModelWindow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.html)
[IModelWindow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow_members.html)
[IModelWindow::HWnd Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow~HWnd.html)

## Availability

SOLIDWORKS 2010 SP4, Revision 18.4
