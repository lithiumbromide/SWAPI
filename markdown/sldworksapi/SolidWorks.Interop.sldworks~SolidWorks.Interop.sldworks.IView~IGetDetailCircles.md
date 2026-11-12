---
title: "IGetDetailCircles Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetDetailCircles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircles.html"
---

# IGetDetailCircles Method (IView)

Gets the detail circles in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDetailCircles( _
   ByVal NumDetailCircles As System.Integer _
) As DetailCircle
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumDetailCircles As System.Integer
Dim value As DetailCircle

value = instance.IGetDetailCircles(NumDetailCircles)
```

### C#

```csharp
DetailCircle IGetDetailCircles(
   System.int NumDetailCircles
)
```

### C++/CLI

```cpp
DetailCircle^ IGetDetailCircles(
   System.int NumDetailCircles
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumDetailCircles`: Number of detail circles in the view

### Return Value

- in-process, unmanaged C++: Pointer to an array of [detail circles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDetailCircle.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Call [IView::GetDetailCircleCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDetailCircleCount2.html) to get the value for NumDetailCircles.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDetail Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetail.html)
[IView::GetDetailCircleInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleInfo2.html)
[IView::GetDetailCircleStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleStrings.html)
[IView::IGetDetail Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetail.html)
[IView::IGetDetailCircleInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircleInfo2.html)
[IView::IGetDetailCircleStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircleStrings.html)
[IView::GetDetailCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircles.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
