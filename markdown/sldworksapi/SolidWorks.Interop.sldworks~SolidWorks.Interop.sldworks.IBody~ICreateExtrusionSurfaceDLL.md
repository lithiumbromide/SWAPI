---
title: "ICreateExtrusionSurfaceDLL Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ICreateExtrusionSurfaceDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateExtrusionSurfaceDLL.html"
---

# ICreateExtrusionSurfaceDLL Method (IBody)

Obsolete. Superseded by [IBody2::ICreateExtrusionSurfaceDLL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateExtrusionSurfaceDLL.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateExtrusionSurfaceDLL( _
   ByVal ProfileCurve As Curve, _
   ByRef AxisDirection As System.Double _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim ProfileCurve As Curve
Dim AxisDirection As System.Double
Dim value As Surface

value = instance.ICreateExtrusionSurfaceDLL(ProfileCurve, AxisDirection)
```

### C#

```csharp
Surface ICreateExtrusionSurfaceDLL(
   Curve ProfileCurve,
   ref System.double AxisDirection
)
```

### C++/CLI

```cpp
Surface^ ICreateExtrusionSurfaceDLL(
   Curve^ ProfileCurve,
   System.double% AxisDirection
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ProfileCurve`:
- `AxisDirection`:

## VBA Syntax

See [Body::ICreateExtrusionSurfaceDLL](ms-its:sldworksapivb6.chm::/sldworks~Body~ICreateExtrusionSurfaceDLL.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
