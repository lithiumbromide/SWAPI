---
title: "FeatureFillet5 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FeatureFillet5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureFillet5.html"
---

# FeatureFillet5 Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::FeatureFillet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureFillet.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureFillet5( _
   ByVal Options As System.Integer, _
   ByVal R1 As System.Double, _
   ByVal Ftyp As System.Integer, _
   ByVal OverflowType As System.Integer, _
   ByVal Radii As System.Object, _
   ByVal SetBackDistances As System.Object, _
   ByVal PointRadiusArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Options As System.Integer
Dim R1 As System.Double
Dim Ftyp As System.Integer
Dim OverflowType As System.Integer
Dim Radii As System.Object
Dim SetBackDistances As System.Object
Dim PointRadiusArray As System.Object
Dim value As System.Integer

value = instance.FeatureFillet5(Options, R1, Ftyp, OverflowType, Radii, SetBackDistances, PointRadiusArray)
```

### C#

```csharp
System.int FeatureFillet5(
   System.int Options,
   System.double R1,
   System.int Ftyp,
   System.int OverflowType,
   System.object Radii,
   System.object SetBackDistances,
   System.object PointRadiusArray
)
```

### C++/CLI

```cpp
System.int FeatureFillet5(
   System.int Options,
   System.double R1,
   System.int Ftyp,
   System.int OverflowType,
   System.Object^ Radii,
   System.Object^ SetBackDistances,
   System.Object^ PointRadiusArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`:
- `R1`:
- `Ftyp`:
- `OverflowType`:
- `Radii`:
- `SetBackDistances`:
- `PointRadiusArray`:

## VBA Syntax

See [ModelDoc2::FeatureFillet5](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FeatureFillet5.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
