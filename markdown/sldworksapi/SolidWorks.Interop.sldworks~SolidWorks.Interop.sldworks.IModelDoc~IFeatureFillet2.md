---
title: "IFeatureFillet2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IFeatureFillet2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IFeatureFillet2.html"
---

# IFeatureFillet2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IFeatureFillet2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IFeatureFillet2.html).

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
Dim instance As IModelDoc
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

See [ModelDoc::IFeatureFillet2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IFeatureFillet2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
