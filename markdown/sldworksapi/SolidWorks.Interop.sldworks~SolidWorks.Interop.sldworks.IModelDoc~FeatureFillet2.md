---
title: "FeatureFillet2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "FeatureFillet2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureFillet2.html"
---

# FeatureFillet2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::FeatureFillet2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureFillet2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureFillet2( _
   ByVal R1 As System.Double, _
   ByVal Propagate As System.Boolean, _
   ByVal Ftyp As System.Boolean, _
   ByVal VarRadTyp As System.Boolean, _
   ByVal OverflowType As System.Integer, _
   ByVal NRadii As System.Integer, _
   ByVal Radii As System.Object _
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
Dim Radii As System.Object
Dim value As System.Integer

value = instance.FeatureFillet2(R1, Propagate, Ftyp, VarRadTyp, OverflowType, NRadii, Radii)
```

### C#

```csharp
System.int FeatureFillet2(
   System.double R1,
   System.bool Propagate,
   System.bool Ftyp,
   System.bool VarRadTyp,
   System.int OverflowType,
   System.int NRadii,
   System.object Radii
)
```

### C++/CLI

```cpp
System.int FeatureFillet2(
   System.double R1,
   System.bool Propagate,
   System.bool Ftyp,
   System.bool VarRadTyp,
   System.int OverflowType,
   System.int NRadii,
   System.Object^ Radii
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

See [ModelDoc::FeatureFillet2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~FeatureFillet2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
