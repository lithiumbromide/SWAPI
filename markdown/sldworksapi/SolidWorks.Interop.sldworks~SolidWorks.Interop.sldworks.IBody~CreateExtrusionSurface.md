---
title: "CreateExtrusionSurface Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "CreateExtrusionSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~CreateExtrusionSurface.html"
---

# CreateExtrusionSurface Method (IBody)

Obsolete. Superseded by [IBody2::CreateExtrusionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateExtrusionSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateExtrusionSurface( _
   ByVal ProfileCurve As System.Object, _
   ByVal AxisDirection As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim ProfileCurve As System.Object
Dim AxisDirection As System.Object
Dim value As System.Object

value = instance.CreateExtrusionSurface(ProfileCurve, AxisDirection)
```

### C#

```csharp
System.object CreateExtrusionSurface(
   System.object ProfileCurve,
   System.object AxisDirection
)
```

### C++/CLI

```cpp
System.Object^ CreateExtrusionSurface(
   System.Object^ ProfileCurve,
   System.Object^ AxisDirection
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ProfileCurve`:
- `AxisDirection`:

## VBA Syntax

See [Body::CreateExtrusionSurface](ms-its:sldworksapivb6.chm::/sldworks~Body~CreateExtrusionSurface.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
