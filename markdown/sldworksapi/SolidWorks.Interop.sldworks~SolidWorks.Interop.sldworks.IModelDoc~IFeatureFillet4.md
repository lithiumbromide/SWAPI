---
title: "IFeatureFillet4 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IFeatureFillet4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IFeatureFillet4.html"
---

# IFeatureFillet4 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IFeatureFillet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IFeatureFillet4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IFeatureFillet4( _
   ByVal R1 As System.Double, _
   ByVal Propagate As System.Boolean, _
   ByVal UniformRadius As System.Boolean, _
   ByVal Ftyp As System.Integer, _
   ByVal VarRadTyp As System.Boolean, _
   ByVal OverflowType As System.Integer, _
   ByVal NRadii As System.Integer, _
   ByRef Radii As System.Double, _
   ByVal UseHelpPoint As System.Boolean, _
   ByVal UseTangentHoldLine As System.Boolean, _
   ByVal CornerType As System.Boolean, _
   ByVal SetbackDistCount As System.Integer, _
   ByRef SetBackDistances As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim R1 As System.Double
Dim Propagate As System.Boolean
Dim UniformRadius As System.Boolean
Dim Ftyp As System.Integer
Dim VarRadTyp As System.Boolean
Dim OverflowType As System.Integer
Dim NRadii As System.Integer
Dim Radii As System.Double
Dim UseHelpPoint As System.Boolean
Dim UseTangentHoldLine As System.Boolean
Dim CornerType As System.Boolean
Dim SetbackDistCount As System.Integer
Dim SetBackDistances As System.Double
Dim value As System.Integer

value = instance.IFeatureFillet4(R1, Propagate, UniformRadius, Ftyp, VarRadTyp, OverflowType, NRadii, Radii, UseHelpPoint, UseTangentHoldLine, CornerType, SetbackDistCount, SetBackDistances)
```

### C#

```csharp
System.int IFeatureFillet4(
   System.double R1,
   System.bool Propagate,
   System.bool UniformRadius,
   System.int Ftyp,
   System.bool VarRadTyp,
   System.int OverflowType,
   System.int NRadii,
   ref System.double Radii,
   System.bool UseHelpPoint,
   System.bool UseTangentHoldLine,
   System.bool CornerType,
   System.int SetbackDistCount,
   ref System.double SetBackDistances
)
```

### C++/CLI

```cpp
System.int IFeatureFillet4(
   System.double R1,
   System.bool Propagate,
   System.bool UniformRadius,
   System.int Ftyp,
   System.bool VarRadTyp,
   System.int OverflowType,
   System.int NRadii,
   System.double% Radii,
   System.bool UseHelpPoint,
   System.bool UseTangentHoldLine,
   System.bool CornerType,
   System.int SetbackDistCount,
   System.double% SetBackDistances
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `R1`:
- `Propagate`:
- `UniformRadius`:
- `Ftyp`:
- `VarRadTyp`:
- `OverflowType`:
- `NRadii`:
- `Radii`:
- `UseHelpPoint`:
- `UseTangentHoldLine`:
- `CornerType`:
- `SetbackDistCount`:
- `SetBackDistances`:

## VBA Syntax

See [ModelDoc::IFeatureFillet4](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IFeatureFillet4.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
