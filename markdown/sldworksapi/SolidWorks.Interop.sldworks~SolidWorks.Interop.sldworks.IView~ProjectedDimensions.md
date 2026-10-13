---
title: "ProjectedDimensions Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "ProjectedDimensions"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ProjectedDimensions.html"
---

# ProjectedDimensions Property (IView)

Gets or sets whether dimensions in this view are true or projected.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProjectedDimensions As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

instance.ProjectedDimensions = value

value = instance.ProjectedDimensions
```

### C#

```csharp
System.bool ProjectedDimensions {get; set;}
```

### C++/CLI

```cpp
property System.bool ProjectedDimensions {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the dimensions in this drawing view are projected measurements, false if the dimensions in this drawing view are true measurements

## VBA Syntax

See [View::ProjectedDimensions](ms-its:sldworksapivb6.chm::/sldworks~View~ProjectedDimensions.html).

## Remarks

Existing dimensions in this drawing view are deleted when this property is changed.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDimensionCount4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionCount4.html)
[IView::GetDimensionIds4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionIds4.html)
[IView::GetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionInfo6.html)
[IView::GetDimensionString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionString4.html)
[IView::IGetDimensionIds4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionIds4.html)
[IView::IGetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionInfo6.html)
[IView::IGetDimensionString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionString4.html)

## Availability

SOLIDWORKS 99, datecode 1999207
