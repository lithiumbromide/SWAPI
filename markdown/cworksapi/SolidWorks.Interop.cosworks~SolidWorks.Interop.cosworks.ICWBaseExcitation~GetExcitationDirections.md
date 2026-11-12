---
title: "GetExcitationDirections Method (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "GetExcitationDirections"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetExcitationDirections.html"
---

# GetExcitationDirections Method (ICWBaseExcitation)

Obsolete. Superseded by [ICWBaseExcitation::GetExcitationDirections2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetExcitationDirections2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetExcitationDirections( _
   ByRef BDir1 As System.Integer, _
   ByRef BDir2 As System.Integer, _
   ByRef BDir3 As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim BDir1 As System.Integer
Dim BDir2 As System.Integer
Dim BDir3 As System.Integer

instance.GetExcitationDirections(BDir1, BDir2, BDir3)
```

### C#

```csharp
void GetExcitationDirections(
   out System.int BDir1,
   out System.int BDir2,
   out System.int BDir3
)
```

### C++/CLI

```cpp
void GetExcitationDirections(
   [Out] System.int BDir1,
   [Out] System.int BDir2,
   [Out] System.int BDir3
)
```

### Parameters

- `BDir1`: 1 to get excitation along plane direction 1, 0 to not (see **Remarks**)
- `BDir2`: 1 to get excitation along plane direction 2, 0 to not (see **Remarks**)
- `BDir3`: 1 to get excitation along plane direction 3, 0 to not (see **Remarks**)

## VBA Syntax

See [CWBaseExcitation::GetExcitationDirections](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBaseExcitation~GetExcitationDirections.html).

## Remarks

For uniform base excitations, this method is valid only if you did not call [ICWBaseExcitation::SetDirectionEntityForUniformExcitation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~SetDirectionEntityForUniformExcitation.html) to set the face, edge, or plane in whose direction the excitation is uniformly applied.

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)
[ICWBaseExcitation::SetExcitationDirections Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetExcitationDirections.html)
[ICWBaseExcitation::GetExcitationDirectionValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetExcitationDirectionValues.html)
[ICWBaseExcitation::GetExcitationReverseDirections Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetExcitationReverseDirections.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
