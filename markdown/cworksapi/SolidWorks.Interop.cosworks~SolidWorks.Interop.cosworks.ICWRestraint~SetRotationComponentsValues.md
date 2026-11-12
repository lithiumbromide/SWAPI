---
title: "SetRotationComponentsValues Method (ICWRestraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRestraint"
member: "SetRotationComponentsValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetRotationComponentsValues.html"
---

# SetRotationComponentsValues Method (ICWRestraint)

Obsolete. Superseded by [ICWRestraint::SetRotationComponentsValues2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetRotationComponentsValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetRotationComponentsValues( _
   ByVal BVal1 As System.Integer, _
   ByVal BVal2 As System.Integer, _
   ByVal BVal3 As System.Integer, _
   ByVal DVal1 As System.Double, _
   ByVal DVal2 As System.Double, _
   ByVal DVal3 As System.Double _
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

instance.SetRotationComponentsValues(BVal1, BVal2, BVal3, DVal1, DVal2, DVal3)
```

### C#

```csharp
void SetRotationComponentsValues(
   System.int BVal1,
   System.int BVal2,
   System.int BVal3,
   System.double DVal1,
   System.double DVal2,
   System.double DVal3
)
```

### C++/CLI

```cpp
void SetRotationComponentsValues(
   System.int BVal1,
   System.int BVal2,
   System.int BVal3,
   System.double DVal1,
   System.double DVal2,
   System.double DVal3
)
```

### Parameters

- `BVal1`: 1 to set DVal1, 0 to not
- `BVal2`: 1 to set DVal2, 0 to not
- `BVal3`: 1 to set DVal3, 0 to not
- `DVal1`: (see **Remarks**)
- `DVal2`: (see **Remarks**)
- `DVal3`: (see **Remarks**)

## VBA Syntax

See [CWRestraint::SetRotationComponentsValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRestraint~SetRotationComponentsValues.html).

## Remarks

This method is valid only for beams and shell meshes with [ICWRestraint::RestraintType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~RestraintType.html) set to:

- [swsRestraintType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRestraintType_e.html).swsRestraintTypeCylindricalFaces
- swsRestraintType_e.swsRestaintTypeReferenceGeometry
- swsRestraintType_e.swsRestraintTypeSphericalSurface
  - or -
- swsRestraintType_e.swsRestraintTypeFlatFace

| If the direction reference of this restraint is... | Then set... |
| --- | --- |
| An axis or cylindrical face | DVal1 in the radial direction, DVal2 in the circumferential direction, and DVal3 in the axial direction. |
| A spherical face | DVal1 in the radial direction, DVal2 in the longitudinal direction, and DVal3 in the latitudinal direction. |
| A flat face | DVal1 about face direction 1, DVal2 about face direction 2, and DVal3 about the normal to the face. |
| A model edge | DVal3 about the edge. |

Call [ICWRestraint::SetReferenceGeometry](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetReferenceGeometry.html) to set the direction reference of this restraint.

## See Also

[ICWRestraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)
[ICWRestraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint_members.html)
[ICWRestraint::GetRotationComponentsValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetRotationComponentsValues.html)
[ICWRestraint::SetTranslationComponentsValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetTranslationComponentsValues.html)
[ICWRestraint::SetReverseDirections Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetReverseDirections.html)
[ICWRestraint::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~Unit.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
