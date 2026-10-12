---
title: "IFeatureFillet5 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IFeatureFillet5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFeatureFillet5.html"
---

# IFeatureFillet5 Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::FeatureCut](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCut.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IFeatureFillet5( _
   ByVal Options As System.Integer, _
   ByVal R1 As System.Double, _
   ByVal Ftyp As System.Integer, _
   ByVal OverflowType As System.Integer, _
   ByVal NRadii As System.Integer, _
   ByRef Radii As System.Double, _
   ByVal SetbackDistCount As System.Integer, _
   ByRef SetBackDistances As System.Double, _
   ByVal PointCount As System.Integer, _
   ByRef PointRadiusArray As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Options As System.Integer
Dim R1 As System.Double
Dim Ftyp As System.Integer
Dim OverflowType As System.Integer
Dim NRadii As System.Integer
Dim Radii As System.Double
Dim SetbackDistCount As System.Integer
Dim SetBackDistances As System.Double
Dim PointCount As System.Integer
Dim PointRadiusArray As System.Double
Dim value As System.Integer

value = instance.IFeatureFillet5(Options, R1, Ftyp, OverflowType, NRadii, Radii, SetbackDistCount, SetBackDistances, PointCount, PointRadiusArray)
```

### C#

```csharp
System.int IFeatureFillet5(
   System.int Options,
   System.double R1,
   System.int Ftyp,
   System.int OverflowType,
   System.int NRadii,
   ref System.double Radii,
   System.int SetbackDistCount,
   ref System.double SetBackDistances,
   System.int PointCount,
   ref System.double PointRadiusArray
)
```

### C++/CLI

```cpp
System.int IFeatureFillet5(
   System.int Options,
   System.double R1,
   System.int Ftyp,
   System.int OverflowType,
   System.int NRadii,
   System.double% Radii,
   System.int SetbackDistCount,
   System.double% SetBackDistances,
   System.int PointCount,
   System.double% PointRadiusArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`:
- `R1`:
- `Ftyp`: v
- `OverflowType`: v
- `NRadii`: v
- `Radii`: v
- `SetbackDistCount`: v
- `SetBackDistances`: v
- `PointCount`: v
- `PointRadiusArray`: v

## VBA Syntax

See [ModelDoc2::IFeatureFillet5](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IFeatureFillet5.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
