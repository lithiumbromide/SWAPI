---
title: "GetTemporaryAxes Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetTemporaryAxes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTemporaryAxes.html"
---

# GetTemporaryAxes Method (IView)

Gets the information of the temporary axes displayed in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTemporaryAxes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetTemporaryAxes()
```

### C#

```csharp
System.object GetTemporaryAxes()
```

### C++/CLI

```cpp
System.Object^ GetTemporaryAxes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of double of the information about the temporary axes in this view (see **Remarks**)

## VBA Syntax

See [View::GetTemporaryAxes](ms-its:sldworksapivb6.chm::/sldworks~View~GetTemporaryAxes.html).

## Examples

[Get Temporary Axes in Each Drawing View (VBA)](Get_Temporary_Axes_in_Each_Drawing_View_Example_VB.htm)

## Remarks

This array contains the start and end points, in that order, of temporary axes.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetTemporaryAxesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTemporaryAxesCount.html)
[IView::IGetTemporaryAxes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetTemporaryAxes.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
