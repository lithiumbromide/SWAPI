---
title: "FeatureFillet4 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "FeatureFillet4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureFillet4.html"
---

# FeatureFillet4 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::FeatureFillet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureFillet5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureFillet4( _
   ByVal R1 As System.Double, _
   ByVal Propagate As System.Boolean, _
   ByVal UniformRadius As System.Boolean, _
   ByVal Ftyp As System.Integer, _
   ByVal VarRadTyp As System.Boolean, _
   ByVal OverflowType As System.Integer, _
   ByVal NRadii As System.Integer, _
   ByVal Radii As System.Object, _
   ByVal UseHelpPoint As System.Boolean, _
   ByVal UseTangentHoldLine As System.Boolean, _
   ByVal CornerType As System.Boolean, _
   ByVal SetbackDistCount As System.Integer, _
   ByVal SetBackDistances As System.Object _
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
Dim Radii As System.Object
Dim UseHelpPoint As System.Boolean
Dim UseTangentHoldLine As System.Boolean
Dim CornerType As System.Boolean
Dim SetbackDistCount As System.Integer
Dim SetBackDistances As System.Object
Dim value As System.Integer

value = instance.FeatureFillet4(R1, Propagate, UniformRadius, Ftyp, VarRadTyp, OverflowType, NRadii, Radii, UseHelpPoint, UseTangentHoldLine, CornerType, SetbackDistCount, SetBackDistances)
```

### C#

```csharp
System.int FeatureFillet4(
   System.double R1,
   System.bool Propagate,
   System.bool UniformRadius,
   System.int Ftyp,
   System.bool VarRadTyp,
   System.int OverflowType,
   System.int NRadii,
   System.object Radii,
   System.bool UseHelpPoint,
   System.bool UseTangentHoldLine,
   System.bool CornerType,
   System.int SetbackDistCount,
   System.object SetBackDistances
)
```

### C++/CLI

```cpp
System.int FeatureFillet4(
   System.double R1,
   System.bool Propagate,
   System.bool UniformRadius,
   System.int Ftyp,
   System.bool VarRadTyp,
   System.int OverflowType,
   System.int NRadii,
   System.Object^ Radii,
   System.bool UseHelpPoint,
   System.bool UseTangentHoldLine,
   System.bool CornerType,
   System.int SetbackDistCount,
   System.Object^ SetBackDistances
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

See [ModelDoc::FeatureFillet4](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~FeatureFillet4.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
