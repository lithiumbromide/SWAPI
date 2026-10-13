---
title: "Proportional Property (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "Proportional"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~Proportional.html"
---

# Proportional Property (ISketchSpline)

Gets or sets whether the spline resizes proportionally when you drag an endpoint the spline.

## Syntax

### Visual Basic (Declaration)

```vb
Property Proportional As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim value As System.Boolean

instance.Proportional = value

value = instance.Proportional
```

### C#

```csharp
System.bool Proportional {get; set;}
```

### C++/CLI

```cpp
property System.bool Proportional {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to resize the spline proportionally, false to not

## VBA Syntax

See [SketchSpline::Proportional](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~Proportional.html).

## Examples

[Get and Set Spline Properties (VBA)](Get_and_Set_Spline_Properties_Example_VB.htm)

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
