---
title: "GetTranslationComponentsValues Method (ICWRestraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRestraint"
member: "GetTranslationComponentsValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetTranslationComponentsValues.html"
---

# GetTranslationComponentsValues Method (ICWRestraint)

Obsolete. Superseded by [ICWRestraint::GetTranslationComponentsValues2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetTranslationComponentsValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetTranslationComponentsValues( _
   ByRef BVal1 As System.Integer, _
   ByRef BVal2 As System.Integer, _
   ByRef BVal3 As System.Integer, _
   ByRef DVal1 As System.Double, _
   ByRef DVal2 As System.Double, _
   ByRef DVal3 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRestraint
Dim BVal1 As System.Integer
Dim BVal2 As System.Integer
Dim BVal3 As System.Integer
Dim DVal1 As System.Double
Dim DVal2 As System.Double
Dim DVal3 As System.Double

instance.GetTranslationComponentsValues(BVal1, BVal2, BVal3, DVal1, DVal2, DVal3)
```

### C#

```csharp
void GetTranslationComponentsValues(
   out System.int BVal1,
   out System.int BVal2,
   out System.int BVal3,
   out System.double DVal1,
   out System.double DVal2,
   out System.double DVal3
)
```

### C++/CLI

```cpp
void GetTranslationComponentsValues(
   [Out] System.int BVal1,
   [Out] System.int BVal2,
   [Out] System.int BVal3,
   [Out] System.double DVal1,
   [Out] System.double DVal2,
   [Out] System.double DVal3
)
```

### Parameters

- `BVal1`: 1 to use DVal1, 0 to not
- `BVal2`: 1 to use DVal2, 0 to not
- `BVal3`: 1 to use DVal3, 0 to not
- `DVal1`: (see **Remarks**)
- `DVal2`: (see **Remarks**)
- `DVal3`: (see **Remarks**)

## VBA Syntax

See [CWRestraint::GetTranslationComponentsValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRestraint~GetTranslationComponentsValues.html).

## Examples

See the [ICWRestraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html) examples.

## Remarks

This method is valid for all [ICWRestraint::RestraintType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~RestraintType.html)s except:

- [swsRestraintType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRestraintType_e.html).swsRestraintSymmetric
- swsRestraintType_e.swsRestaintTypeFixed
- swsRestraintType_e.swsRestraintTypeImmovable

| If the direction reference of this restraint is... | Then... |
| --- | --- |
| An axis or cylindrical face | DVal1 is in the radial direction, DVal2 is in the circumferential direction, and DVal3 is in the axial direction. |
| A spherical face | DVal1 is in the radial direction, DVal2 is in the longitudinal direction, and DVal3 is in the latitudinal direction. |
| A flat face | DVal1 is in face direction 1, DVal2 is in face direction 2, and DVal3 is in the normal to the face. |
| A model edge | DVal3 is along the edge. |

Call [ICWRestraint::SetReferenceGeometry](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetReferenceGeometry.html) to set the direction reference of this restraint.

## See Also

[ICWRestraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)
[ICWRestraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint_members.html)
[ICWRestraint::SetTranslationComponentsValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetTranslationComponentsValues.html)
[ICWRestraint::GetRotationComponentsValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetRotationComponentsValues.html)
[ICWRestraint::GetReverseDirections Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetReverseDirections.html)
[ICWRestraint::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~Unit.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
