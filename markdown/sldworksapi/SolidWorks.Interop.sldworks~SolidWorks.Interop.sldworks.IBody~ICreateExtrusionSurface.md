---
title: "ICreateExtrusionSurface Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ICreateExtrusionSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateExtrusionSurface.html"
---

# ICreateExtrusionSurface Method (IBody)

Obsolete. Superseded by [IBody2::ICreateExtrusionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateExtrusionSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateExtrusionSurface( _
   ByVal ProfileCurve As Curve, _
   ByVal AxisDirection As System.Object _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim ProfileCurve As Curve
Dim AxisDirection As System.Object
Dim value As Surface

value = instance.ICreateExtrusionSurface(ProfileCurve, AxisDirection)
```

### C#

```csharp
Surface ICreateExtrusionSurface(
   Curve ProfileCurve,
   System.object AxisDirection
)
```

### C++/CLI

```cpp
Surface^ ICreateExtrusionSurface(
   Curve^ ProfileCurve,
   System.Object^ AxisDirection
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ProfileCurve`:
- `AxisDirection`:

## VBA Syntax

See [Body::ICreateExtrusionSurface](ms-its:sldworksapivb6.chm::/sldworks~Body~ICreateExtrusionSurface.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
