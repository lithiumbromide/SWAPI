---
title: "GetExcitationReverseDirections2 Method (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "GetExcitationReverseDirections2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetExcitationReverseDirections2.html"
---

# GetExcitationReverseDirections2 Method (ICWBaseExcitation)

Gets whether to reverse base excitation directions.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetExcitationReverseDirections2( _
   ByRef BDir1 As System.Boolean, _
   ByRef BDir2 As System.Boolean, _
   ByRef BDir3 As System.Boolean, _
   ByRef BReversePhaseAngle As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim BDir1 As System.Boolean
Dim BDir2 As System.Boolean
Dim BDir3 As System.Boolean
Dim BReversePhaseAngle As System.Boolean

instance.GetExcitationReverseDirections2(BDir1, BDir2, BDir3, BReversePhaseAngle)
```

### C#

```csharp
void GetExcitationReverseDirections2(
   out System.bool BDir1,
   out System.bool BDir2,
   out System.bool BDir3,
   out System.bool BReversePhaseAngle
)
```

### C++/CLI

```cpp
void GetExcitationReverseDirections2(
   [Out] System.bool BDir1,
   [Out] System.bool BDir2,
   [Out] System.bool BDir3,
   [Out] System.bool BReversePhaseAngle
)
```

### Parameters

- `BDir1`: -1 or true to reverse plane direction 1, 0 or false to not; valid only if BDir1 = -1 in [ICWBaseExcitation::GetExcitationDirections2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetExcitationDirections2.html) (see **Remarks**)
- `BDir2`: -1 or true to reverse plane direction 2, 0 or false to not; valid only if BDir2 = -1 in ICWBaseExcitation::GetExcitationDirections2 (see **Remarks**)
- `BDir3`: -1 or true to reverse plane direction 3, 0 or false to not; valid only if BDir3 = -1 in ICWBaseExcitation::GetExcitationDirections2 (see **Remarks**)
- `BReversePhaseAngle`: -1 or true to reverse phase angle, 0 or false to not

## Examples

See the [ICWBaseExcitation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html) examples.

## Remarks

For uniform base excitations, this method is valid only if you did not call [ICWBaseExcitation::SetDirectionEntityForUniformExcitation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~SetDirectionEntityForUniformExcitation.html) to set the face, edge, or plane in whose direction the excitation is uniformly applied.

This method returns booleans or integers in out parameters BDir1, BDir2, BDir3, and BReversePhaseAngle, depending on their prior declarations.

If out parameters BDir1, BDir2, BDir3, BReversePhaseAngle are cast as:

- Booleans, true or false is returned in each out parameter.
- Longs or integers, -1 (=true) or 0 (=false) is returned in each out parameter.

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
