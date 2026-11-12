---
title: "ICreateRevolutionSurface Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ICreateRevolutionSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateRevolutionSurface.html"
---

# ICreateRevolutionSurface Method (IBody)

Obsolete. Superseded by [IBody2::ICreateRevolutionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateRevolutionSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateRevolutionSurface( _
   ByVal ProfileCurve As Curve, _
   ByVal AxisPoint As System.Object, _
   ByVal AxisDirection As System.Object, _
   ByVal ProfileEndPtParams As System.Object _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim ProfileCurve As Curve
Dim AxisPoint As System.Object
Dim AxisDirection As System.Object
Dim ProfileEndPtParams As System.Object
Dim value As Surface

value = instance.ICreateRevolutionSurface(ProfileCurve, AxisPoint, AxisDirection, ProfileEndPtParams)
```

### C#

```csharp
Surface ICreateRevolutionSurface(
   Curve ProfileCurve,
   System.object AxisPoint,
   System.object AxisDirection,
   System.object ProfileEndPtParams
)
```

### C++/CLI

```cpp
Surface^ ICreateRevolutionSurface(
   Curve^ ProfileCurve,
   System.Object^ AxisPoint,
   System.Object^ AxisDirection,
   System.Object^ ProfileEndPtParams
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ProfileCurve`:
- `AxisPoint`:
- `AxisDirection`:
- `ProfileEndPtParams`:

## VBA Syntax

See [Body::ICreateRevolutionSurface](ms-its:sldworksapivb6.chm::/sldworks~Body~ICreateRevolutionSurface.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
