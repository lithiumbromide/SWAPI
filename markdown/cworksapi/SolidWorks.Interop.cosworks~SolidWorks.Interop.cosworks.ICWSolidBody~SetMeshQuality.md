---
title: "SetMeshQuality Method (ICWSolidBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidBody"
member: "SetMeshQuality"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetMeshQuality.html"
---

# SetMeshQuality Method (ICWSolidBody)

Sets the mesh quality for the solid body.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMeshQuality( _
   ByVal NMeshQuality As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidBody
Dim NMeshQuality As System.Integer
Dim value As System.Boolean

value = instance.SetMeshQuality(NMeshQuality)
```

### C#

```csharp
System.bool SetMeshQuality(
   System.int NMeshQuality
)
```

### C++/CLI

```cpp
System.bool SetMeshQuality(
   System.int NMeshQuality
)
```

### Parameters

- `NMeshQuality`: Mesh quality as defined in [swsMeshQuality_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshQuality_e.html)

### Return Value

0 if successful

## VBA Syntax

See [CWSolidBody::SetMeshQuality](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidBody~SetMeshQuality.html).

## See Also

[ICWSolidBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody.html)
[ICWSolidBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody_members.html)

## Availability

SOLIDWORKS Simulation API 2020 SP0
