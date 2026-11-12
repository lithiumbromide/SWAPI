---
title: "GetReverseDirections Method (ICWRestraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRestraint"
member: "GetReverseDirections"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetReverseDirections.html"
---

# GetReverseDirections Method (ICWRestraint)

Obsolete. Superseded by [ICWRestraint::GetReverseDirections2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetReverseDirections2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetReverseDirections( _
   ByRef BVal1 As System.Integer, _
   ByRef BVal2 As System.Integer, _
   ByRef BVal3 As System.Integer, _
   ByRef BVal4 As System.Integer, _
   ByRef BVal5 As System.Integer, _
   ByRef BVal6 As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRestraint
Dim BVal1 As System.Integer
Dim BVal2 As System.Integer
Dim BVal3 As System.Integer
Dim BVal4 As System.Integer
Dim BVal5 As System.Integer
Dim BVal6 As System.Integer

instance.GetReverseDirections(BVal1, BVal2, BVal3, BVal4, BVal5, BVal6)
```

### C#

```csharp
void GetReverseDirections(
   out System.int BVal1,
   out System.int BVal2,
   out System.int BVal3,
   out System.int BVal4,
   out System.int BVal5,
   out System.int BVal6
)
```

### C++/CLI

```cpp
void GetReverseDirections(
   [Out] System.int BVal1,
   [Out] System.int BVal2,
   [Out] System.int BVal3,
   [Out] System.int BVal4,
   [Out] System.int BVal5,
   [Out] System.int BVal6
)
```

### Parameters

- `BVal1`: 1 if plane direction 1 is reversed, 0 if not; valid only if BVal1 of [ICWRestraint::GetTranslationComponentsValues](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetTranslationComponentsValues.html) is set to 1
- `BVal2`: 1 if plane direction 2 is reversed, 0 if not; valid only if BVal2 of ICWRestraint::GetTranslationComponentsValues is set to 1
- `BVal3`: 1 if normal to the plane is reversed, 0 if not; valid only if BVal3 of ICWRestraint::GetTranslationComponentsValues is set to 1
- `BVal4`: 1 if radial direction is reversed, 0 if not; valid only if BVal1 of [ICWRestraint::GetRotationComponentsValues](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetRotationComponentsValues.html) is set to 1
- `BVal5`: 1 if circumferential direction is reversed, 0 if not; valid only if BVal2 of ICWRestraint::GetRotationComponentsValues is set to 1
- `BVal6`: 1 if axial direction is reversed, 0 if not; valid only if BVal3 of ICWRestraint::GetRotationComponentsValues is set to 1

## VBA Syntax

See [CWRestraint::GetReverseDirections](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRestraint~GetReverseDirections.html).

## Examples

See the [ICWRestraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html) examples.

## See Also

[ICWRestraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)
[ICWRestraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint_members.html)
[ICWRestraint::SetReverseDirections Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetReverseDirections.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
