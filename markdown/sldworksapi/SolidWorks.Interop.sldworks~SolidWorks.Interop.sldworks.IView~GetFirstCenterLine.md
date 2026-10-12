---
title: "GetFirstCenterLine Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstCenterLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterLine.html"
---

# GetFirstCenterLine Method (IView)

Gets the first centerline in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstCenterLine() As Centerline
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As Centerline

value = instance.GetFirstCenterLine()
```

### C#

```csharp
Centerline GetFirstCenterLine()
```

### C++/CLI

```cpp
Centerline^ GetFirstCenterLine();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [centerline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterLine.html)

## VBA Syntax

See [View::GetFirstCenterLine](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstCenterLine.html).

## Examples

[Get Centerlines in Drawing (C#)](Get_Centerlines_in_Drawing_Example_CSharp.htm)
[Get Centerlines in Drawing (VB.NET)](Get_Centerlines_in_Drawing_Example_VBNET.htm)
[Get Centerlines in Drawing (VBA)](Get_Centerlines_in_Drawing_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetCenterLineSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterLineSketch.html)
[ICenterline::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine~GetNext.html)
[IView::GetCenterLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterLines.html)
[IView::IGetCenterLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterLines.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.0
