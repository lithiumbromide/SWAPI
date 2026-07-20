---
title: "GetDimensionDisplayString4 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDimensionDisplayString4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayString4.html"
---

# GetDimensionDisplayString4 Method (IView)

Obsolete. Superseded by

[IView::GetDimensionDisplayString5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayString5.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDimensionDisplayString4() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetDimensionDisplayString4()
```

### C#

```csharp
System.object GetDimensionDisplayString4()
```

### C++/CLI

```cpp
System.Object^ GetDimensionDisplayString4();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Array of strings containing the dimension text (see

Remarks

)

## VBA Syntax

See

[View::GetDimensionDisplayString4](ms-its:sldworksapivb6.chm::/sldworks~View~GetDimensionDisplayString4.html)

.

## Remarks

For each dimension in the drawing sheet or drawing view, this method returns 10 strings. If any of the dimension strings are not used, then those strings are returned as empty strings.

[value1, tolMax1 tolMin1, value2, tolMax2, tolMin2, prefix, suffix, callout1, callout2]

This set of data is returned for each dimension in the view. See[IView::GetDimensionCount4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDimensionCount4.html)to determine the number of dimensions in the drawing sheet or drawing view.

NOTES:

- A previous version of this method,

  [IView::GetDimensionDisplayString2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDimensionDisplayString2.html)

  or

  [IView::IGetDimensionDisplayString2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetDimensionDisplayString2.html)

  , detects and overlooks dangling dimensions. These method, IView::GetDimensionDisplayString4 and

  [IView::IGetDimensionDisplayString4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetDimensionDisplayString4.html)

  , do not overlook nor do they indicate that any dimensions are dangling. Use IView::GetDimensionDisplayString2 if you need dangling dimensions detected and overlooked.
- This method does not support

  [hole callouts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.html)

  .

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

[IView::GetDimensionDisplayInfo5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfo5.html)

[IView::GetDimensionDisplayInfoSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfoSize2.html)

[IView::GetDimensionIds4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionIds4.html)

[IView::GetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionInfo6.html)

[IView::GetDimensionString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionString4.html)

[IView::IGetDimensionDisplayInfo5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionDisplayInfo5.html)

[IView::IGetDimensionIds4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionIds4.html)

[IView::IGetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionInfo6.html)

[IView::IGetDimensionString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionString4.html)

[IView::ProjectedDimensions Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ProjectedDimensions.html)

[IView::GetFirstDisplayDimension5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDisplayDimension5.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
