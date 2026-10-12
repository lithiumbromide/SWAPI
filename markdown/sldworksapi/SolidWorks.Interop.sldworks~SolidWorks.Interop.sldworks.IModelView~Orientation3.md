---
title: "Orientation3 Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "Orientation3"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Orientation3.html"
---

# Orientation3 Property (IModelView)

Gets or sets the model view orientation matrix.

## Syntax

### Visual Basic (Declaration)

```vb
Property Orientation3 As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As MathTransform

instance.Orientation3 = value

value = instance.Orientation3
```

### C#

```csharp
MathTransform Orientation3 {get; set;}
```

### C++/CLI

```cpp
property MathTransform^ Orientation3 {
   MathTransform^ get();
   void set (    MathTransform^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[View orientation matrix](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [ModelView::Orientation3](ms-its:sldworksapivb6.chm::/sldworks~ModelView~Orientation3.html).

## Remarks

When modifying a model view transform, you must use IModelView::Orientation3 and [IModelView::Translation3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~Translation3.html). For example:

```vb
...
Dim xyzOrigin As SldWorks.MathPoint
dPoint(0) = 0#: dPoint(1) = 0#: dPoint(2) = 0#
Set xyzOrigin = swMathUtil.CreatePoint((dPoint))

Set swVectorZ = swVectorZ.Scale(-1)
Set swMathTrans = swMathUtil.ComposeTransform(swVectorX, swVectorY, swVectorZ, xyzOrigin.ConvertToVector, 1#)
Set swMathTrans = swMathTrans.Inverse

Set swModelView = swModel.ActiveView
Set swViewTrans = swModelView.Orientation3
swModelView.Orientation3 = swMathTrans

Dim u As Double
u = swModelView.Scale2
Set swMathPoint = swVectorT.ConvertToPoint
Set swMathPoint = swMathPoint.Scale(-1 * u)
Set swMathPoint = swMathPoint.MultiplyTransform(swMathTrans)
swModelView.Translation3 = swMathPoint.ConvertToVector
...
```

Also, check the vectors by looking at the triad in the model view.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::Scale2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Scale2.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
