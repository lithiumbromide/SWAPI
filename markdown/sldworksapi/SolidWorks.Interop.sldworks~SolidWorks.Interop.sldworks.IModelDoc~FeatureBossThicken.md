---
title: "FeatureBossThicken Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "FeatureBossThicken"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureBossThicken.html"
---

# FeatureBossThicken Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::FeatureBossThicken](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureBossThicken.html).

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
Dim instance As IModelDoc
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

See [ModelDoc::FeatureBossThicken](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~FeatureBossThicken.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
