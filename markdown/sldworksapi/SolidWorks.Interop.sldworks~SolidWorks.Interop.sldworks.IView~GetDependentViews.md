---
title: "GetDependentViews Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDependentViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDependentViews.html"
---

# GetDependentViews Method (IView)

Gets either all, or only the specified, dependent views in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDependentViews( _
   ByVal AllViews As System.Boolean, _
   ByVal SpecificViewType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim AllViews As System.Boolean
Dim SpecificViewType As System.Integer
Dim value As System.Object

value = instance.GetDependentViews(AllViews, SpecificViewType)
```

### C#

```csharp
System.object GetDependentViews(
   System.bool AllViews,
   System.int SpecificViewType
)
```

### C++/CLI

```cpp
System.Object^ GetDependentViews(
   System.bool AllViews,
   System.int SpecificViewType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AllViews`: True to get all of the dependent views in this view, false to get only the SpecificViewType views in this view
- `SpecificViewType`: Type of dependent view as defined in [swDrawingViewTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingViewTypes_e.html)

### Return Value

Array of dependent [views](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html)

## VBA Syntax

See [View::GetDependentViews](ms-its:sldworksapivb6.chm::/sldworks~View~GetDependentViews.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDependentViewCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDependentViewCount.html)
[IView::IGetDependentViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDependentViews.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
