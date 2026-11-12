---
title: "FeatureCutThicken Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FeatureCutThicken"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureCutThicken.html"
---

# FeatureCutThicken Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::FeatureCutThicken](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCutThicken.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub FeatureCutThicken( _
   ByVal Thickness As System.Double, _
   ByVal Direction As System.Integer, _
   ByVal FaceIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Thickness As System.Double
Dim Direction As System.Integer
Dim FaceIndex As System.Integer

instance.FeatureCutThicken(Thickness, Direction, FaceIndex)
```

### C#

```csharp
void FeatureCutThicken(
   System.double Thickness,
   System.int Direction,
   System.int FaceIndex
)
```

### C++/CLI

```cpp
void FeatureCutThicken(
   System.double Thickness,
   System.int Direction,
   System.int FaceIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`:
- `Direction`:
- `FaceIndex`:

## VBA Syntax

See [ModelDoc2::FeatureCutThicken](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FeatureCutThicken.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
