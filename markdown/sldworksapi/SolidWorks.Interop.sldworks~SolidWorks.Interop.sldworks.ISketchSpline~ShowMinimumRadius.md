---
title: "ShowMinimumRadius Property (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "ShowMinimumRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowMinimumRadius.html"
---

# ShowMinimumRadius Property (ISketchSpline)

Gets or sets the minimum radius of a curve for this spline.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowMinimumRadius As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim value As System.Boolean

instance.ShowMinimumRadius = value

value = instance.ShowMinimumRadius
```

### C#

```csharp
System.bool ShowMinimumRadius {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowMinimumRadius {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Minimum radius

## VBA Syntax

See [SketchSpline::ShowMinimumRadius](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~ShowMinimumRadius.html).

## Examples

[Get and Set Spline Properties (VBA)](Get_and_Set_Spline_Properties_Example_VB.htm)

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
