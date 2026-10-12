---
title: "IGetDependentViews Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetDependentViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDependentViews.html"
---

# IGetDependentViews Method (IView)

Gets either all, or only the specified, dependent views in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDependentViews( _
   ByVal AllViews As System.Boolean, _
   ByVal SpecificViewType As System.Integer, _
   ByVal DependentViewCount As System.Integer _
) As View
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim AllViews As System.Boolean
Dim SpecificViewType As System.Integer
Dim DependentViewCount As System.Integer
Dim value As View

value = instance.IGetDependentViews(AllViews, SpecificViewType, DependentViewCount)
```

### C#

```csharp
View IGetDependentViews(
   System.bool AllViews,
   System.int SpecificViewType,
   System.int DependentViewCount
)
```

### C++/CLI

```cpp
View^ IGetDependentViews(
   System.bool AllViews,
   System.int SpecificViewType,
   System.int DependentViewCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AllViews`: True to get all of the dependent views in this view, false to get only the SpecificViewType views in this view
- `SpecificViewType`: Type of dependent view as defined in [swDrawingViewTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingViewTypes_e.html)
- `DependentViewCount`: Number of dependent views

### Return Value

Array of dependent [views](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html)

## VBA Syntax

See [View::IGetDependentViews](ms-its:sldworksapivb6.chm::/sldworks~View~IGetDependentViews.html).

## Remarks

Call [IView::GetDependentViewCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDependentViewCount.html) before calling this method to get the value of DependentViewCount.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDependentViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDependentViews.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
