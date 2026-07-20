---
title: "GetFirstDisplayDimension6 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstDisplayDimension6"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDisplayDimension6.html"
---

# GetFirstDisplayDimension6 Method (IView)

Gets the first display dimension in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstDisplayDimension6() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetFirstDisplayDimension6()
```

### C#

```csharp
System.object GetFirstDisplayDimension6()
```

### C++/CLI

```cpp
System.Object^ GetFirstDisplayDimension6();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

## VBA Syntax

See

[View::GetFirstDisplayDimension6](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstDisplayDimension6.html)

.

## Examples

[Get Dimension Values in Drawing (VBA)](Get_Dimension_Values_in_Drawing_Example_VB.htm)

## Remarks

This method obsoletes IView::GetFirstDisplayDimension5 by supporting inactive sheets.

A SOLIDWORKS dimension can be displayed more than once. For example, the base-extrude dimension could be brought into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the[IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)object in the SOLIDWORKS API. The original base-extrude dimension is represented by the[IDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension.html)object in the SOLIDWORKS API.

This method displays:

- dimensions on both the sheet and sheet format.
- suppressed dimensions.

Call[IDisplayDimension::GetNext5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetNext5.html)to get the next display dimension on this drawing sheet.

Do not use[IAnnotation::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~Visible.html)property to modify this method's return value.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

[IView::GetDimensionCount4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionCount4.html)

[IView::GetDimensionDisplayInfo5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfo5.html)

[IView::GetDimensionDisplayInfoSize2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfoSize2.html)

[IView::GetDimensionDisplayString5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayString5.html)

[IView::GetDimensionIds4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionIds4.html)

[IView::GetDimensionInfo7 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionInfo7.html)

[IView::GetDimensionString4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionString4.html)

[IView::GetDisplayDimensions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayDimensions.html)

[IView::ProjectedDimensions Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ProjectedDimensions.html)

## Availability

SOLIDWORKS 2025 SP01, Revision Number 33.1
