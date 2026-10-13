---
title: "ICreateRevolutionSurfaceDLL Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ICreateRevolutionSurfaceDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRevolutionSurfaceDLL.html"
---

# ICreateRevolutionSurfaceDLL Method (IBody2)

Creates a surface of revolution for this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateRevolutionSurfaceDLL( _
   ByVal ProfileCurve As Curve, _
   ByRef AxisPoint As System.Double, _
   ByRef AxisDirection As System.Double, _
   ByRef ProfileEndPtParams As System.Double _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim ProfileCurve As Curve
Dim AxisPoint As System.Double
Dim AxisDirection As System.Double
Dim ProfileEndPtParams As System.Double
Dim value As Surface

value = instance.ICreateRevolutionSurfaceDLL(ProfileCurve, AxisPoint, AxisDirection, ProfileEndPtParams)
```

### C#

```csharp
Surface ICreateRevolutionSurfaceDLL(
   Curve ProfileCurve,
   ref System.double AxisPoint,
   ref System.double AxisDirection,
   ref System.double ProfileEndPtParams
)
```

### C++/CLI

```cpp
Surface^ ICreateRevolutionSurfaceDLL(
   Curve^ ProfileCurve,
   System.double% AxisPoint,
   System.double% AxisDirection,
   System.double% ProfileEndPtParams
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ProfileCurve`: Pointer to a profile [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) object
- `AxisPoint`: Array of 3 doubles (x,y,z)
- `AxisDirection`: Array of 3 doubles (x,y,z)
- `ProfileEndPtParams`: Array of 2 doubles (uStart,uEnd)

### Return Value

Pointer to a new [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) of revolution

## VBA Syntax

See [Body2::ICreateRevolutionSurfaceDLL](ms-its:sldworksapivb6.chm::/sldworks~Body2~ICreateRevolutionSurfaceDLL.html).

## Remarks

Any existing object created by this method is destroyed if you call this method again.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
