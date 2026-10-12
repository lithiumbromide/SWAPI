---
title: "FeatureCutThicken Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "FeatureCutThicken"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureCutThicken.html"
---

# FeatureCutThicken Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::FeatureCutThicken](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureCutThicken.html).

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
Dim instance As IModelDoc
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

See [ModelDoc::FeatureCutThicken](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~FeatureCutThicken.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
