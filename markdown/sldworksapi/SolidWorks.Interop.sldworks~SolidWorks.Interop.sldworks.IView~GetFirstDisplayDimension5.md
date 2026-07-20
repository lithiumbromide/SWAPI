---
title: "GetFirstDisplayDimension5 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstDisplayDimension5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDisplayDimension5.html"
---

# GetFirstDisplayDimension5 Method (IView)

Obsolete. Superseded by

[IView::GetFirstDisplayDimension6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDisplayDimension6.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstDisplayDimension5() As DisplayDimension
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As DisplayDimension

value = instance.GetFirstDisplayDimension5()
```

### C#

```csharp
DisplayDimension GetFirstDisplayDimension5()
```

### C++/CLI

```cpp
DisplayDimension^ GetFirstDisplayDimension5();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

First

[display dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)

## VBA Syntax

See

[View::GetFirstDisplayDimension5](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstDisplayDimension5.html)

.

## Remarks

A SOLIDWORKS dimension can be displayed more than once. For example, the base-extrude dimension could be brought into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the[IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)object in the SOLIDWORKS API. The original base-extrude dimension is represented by the[IDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension.html)object in the SOLIDWORKS API.

This method displays:

- dimensions on both the sheet and sheet format.
- suppressed dimensions.

Call[IDisplayDimension::GetNext5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetNext5.html)to get the next display dimension on this drawing sheet.

Do not use[IAnnotation::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~Visible.html)property to modify this method's return value.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

[IView::GetDimensionCount4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionCount4.html)

[IView::GetDimensionDisplayInfo5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfo5.html)

[IView::GetDimensionDisplayInfoSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfoSize2.html)

[IView::GetDimensionDisplayString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayString4.html)

[IView::GetDimensionIds4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionIds4.html)

[IView::GetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionInfo6.html)

[IView::GetDimensionString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionString4.html)

[IView::IGetDimensionDisplayInfo5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionDisplayInfo5.html)

[IView::IGetDimensionDisplayString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionDisplayString4.html)

[IView::IGetDimensionIds4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionIds4.html)

[IView::IGetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionInfo6.html)

[IView::ProjectedDimensions Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ProjectedDimensions.html)

[IView::IGetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDisplayDimensions.html)

[IView::GetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayDimensions.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
