---
title: "ScaleDecimal Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "ScaleDecimal"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleDecimal.html"
---

# ScaleDecimal Property (IView)

Gets or sets the scale of the drawing view, returning the results in decimal format.

## Syntax

### Visual Basic (Declaration)

```vb
Property ScaleDecimal As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Double

instance.ScaleDecimal = value

value = instance.ScaleDecimal
```

### C#

```csharp
System.double ScaleDecimal {get; set;}
```

### C++/CLI

```cpp
property System.double ScaleDecimal {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Drawing view scale

## VBA Syntax

See [View::ScaleDecimal](ms-its:sldworksapivb6.chm::/sldworks~View~ScaleDecimal.html).

## Examples

[Set View Scale (VBA)](Set_View_Scale_Example_VB.htm)

## Remarks

[IView::ScaleRatio](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~ScaleRatio.html) or [IView::IScaleRatio](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IScaleRatio.html) and this property contain the same information, but use the value in different ways:

- IView::ScaleRatio gets or sets the scale as a ratio of two numbers.
- IView::ScaleDecimal returns the scale as a decimal number.

For example, if View::ScaleRatio returns 3 2 or 3:2, then IView::ScaleDecimal would return 1.5.

Changing this property can cause changes to the graphics of the drawing. After making all the of the view-related changes, call the [IModelDoc2::EditRebuild2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) method to regenerate the drawing to see these changes.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::UseParentScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseParentScale.html)
[IView::UseSheetScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseSheetScale.html)
