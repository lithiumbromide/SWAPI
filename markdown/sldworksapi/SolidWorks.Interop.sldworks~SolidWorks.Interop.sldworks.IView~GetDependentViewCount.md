---
title: "GetDependentViewCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDependentViewCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDependentViewCount.html"
---

# GetDependentViewCount Method (IView)

Gets the number of all, or only the specified, dependent views (i.e., alternate position, detail, section, etc.) in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDependentViewCount( _
   ByVal AllViews As System.Boolean, _
   ByVal SpecificViewType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim AllViews As System.Boolean
Dim SpecificViewType As System.Integer
Dim value As System.Integer

value = instance.GetDependentViewCount(AllViews, SpecificViewType)
```

### C#

```csharp
System.int GetDependentViewCount(
   System.bool AllViews,
   System.int SpecificViewType
)
```

### C++/CLI

```cpp
System.int GetDependentViewCount(
   System.bool AllViews,
   System.int SpecificViewType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AllViews`: True to get the number of all of the dependent views in this view, false to get the number of SpecificViewType views in this view
- `SpecificViewType`: Type of dependent view as defined in [swDrawingViewTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingViewTypes_e.html)

### Return Value

Number of dependent views

## VBA Syntax

See [View::GetDependentViewCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetDependentViewCount.html).

## Remarks

Call this method before calling [IView::IGetDependentViews](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetDependentViews.html) to get the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDependentViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDependentViews.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
