---
title: "FeatureCutThicken2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FeatureCutThicken2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureCutThicken2.html"
---

# FeatureCutThicken2 Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::FeatureCutThicken](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCutThicken.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub FeatureCutThicken2( _
   ByVal Thickness As System.Double, _
   ByVal Direction As System.Integer, _
   ByVal FaceIndex As System.Integer, _
   ByVal FillVolume As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Thickness As System.Double
Dim Direction As System.Integer
Dim FaceIndex As System.Integer
Dim FillVolume As System.Boolean

instance.FeatureCutThicken2(Thickness, Direction, FaceIndex, FillVolume)
```

### C#

```csharp
void FeatureCutThicken2(
   System.double Thickness,
   System.int Direction,
   System.int FaceIndex,
   System.bool FillVolume
)
```

### C++/CLI

```cpp
void FeatureCutThicken2(
   System.double Thickness,
   System.int Direction,
   System.int FaceIndex,
   System.bool FillVolume
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`:
- `Direction`:
- `FaceIndex`:
- `FillVolume`:

## VBA Syntax

See [ModelDoc2::FeatureCutThicken2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FeatureCutThicken2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
