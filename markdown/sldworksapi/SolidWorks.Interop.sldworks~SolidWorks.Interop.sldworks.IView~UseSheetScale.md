---
title: "UseSheetScale Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "UseSheetScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseSheetScale.html"
---

# UseSheetScale Property (IView)

Gets or sets whether the scale of the drawing view is the same as the scale of the drawing sheet on which this view is located.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseSheetScale As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

instance.UseSheetScale = value

value = instance.UseSheetScale
```

### C#

```csharp
System.int UseSheetScale {get; set;}
```

### C++/CLI

```cpp
property System.int UseSheetScale {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

1 if the view scale is the same as the sheet scale, 0 if the view scale is independent of the sheet scale

## VBA Syntax

See [View::UseSheetScale](ms-its:sldworksapivb6.chm::/sldworks~View~UseSheetScale.html).

## Examples

[Set View Scale (VBA)](Set_View_Scale_Example_VB.htm)

## Remarks

If the property is 0, then it is possible that the view scale is the same as the sheet scale.

Changing this property can cause changes to the graphics of the drawing. After making all of the view-related changes, call the [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) method to regenerate the drawing to see these changes.

To set the drawing view's scale to be the same as the parent's drawing sheet's scale, use [IView::UseParentScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~UseParentScale.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::ScaleRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleRatio.html)
[IView::ScaleDecimal Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleDecimal.html)
[IView::IScaleRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IScaleRatio.html)
