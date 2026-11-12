---
title: "TangentMagnitude Property (ISplineHandle)"
project: "SOLIDWORKS API Help"
interface: "ISplineHandle"
member: "TangentMagnitude"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentMagnitude.html"
---

# TangentMagnitude Property (ISplineHandle)

Gets or sets the weight for the tangency magnitude in the specified direction for this spline handle.

## Syntax

### Visual Basic (Declaration)

```vb
Property TangentMagnitude( _
   ByVal WhichDirection As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineHandle
Dim WhichDirection As System.Integer
Dim value As System.Double

instance.TangentMagnitude(WhichDirection) = value

value = instance.TangentMagnitude(WhichDirection)
```

### C#

```csharp
System.double TangentMagnitude(
   System.int WhichDirection
) {get; set;}
```

### C++/CLI

```cpp
property System.double TangentMagnitude {
   System.double get(System.int WhichDirection);
   void set (System.int WhichDirection, System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichDirection`: Direction as defined in [swTangentMagnitudeDirection_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangentMagnitudeDirection_e.html)

### Property Value

Weight for the tangency magnitude in the specified direction

## VBA Syntax

See [SplineHandle::TangentMagnitude](ms-its:sldworksapivb6.chm::/sldworks~SplineHandle~TangentMagnitude.html).

## Examples

See the [ISplineHandle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html) examples.

## See Also

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html)
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.html)
[ISplineHandle::TangentDriving Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentDriving.html)
[ISplineHandle::TangentPolarDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentPolarDirection.html)
[ISplineHandle::TangentRadialDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentRadialDirection.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
