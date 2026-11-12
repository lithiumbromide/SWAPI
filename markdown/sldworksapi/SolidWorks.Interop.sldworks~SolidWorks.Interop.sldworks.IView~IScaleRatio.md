---
title: "IScaleRatio Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IScaleRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IScaleRatio.html"
---

# IScaleRatio Property (IView)

Gets or sets the scale of the drawing view, returning the results in ratio format (n:n).

## Syntax

### Visual Basic (Declaration)

```vb
Property IScaleRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Double

instance.IScaleRatio = value

value = instance.IScaleRatio
```

### C#

```csharp
System.double IScaleRatio {get; set;}
```

### C++/CLI

```cpp
property System.double IScaleRatio {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of 2 doubles (see **Remarks**)

## VBA Syntax

See [View::IScaleRatio](ms-its:sldworksapivb6.chm::/sldworks~View~IScaleRatio.html).

## Remarks

The two values represent the two numbers if the scale is described as a ratio. The first value is the numerator; the second value is the denominator. This is what the scale is when represented as n:n.

This property and [IView::ScaleDecimal](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~ScaleDecimal.html) contain the same information, but use the value in a different form.

- IView::ScaleRatio returns the scale as a ratio of two numbers.
- IView::ScaleDecimal returns the scale as a decimal number.

For example, if View::ScaleRatio returns 3 2 or 3:2, then IView::ScaleDecimal would return 1.5.

Changing this property may cause changes to the graphics of the drawing. After making all of the view-related changes, call [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) to regenerate the drawing to see these changes.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::UseParentScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseParentScale.html)
[IView::UseSheetScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseSheetScale.html)
[IView::ScaleRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleRatio.html)
