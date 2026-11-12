---
title: "TranslateBy Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "TranslateBy"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~TranslateBy.html"
---

# TranslateBy Method (IModelView)

Translates the model view in the screen.

## Syntax

### Visual Basic (Declaration)

```vb
Sub TranslateBy( _
   ByVal X As System.Double, _
   ByVal Y As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim X As System.Double
Dim Y As System.Double

instance.TranslateBy(X, Y)
```

### C#

```csharp
void TranslateBy(
   System.double X,
   System.double Y
)
```

### C++/CLI

```cpp
void TranslateBy(
   System.double X,
   System.double Y
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: Translation in X direction, in meters and relative to X,Y axes of the graphics area
- `Y`: Translation in Y direction, in meters and relative to Windows X,Y axes of the graphics area

## VBA Syntax

See [ModelView::TranslateBy](ms-its:sldworksapivb6.chm::/sldworks~ModelView~TranslateBy.html).

## Examples

[Set Viewports (VB.NET)](Set_Viewports_Example_VBNET.htm)
[Set Viewports (VBA)](Set_Viewports_Example_VB.htm)
[Set Viewports (C#)](Set_Viewports_Example_CSharp.htm)

## Remarks

This method lets you specify a vector by which to translate the current SOLIDWORKS graphics area. This vector is in meters and is relative to the X,Y axes of the graphics area. This vector has no relation to the SOLIDWORKS triad axis that is displayed in the graphics area. This method is equivalent to the user-interface panning of the graphics area.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
