---
title: "FeatureBossThicken2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "FeatureBossThicken2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureBossThicken2.html"
---

# FeatureBossThicken2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::FeatureBossThicken2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureBossThicken2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub FeatureBossThicken2( _
   ByVal Thickness As System.Double, _
   ByVal Direction As System.Integer, _
   ByVal FaceIndex As System.Integer, _
   ByVal FillVolume As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Thickness As System.Double
Dim Direction As System.Integer
Dim FaceIndex As System.Integer
Dim FillVolume As System.Boolean

instance.FeatureBossThicken2(Thickness, Direction, FaceIndex, FillVolume)
```

### C#

```csharp
void FeatureBossThicken2(
   System.double Thickness,
   System.int Direction,
   System.int FaceIndex,
   System.bool FillVolume
)
```

### C++/CLI

```cpp
void FeatureBossThicken2(
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

See [ModelDoc::FeatureBossThicken2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~FeatureBossThicken2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
