---
title: "FeatureCut2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "FeatureCut2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureCut2.html"
---

# FeatureCut2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::FeatureCut2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureCut2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub FeatureCut2( _
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
   ByVal KeepPieceIndex As System.Integer _
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
Dim KeepPieceIndex As System.Integer

instance.FeatureCut2(Sd, Flip, Dir, T1, T2, D1, D2, Dchk1, Dchk2, Ddir1, Ddir2, Dang1, Dang2, OffsetReverse1, OffsetReverse2, KeepPieceIndex)
```

### C#

```csharp
void FeatureCut2(
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
   System.int KeepPieceIndex
)
```

### C++/CLI

```cpp
void FeatureCut2(
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
   System.int KeepPieceIndex
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
- `KeepPieceIndex`:

## VBA Syntax

See [ModelDoc::FeatureCut2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~FeatureCut2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
