---
title: "IFeatureFillet2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IFeatureFillet2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFeatureFillet2.html"
---

# IFeatureFillet2 Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::FeatureCut](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCut.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IFeatureFillet2( _
   ByVal R1 As System.Double, _
   ByVal Propagate As System.Boolean, _
   ByVal Ftyp As System.Boolean, _
   ByVal VarRadTyp As System.Boolean, _
   ByVal OverflowType As System.Integer, _
   ByVal NRadii As System.Integer, _
   ByRef Radii As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim R1 As System.Double
Dim Propagate As System.Boolean
Dim Ftyp As System.Boolean
Dim VarRadTyp As System.Boolean
Dim OverflowType As System.Integer
Dim NRadii As System.Integer
Dim Radii As System.Double
Dim value As System.Integer

value = instance.IFeatureFillet2(R1, Propagate, Ftyp, VarRadTyp, OverflowType, NRadii, Radii)
```

### C#

```csharp
System.int IFeatureFillet2(
   System.double R1,
   System.bool Propagate,
   System.bool Ftyp,
   System.bool VarRadTyp,
   System.int OverflowType,
   System.int NRadii,
   ref System.double Radii
)
```

### C++/CLI

```cpp
System.int IFeatureFillet2(
   System.double R1,
   System.bool Propagate,
   System.bool Ftyp,
   System.bool VarRadTyp,
   System.int OverflowType,
   System.int NRadii,
   System.double% Radii
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `R1`:
- `Propagate`:
- `Ftyp`:
- `VarRadTyp`:
- `OverflowType`:
- `NRadii`:
- `Radii`:

## VBA Syntax

See [ModelDoc2::IFeatureFillet2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IFeatureFillet2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
