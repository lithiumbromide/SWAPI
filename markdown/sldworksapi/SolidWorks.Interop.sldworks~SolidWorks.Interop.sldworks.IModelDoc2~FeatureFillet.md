---
title: "FeatureFillet Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FeatureFillet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureFillet.html"
---

# FeatureFillet Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::FeatureFillet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureFillet.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub FeatureFillet( _
   ByVal R1 As System.Double, _
   ByVal Propagate As System.Boolean, _
   ByVal Ftyp As System.Boolean, _
   ByVal VarRadTyp As System.Boolean, _
   ByVal OverflowType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim R1 As System.Double
Dim Propagate As System.Boolean
Dim Ftyp As System.Boolean
Dim VarRadTyp As System.Boolean
Dim OverflowType As System.Integer

instance.FeatureFillet(R1, Propagate, Ftyp, VarRadTyp, OverflowType)
```

### C#

```csharp
void FeatureFillet(
   System.double R1,
   System.bool Propagate,
   System.bool Ftyp,
   System.bool VarRadTyp,
   System.int OverflowType
)
```

### C++/CLI

```cpp
void FeatureFillet(
   System.double R1,
   System.bool Propagate,
   System.bool Ftyp,
   System.bool VarRadTyp,
   System.int OverflowType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `R1`:
- `Propagate`:
- `Ftyp`:
- `VarRadTyp`:
- `OverflowType`:

## VBA Syntax

See [ModelDoc2::FeatureFillet](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FeatureFillet.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
