---
title: "CreateRevolutionSurface Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "CreateRevolutionSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~CreateRevolutionSurface.html"
---

# CreateRevolutionSurface Method (IBody)

Obsolete. Superseded by [IBody2::CreateRevolutionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateRevolutionSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateRevolutionSurface( _
   ByVal ProfileCurve As System.Object, _
   ByVal AxisPoint As System.Object, _
   ByVal AxisDirection As System.Object, _
   ByVal ProfileEndPtParams As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim ProfileCurve As System.Object
Dim AxisPoint As System.Object
Dim AxisDirection As System.Object
Dim ProfileEndPtParams As System.Object
Dim value As System.Object

value = instance.CreateRevolutionSurface(ProfileCurve, AxisPoint, AxisDirection, ProfileEndPtParams)
```

### C#

```csharp
System.object CreateRevolutionSurface(
   System.object ProfileCurve,
   System.object AxisPoint,
   System.object AxisDirection,
   System.object ProfileEndPtParams
)
```

### C++/CLI

```cpp
System.Object^ CreateRevolutionSurface(
   System.Object^ ProfileCurve,
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

See [Body::CreateRevolutionSurface](ms-its:sldworksapivb6.chm::/sldworks~Body~CreateRevolutionSurface.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
