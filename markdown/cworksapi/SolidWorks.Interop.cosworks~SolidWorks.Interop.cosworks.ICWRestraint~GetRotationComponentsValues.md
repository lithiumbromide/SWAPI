---
title: "GetRotationComponentsValues Method (ICWRestraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRestraint"
member: "GetRotationComponentsValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetRotationComponentsValues.html"
---

# GetRotationComponentsValues Method (ICWRestraint)

Obsolete. Superseded by [ICWRestraint::GetRotationComponentsValues2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetRotationComponentsValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetRotationComponentsValues( _
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

instance.GetRotationComponentsValues(BVal1, BVal2, BVal3, DVal1, DVal2, DVal3)
```

### C#

```csharp
void GetRotationComponentsValues(
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
void GetRotationComponentsValues(
   [Out] System.int BVal1,
   [Out] System.int BVal2,
   [Out] System.int BVal3,
   [Out] System.double DVal1,
   [Out] System.double DVal2,
   [Out] System.double DVal3
)
```

### Parameters

- `BVal1`: 1 to use DVal1 , 0 to not
- `BVal2`: 1 to use DVal2, 0 to not
- `BVal3`: 1 to use DVal3, 0 to not
- `DVal1`: (see **Remarks**)
- `DVal2`: (see **Remarks**)
- `DVal3`: (see **Remarks**)

## VBA Syntax

See [CWRestraint::GetRotationComponentsValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRestraint~GetRotationComponentsValues.html).

## Remarks

This method is valid only for beams and shell meshes with [ICWRestraint::RestraintType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~RestraintType.html) set to:

- [swsRestraintType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRestraintType_e.html).swsRestraintTypeCylindricalFaces
- swsRestraintType_e.swsRestaintTypeReferenceGeometry
- swsRestraintType_e.swsRestraintTypeSphericalSurface
  - or -
- swsRestraintType_e.swsRestraintTypeFlatFace

| If the direction reference of this restraint is... | Then... |
| --- | --- |
| An axis or cylindrical face | DVal1 is in the radial direction, DVal2 is in the circumferential direction, and DVal3 is in the axial direction. |
| A spherical face | DVal1 is in the radial direction, DVal2 is in the longitudinal direction, and DVal3 is in the latitudinal direction. |
| A flat face | DVal1 is about face direction 1, DVal2 is about face direction 2, and DVal3 is about the normal to the face. |
| A model edge | DVal3 is about the edge. |

Call [ICWRestraint::SetReferenceGeometry](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetReferenceGeometry.html) to set the direction reference of this restraint.

## See Also

[ICWRestraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)
[ICWRestraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint_members.html)
[ICWRestraint::SetRotationComponentsValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetRotationComponentsValues.html)
[ICWRestraint::GetReverseDirections Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetReverseDirections.html)
[ICWRestraint::GetTranslationComponentsValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetTranslationComponentsValues.html)
[ICWRestraint::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~Unit.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
