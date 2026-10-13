---
title: "SetReverseDirections2 Method (ICWRestraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRestraint"
member: "SetReverseDirections2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetReverseDirections2.html"
---

# SetReverseDirections2 Method (ICWRestraint)

Sets whether to reverse the translation and rotation component directions for this restraint.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReverseDirections2( _
   ByVal BVal1 As System.Boolean, _
   ByVal BVal2 As System.Boolean, _
   ByVal BVal3 As System.Boolean, _
   ByVal BVal4 As System.Boolean, _
   ByVal BVal5 As System.Boolean, _
   ByVal BVal6 As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRestraint
Dim BVal1 As System.Boolean
Dim BVal2 As System.Boolean
Dim BVal3 As System.Boolean
Dim BVal4 As System.Boolean
Dim BVal5 As System.Boolean
Dim BVal6 As System.Boolean

instance.SetReverseDirections2(BVal1, BVal2, BVal3, BVal4, BVal5, BVal6)
```

### C#

```csharp
void SetReverseDirections2(
   System.bool BVal1,
   System.bool BVal2,
   System.bool BVal3,
   System.bool BVal4,
   System.bool BVal5,
   System.bool BVal6
)
```

### C++/CLI

```cpp
void SetReverseDirections2(
   System.bool BVal1,
   System.bool BVal2,
   System.bool BVal3,
   System.bool BVal4,
   System.bool BVal5,
   System.bool BVal6
)
```

### Parameters

- `BVal1`: -1 or true to reverse plane direction 1, 0 or false to not; valid only if BVal1 of [ICWRestraint::GetTranslationComponentsValues2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetTranslationComponentsValues2.html) is set to -1 or true (see **Remarks**)
- `BVal2`: -1 or true to reverse plane direction 2, 0 or false to not; valid only if BVal2 of ICWRestraint::GetTranslationComponentsValues2 is set to -1 or true (see **Remarks**)
- `BVal3`: -1 or true to reverse the normal to the plane, 0 or false to not; valid only if BVal3 of ICWRestraint::GetTranslationComponentsValues2 is set to -1 or true (see **Remarks**)
- `BVal4`: -1 or true to reverse radial direction, 0 or false to not; valid only if BVal1 of [ICWRestraint::GetRotationComponentsValues2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetRotationComponentsValues2.html) is set to -1 or true (see **Remarks**)
- `BVal5`: -1 or true to reverse circumferential direction, 0 or false to not; valid only if BVal2 of ICWRestraint::GetRotationComponentsValues2 is set to -1 or true (see **Remarks**)
- `BVal6`: -1 or true to reverse axial direction, 0 or false to not; valid only if BVal3 of ICWRestraint::GetRotationComponentsValues2 is set to -1 or true (see **Remarks**)

## VBA Syntax

See [CWRestraint::SetReverseDirections2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRestraint~SetReverseDirections2.html).

## Remarks

Specify booleans or integers in parameters BVal1-6: true = -1 and false = 0.

## See Also

[ICWRestraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)
[ICWRestraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
