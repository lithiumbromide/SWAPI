---
title: "SetExcitationDirections2 Method (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "SetExcitationDirections2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetExcitationDirections2.html"
---

# SetExcitationDirections2 Method (ICWBaseExcitation)

Sets the excitation directions.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetExcitationDirections2( _
   ByVal BDir1 As System.Boolean, _
   ByVal BDir2 As System.Boolean, _
   ByVal BDir3 As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim BDir1 As System.Boolean
Dim BDir2 As System.Boolean
Dim BDir3 As System.Boolean

instance.SetExcitationDirections2(BDir1, BDir2, BDir3)
```

### C#

```csharp
void SetExcitationDirections2(
   System.bool BDir1,
   System.bool BDir2,
   System.bool BDir3
)
```

### C++/CLI

```cpp
void SetExcitationDirections2(
   System.bool BDir1,
   System.bool BDir2,
   System.bool BDir3
)
```

### Parameters

- `BDir1`: -1 or true to set excitation along plane direction 1, 0 or false to not (see **Remarks**)
- `BDir2`: -1 or true to set excitation along plane direction 2, 0 or false to not (see **Remarks**)
- `BDir3`: -1 or true to set excitation along plane direction 3, 0 or false to not (see **Remarks**)

## Remarks

For uniform base excitations, you can specify the direction of excitation by calling either:

- this method, [ICWBaseExcitation::SetExcitationDirectionValues](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetExcitationDirectionValues.html), and [ICWBaseExcitation::SetExcitationReverseDirections2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetExcitationReverseDirections2.html) to explicitly specify the excitation direction components and values

- or -

- [ICWBaseExcitation::SetDirectionEntityForUniformExcitation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~SetDirectionEntityForUniformExcitation.html) to specify the face, edge, or plane in whose direction the excitation is uniformly applied.

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
