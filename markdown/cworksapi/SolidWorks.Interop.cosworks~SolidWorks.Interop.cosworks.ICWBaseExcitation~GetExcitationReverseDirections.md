---
title: "GetExcitationReverseDirections Method (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "GetExcitationReverseDirections"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetExcitationReverseDirections.html"
---

# GetExcitationReverseDirections Method (ICWBaseExcitation)

Obsolete. Superseded by [ICWBaseExcitation::GetExcitationReverseDirections2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetExcitationReverseDirections2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetExcitationReverseDirections( _
   ByRef BDir1 As System.Integer, _
   ByRef BDir2 As System.Integer, _
   ByRef BDir3 As System.Integer, _
   ByRef BReversePhaseAngle As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim BDir1 As System.Integer
Dim BDir2 As System.Integer
Dim BDir3 As System.Integer
Dim BReversePhaseAngle As System.Integer

instance.GetExcitationReverseDirections(BDir1, BDir2, BDir3, BReversePhaseAngle)
```

### C#

```csharp
void GetExcitationReverseDirections(
   out System.int BDir1,
   out System.int BDir2,
   out System.int BDir3,
   out System.int BReversePhaseAngle
)
```

### C++/CLI

```cpp
void GetExcitationReverseDirections(
   [Out] System.int BDir1,
   [Out] System.int BDir2,
   [Out] System.int BDir3,
   [Out] System.int BReversePhaseAngle
)
```

### Parameters

- `BDir1`: 1 to reverse plane direction 1, 0 to not; valid only if BDir1 = 1 in [ICWBaseExcitation::GetExcitationDirections](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetExcitationDirections.html) (see **Remarks**)
- `BDir2`: 1 to reverse plane direction 2, 0 to not; valid only if BDir2 = 1 in ICWBaseExcitation::GetExcitationDirections (see **Remarks**)
- `BDir3`: 1 to reverse plane direction 3, 0 to not; valid only if BDir3 = 1 in ICWBaseExcitation::GetExcitationDirections (see **Remarks**)
- `BReversePhaseAngle`: 1 to reverse phase angle, 0 to not

## VBA Syntax

See [CWBaseExcitation::GetExcitationReverseDirections](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBaseExcitation~GetExcitationReverseDirections.html).

## Remarks

For uniform base excitations, this method is valid only if you did not call [ICWBaseExcitation::SetDirectionEntityForUniformExcitation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~SetDirectionEntityForUniformExcitation.html) to set the face, edge, or plane in whose direction the excitation is uniformly applied.

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)
[ICWBaseExcitation::SetExcitationReverseDirections Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetExcitationReverseDirections.html)
[ICWBaseExcitation::GetExcitationDirectionValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetExcitationDirectionValues.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
