---
title: "DisplayControlPolygon Property (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "DisplayControlPolygon"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~DisplayControlPolygon.html"
---

# DisplayControlPolygon Property (ISketchSpline)

Gets or sets whether to add a control polygon to this spline.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplayControlPolygon As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim value As System.Boolean

instance.DisplayControlPolygon = value

value = instance.DisplayControlPolygon
```

### C#

```csharp
System.bool DisplayControlPolygon {get; set;}
```

### C++/CLI

```cpp
property System.bool DisplayControlPolygon {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to add a control polygon, false to not

## VBA Syntax

See [SketchSpline::DisplayControlPolygon](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~DisplayControlPolygon.html).

## Examples

[Get and Set Spline Properties (VBA)](Get_and_Set_Spline_Properties_Example_VB.htm)

## Remarks

To add a control polygon, set [ISldWorks::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html) swSketchShowSplineControlPolygon to True.

If the spline is not smooth after dragging a node of the control polygon, use [ISketchSpline::RelaxSpline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSpline~RelaxSpline.html) to smoothen its shape.

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
