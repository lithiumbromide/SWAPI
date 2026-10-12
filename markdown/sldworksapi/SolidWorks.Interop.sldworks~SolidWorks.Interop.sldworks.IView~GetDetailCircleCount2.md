---
title: "GetDetailCircleCount2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDetailCircleCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleCount2.html"
---

# GetDetailCircleCount2 Method (IView)

Gets the number of detail circles in the drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDetailCircleCount2( _
   ByRef Size As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Size As System.Integer
Dim value As System.Integer

value = instance.GetDetailCircleCount2(Size)
```

### C#

```csharp
System.int GetDetailCircleCount2(
   out System.int Size
)
```

### C++/CLI

```cpp
System.int GetDetailCircleCount2(
   [Out] System.int Size
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Size`: Size, which includes a double for each detail circle; this new double contains the layer ID for the detail circle

### Return Value

Number of detail circles in the drawing view

## VBA Syntax

See [View::GetDetailCircleCount2](ms-its:sldworksapivb6.chm::/sldworks~View~GetDetailCircleCount2.html).

## Examples

[Get Detail Circle Information (VBA)](Get_Detail_Circle_Information_Example_VB.htm)

## Remarks

Call this method before calling [IView::GetDetailCircles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetDetailCircles.html) to get the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetDetail Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetail.html)
[IView::IGetDetailCircleInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircleInfo2.html)
[IView::IGetDetailCircleStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircleStrings.html)
[IView::GetDetail Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetail.html)
[IView::GetDetailCircleInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleInfo2.html)
[IView::GetDetailCircleStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleStrings.html)
[IView::GetDetailCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircles.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
