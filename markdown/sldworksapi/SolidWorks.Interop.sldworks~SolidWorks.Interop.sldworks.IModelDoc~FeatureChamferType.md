---
title: "FeatureChamferType Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "FeatureChamferType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureChamferType.html"
---

# FeatureChamferType Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::FeatureChamferType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureChamferType.html).

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
Dim instance As IModelDoc
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

See [ModelDoc::FeatureChamferType](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~FeatureChamferType.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
