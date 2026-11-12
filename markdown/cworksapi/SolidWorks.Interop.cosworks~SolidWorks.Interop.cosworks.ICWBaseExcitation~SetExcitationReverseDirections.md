---
title: "SetExcitationReverseDirections Method (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "SetExcitationReverseDirections"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetExcitationReverseDirections.html"
---

# SetExcitationReverseDirections Method (ICWBaseExcitation)

Obsolete. Superseded by [ICWBaseExcitation::SetExcitationReverseDirections2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetExcitationReverseDirections2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetExcitationReverseDirections( _
   ByVal BDir1 As System.Integer, _
   ByVal BDir2 As System.Integer, _
   ByVal BDir3 As System.Integer, _
   ByVal BReversePhaseAngle As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim BDir1 As System.Integer
Dim BDir2 As System.Integer
Dim BDir3 As System.Integer
Dim BReversePhaseAngle As System.Integer

instance.SetExcitationReverseDirections(BDir1, BDir2, BDir3, BReversePhaseAngle)
```

### C#

```csharp
void SetExcitationReverseDirections(
   System.int BDir1,
   System.int BDir2,
   System.int BDir3,
   System.int BReversePhaseAngle
)
```

### C++/CLI

```cpp
void SetExcitationReverseDirections(
   System.int BDir1,
   System.int BDir2,
   System.int BDir3,
   System.int BReversePhaseAngle
)
```

### Parameters

- `BDir1`: 1 to reverse plane direction 1, 0 to not (see **Remarks**)
- `BDir2`: 1 to reverse plane direction 2, 0 to not (see **Remarks**)
- `BDir3`: 1 to reverse plane direction 3, 0 to not (see **Remarks**)
- `BReversePhaseAngle`: 1 to reverse phase angle, 0 to not (see **Remarks**)

## VBA Syntax

See [CWBaseExcitation::SetExcitationReverseDirections](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBaseExcitation~SetExcitationReverseDirections.html).

## Remarks

For uniform base excitations, you can specify the direction of excitation by calling:

- this method, [ICWBaseExcitation::SetExcitationDirections](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~SetExcitationDirections.html), and [ICWBaseExcitation::SetExcitationDirectionValues](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetExcitationDirectionValues.html) to explicitly specify the excitation direction components and values

- or -

- [ICWBaseExcitation::SetDirectionEntityForUniformExcitation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~SetDirectionEntityForUniformExcitation.html) to specify the face, edge, or plane in whose direction the excitation is uniformly applied.

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)
[ICWBaseExcitation::GetExcitationReverseDirections Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetExcitationReverseDirections.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
