---
title: "UseParentScale Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "UseParentScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseParentScale.html"
---

# UseParentScale Property (IView)

Gets or sets the drawing view's scale to match the parent drawing view's scale.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseParentScale As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

instance.UseParentScale = value

value = instance.UseParentScale
```

### C#

```csharp
System.bool UseParentScale {get; set;}
```

### C++/CLI

```cpp
property System.bool UseParentScale {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the drawing view's scale is set to be the same as the parent's drawing view scale, false if the drawing view scale is independent of the parent's drawing view scale

## VBA Syntax

See [View::UseParentScale](ms-its:sldworksapivb6.chm::/sldworks~View~UseParentScale.html).

## Examples

[Set View Scale Opposite Parent View Scale (VBA)](Set_View_Scale_Opposite_Parent_View_Scale_Example_VB.htm)

## Remarks

Changing this property can cause changes to the graphics of the drawing. After making all of the view-related changes, call the [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) method to regenerate the drawing to see these changes.

To set the drawing view's scale to be the same as the drawing sheet's scale, use [IView::UseSheetScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~UseSheetScale.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IScaleRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IScaleRatio.html)
[IView::ScaleRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleRatio.html)
[IView::ScaleDecimal Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleDecimal.html)

## Availability

SOLIDWORKS 2004 SP5, Revision Number 12.5
