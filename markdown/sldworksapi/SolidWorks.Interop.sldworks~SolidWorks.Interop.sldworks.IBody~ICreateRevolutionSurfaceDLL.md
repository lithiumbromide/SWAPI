---
title: "ICreateRevolutionSurfaceDLL Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ICreateRevolutionSurfaceDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateRevolutionSurfaceDLL.html"
---

# ICreateRevolutionSurfaceDLL Method (IBody)

Obsolete. Superseded by [IBody2::ICreateRevolutionSurfaceDLL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateRevolutionSurfaceDLL.html).

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
Dim instance As IBody
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

- `ProfileCurve`:
- `AxisPoint`:
- `AxisDirection`:
- `ProfileEndPtParams`:

## VBA Syntax

See [Body::ICreateRevolutionSurfaceDLL](ms-its:sldworksapivb6.chm::/sldworks~Body~ICreateRevolutionSurfaceDLL.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
