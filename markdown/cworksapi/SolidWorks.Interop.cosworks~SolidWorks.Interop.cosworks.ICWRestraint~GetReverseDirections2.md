---
title: "GetReverseDirections2 Method (ICWRestraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRestraint"
member: "GetReverseDirections2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetReverseDirections2.html"
---

# GetReverseDirections2 Method (ICWRestraint)

Gets whether to reverse the translation and rotation component directions for this restraint.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetReverseDirections2( _
   ByRef BVal1 As System.Boolean, _
   ByRef BVal2 As System.Boolean, _
   ByRef BVal3 As System.Boolean, _
   ByRef BVal4 As System.Boolean, _
   ByRef BVal5 As System.Boolean, _
   ByRef BVal6 As System.Boolean _
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

instance.GetReverseDirections2(BVal1, BVal2, BVal3, BVal4, BVal5, BVal6)
```

### C#

```csharp
void GetReverseDirections2(
   out System.bool BVal1,
   out System.bool BVal2,
   out System.bool BVal3,
   out System.bool BVal4,
   out System.bool BVal5,
   out System.bool BVal6
)
```

### C++/CLI

```cpp
void GetReverseDirections2(
   [Out] System.bool BVal1,
   [Out] System.bool BVal2,
   [Out] System.bool BVal3,
   [Out] System.bool BVal4,
   [Out] System.bool BVal5,
   [Out] System.bool BVal6
)
```

### Parameters

- `BVal1`: -1 or true if plane direction 1 is reversed, 0 or false if not; valid only if BVal1 of [ICWRestraint::GetTranslationComponentsValues2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetTranslationComponentsValues2.html) is set to -1 or true (see **Remarks**)
- `BVal2`: -1 or true if plane direction 2 is reversed, 0 or false if not; valid only if BVal2 of ICWRestraint::GetTranslationComponentsValues2 is set to -1 or true (see **Remarks**)
- `BVal3`: -1 or true if normal to the plane is reversed, 0 or false if not; valid only if BVal3 of ICWRestraint::GetTranslationComponentsValues2 is set to -1 or true (see **Remarks**)
- `BVal4`: -1 or true if radial direction is reversed, 0 or false if not; valid only if BVal1 of [ICWRestraint::GetRotationComponentsValues2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetRotationComponentsValues2.html) is set to -1 or true (see **Remarks**)
- `BVal5`: -1 or true if circumferential direction is reversed, 0 or false if not; valid only if BVal2 of ICWRestraint::GetRotationComponentsValues2 is set to -1 or true (see **Remarks**)
- `BVal6`: -1 or true if axial direction is reversed, 0 or false if not; valid only if BVal3 of ICWRestraint::GetRotationComponentsValues2 is set to -1 or true (see **Remarks**)

## VBA Syntax

See [CWRestraint::GetReverseDirections2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRestraint~GetReverseDirections2.html).

## Remarks

This method returns booleans or integers in out parameters BVal1-6, depending on their prior declarations.

If out parameters BVal1-6 are cast as:

- Booleans, true or false is returned in each out parameter.
- Longs or integers, -1 (=true) or 0 (=false) is returned in each out parameter.

## See Also

[ICWRestraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)
[ICWRestraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
