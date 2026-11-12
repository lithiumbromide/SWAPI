---
title: "FeatureBossThin Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "FeatureBossThin"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureBossThin.html"
---

# FeatureBossThin Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::FeatureBossThin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureBossThin.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub FeatureBossThin( _
   ByVal Sd As System.Boolean, _
   ByVal Flip As System.Boolean, _
   ByVal Dir As System.Boolean, _
   ByVal T1 As System.Integer, _
   ByVal T2 As System.Integer, _
   ByVal D1 As System.Double, _
   ByVal D2 As System.Double, _
   ByVal Dchk1 As System.Boolean, _
   ByVal Dchk2 As System.Boolean, _
   ByVal Ddir1 As System.Boolean, _
   ByVal Ddir2 As System.Boolean, _
   ByVal Dang1 As System.Double, _
   ByVal Dang2 As System.Double, _
   ByVal OffsetReverse1 As System.Boolean, _
   ByVal OffsetReverse2 As System.Boolean, _
   ByVal Thk1 As System.Double, _
   ByVal Thk2 As System.Double, _
   ByVal EndThk As System.Double, _
   ByVal RevThinDir As System.Integer, _
   ByVal CapEnds As System.Integer, _
   ByVal AddBends As System.Boolean, _
   ByVal BendRad As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Sd As System.Boolean
Dim Flip As System.Boolean
Dim Dir As System.Boolean
Dim T1 As System.Integer
Dim T2 As System.Integer
Dim D1 As System.Double
Dim D2 As System.Double
Dim Dchk1 As System.Boolean
Dim Dchk2 As System.Boolean
Dim Ddir1 As System.Boolean
Dim Ddir2 As System.Boolean
Dim Dang1 As System.Double
Dim Dang2 As System.Double
Dim OffsetReverse1 As System.Boolean
Dim OffsetReverse2 As System.Boolean
Dim Thk1 As System.Double
Dim Thk2 As System.Double
Dim EndThk As System.Double
Dim RevThinDir As System.Integer
Dim CapEnds As System.Integer
Dim AddBends As System.Boolean
Dim BendRad As System.Double

instance.FeatureBossThin(Sd, Flip, Dir, T1, T2, D1, D2, Dchk1, Dchk2, Ddir1, Ddir2, Dang1, Dang2, OffsetReverse1, OffsetReverse2, Thk1, Thk2, EndThk, RevThinDir, CapEnds, AddBends, BendRad)
```

### C#

```csharp
void FeatureBossThin(
   System.bool Sd,
   System.bool Flip,
   System.bool Dir,
   System.int T1,
   System.int T2,
   System.double D1,
   System.double D2,
   System.bool Dchk1,
   System.bool Dchk2,
   System.bool Ddir1,
   System.bool Ddir2,
   System.double Dang1,
   System.double Dang2,
   System.bool OffsetReverse1,
   System.bool OffsetReverse2,
   System.double Thk1,
   System.double Thk2,
   System.double EndThk,
   System.int RevThinDir,
   System.int CapEnds,
   System.bool AddBends,
   System.double BendRad
)
```

### C++/CLI

```cpp
void FeatureBossThin(
   System.bool Sd,
   System.bool Flip,
   System.bool Dir,
   System.int T1,
   System.int T2,
   System.double D1,
   System.double D2,
   System.bool Dchk1,
   System.bool Dchk2,
   System.bool Ddir1,
   System.bool Ddir2,
   System.double Dang1,
   System.double Dang2,
   System.bool OffsetReverse1,
   System.bool OffsetReverse2,
   System.double Thk1,
   System.double Thk2,
   System.double EndThk,
   System.int RevThinDir,
   System.int CapEnds,
   System.bool AddBends,
   System.double BendRad
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sd`:
- `Flip`:
- `Dir`:
- `T1`:
- `T2`:
- `D1`:
- `D2`:
- `Dchk1`:
- `Dchk2`:
- `Ddir1`:
- `Ddir2`:
- `Dang1`:
- `Dang2`:
- `OffsetReverse1`:
- `OffsetReverse2`:
- `Thk1`:
- `Thk2`:
- `EndThk`:
- `RevThinDir`:
- `CapEnds`:
- `AddBends`:
- `BendRad`:

## VBA Syntax

See [ModelDoc::FeatureBossThin](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~FeatureBossThin.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
