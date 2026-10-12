---
title: "GetViewHWndx64 Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "GetViewHWndx64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewHWndx64.html"
---

# GetViewHWndx64 Method (IModelView)

Gets the Microsoft window handle for this model view in 64-bit applications.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetViewHWndx64() As System.Long
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Long

value = instance.GetViewHWndx64()
```

### C#

```csharp
System.long GetViewHWndx64()
```

### C++/CLI

```cpp
System.int64 GetViewHWndx64();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Microsoft window handle

## VBA Syntax

See [ModelView::GetViewHWndx64](ms-its:sldworksapivb6.chm::/sldworks~ModelView~GetViewHWndx64.html).

## Examples

[Get Names of Components, Window Handles, and DIBSECTIONs (C#)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_CSharp.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (VB.NET)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VBNET.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (VBA)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VB.htm)

## Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software.

Window handles are not unique across computers.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelWindow::HWnd Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow~HWnd.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
