---
title: "FeatureChamferType Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FeatureChamferType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureChamferType.html"
---

# FeatureChamferType Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertFeatureChamfer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertFeatureChamfer.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub FeatureChamferType( _
   ByVal ChamferType As System.Short, _
   ByVal Width As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Flip As System.Boolean, _
   ByVal OtherDist As System.Double, _
   ByVal VertexChamDist1 As System.Double, _
   ByVal VertexChamDist2 As System.Double, _
   ByVal VertexChamDist3 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ChamferType As System.Short
Dim Width As System.Double
Dim Angle As System.Double
Dim Flip As System.Boolean
Dim OtherDist As System.Double
Dim VertexChamDist1 As System.Double
Dim VertexChamDist2 As System.Double
Dim VertexChamDist3 As System.Double

instance.FeatureChamferType(ChamferType, Width, Angle, Flip, OtherDist, VertexChamDist1, VertexChamDist2, VertexChamDist3)
```

### C#

```csharp
void FeatureChamferType(
   System.short ChamferType,
   System.double Width,
   System.double Angle,
   System.bool Flip,
   System.double OtherDist,
   System.double VertexChamDist1,
   System.double VertexChamDist2,
   System.double VertexChamDist3
)
```

### C++/CLI

```cpp
void FeatureChamferType(
   System.short ChamferType,
   System.double Width,
   System.double Angle,
   System.bool Flip,
   System.double OtherDist,
   System.double VertexChamDist1,
   System.double VertexChamDist2,
   System.double VertexChamDist3
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ChamferType`:
- `Width`:
- `Angle`:
- `Flip`:
- `OtherDist`:
- `VertexChamDist1`:
- `VertexChamDist2`:
- `VertexChamDist3`:

## VBA Syntax

See [ModelDoc2::FeatureChamferType](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FeatureChamferType.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
