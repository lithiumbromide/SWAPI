---
title: "FeatureBossThicken Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FeatureBossThicken"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureBossThicken.html"
---

# FeatureBossThicken Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::FeatureBossThicken](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureBossThicken.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub FeatureBossThicken( _
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

instance.FeatureBossThicken(Thickness, Direction, FaceIndex)
```

### C#

```csharp
void FeatureBossThicken(
   System.double Thickness,
   System.int Direction,
   System.int FaceIndex
)
```

### C++/CLI

```cpp
void FeatureBossThicken(
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

See [ModelDoc2::FeatureBossThicken](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FeatureBossThicken.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
