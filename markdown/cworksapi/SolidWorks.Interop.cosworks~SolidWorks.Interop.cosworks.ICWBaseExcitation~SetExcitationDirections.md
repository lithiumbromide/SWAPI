---
title: "SetExcitationDirections Method (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "SetExcitationDirections"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetExcitationDirections.html"
---

# SetExcitationDirections Method (ICWBaseExcitation)

Obsolete. Superseded by [ICWBaseExcitation::setExcitationDirections2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetExcitationDirections2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetExcitationDirections( _
   ByVal BDir1 As System.Integer, _
   ByVal BDir2 As System.Integer, _
   ByVal BDir3 As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim BDir1 As System.Integer
Dim BDir2 As System.Integer
Dim BDir3 As System.Integer

instance.SetExcitationDirections(BDir1, BDir2, BDir3)
```

### C#

```csharp
void SetExcitationDirections(
   System.int BDir1,
   System.int BDir2,
   System.int BDir3
)
```

### C++/CLI

```cpp
void SetExcitationDirections(
   System.int BDir1,
   System.int BDir2,
   System.int BDir3
)
```

### Parameters

- `BDir1`: 1 to set excitation along plane direction 1, 0 to not (see **Remarks**)
- `BDir2`: 1 to set excitation along plane direction 2, 0 to not (see **Remarks**)
- `BDir3`: 1 to set excitation along plane direction 3, 0 to not (see **Remarks**)

## VBA Syntax

See [CWBaseExcitation::SetExcitationDirections](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBaseExcitation~SetExcitationDirections.html).

## Remarks

For uniform base excitations, you can specify the direction of excitation by calling either:

- this method, [ICWBaseExcitation::SetExcitationDirectionValues](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~SetExcitationDirectionValues.html), and [ICWBaseExcitation::SetExcitationReverseDirections](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetExcitationReverseDirections.html) to explicitly specify the excitation direction components and values

- or -

- [ICWBaseExcitation::SetDirectionEntityForUniformExcitation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~SetDirectionEntityForUniformExcitation.html) to specify the face, edge, or plane in whose direction the excitation is uniformly applied.

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)
[ICWBaseExcitation::GetExcitationDirections Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetExcitationDirections.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
