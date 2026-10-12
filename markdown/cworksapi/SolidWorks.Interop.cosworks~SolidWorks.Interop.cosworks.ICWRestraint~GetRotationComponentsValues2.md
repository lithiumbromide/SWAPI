---
title: "GetRotationComponentsValues2 Method (ICWRestraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRestraint"
member: "GetRotationComponentsValues2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetRotationComponentsValues2.html"
---

# GetRotationComponentsValues2 Method (ICWRestraint)

Gets the rotational components of this restraint.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetRotationComponentsValues2( _
   ByRef BVal1 As System.Boolean, _
   ByRef BVal2 As System.Boolean, _
   ByRef BVal3 As System.Boolean, _
   ByRef DVal1 As System.Double, _
   ByRef DVal2 As System.Double, _
   ByRef DVal3 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRestraint
Dim BVal1 As System.Boolean
Dim BVal2 As System.Boolean
Dim BVal3 As System.Boolean
Dim DVal1 As System.Double
Dim DVal2 As System.Double
Dim DVal3 As System.Double

instance.GetRotationComponentsValues2(BVal1, BVal2, BVal3, DVal1, DVal2, DVal3)
```

### C#

```csharp
void GetRotationComponentsValues2(
   out System.bool BVal1,
   out System.bool BVal2,
   out System.bool BVal3,
   out System.double DVal1,
   out System.double DVal2,
   out System.double DVal3
)
```

### C++/CLI

```cpp
void GetRotationComponentsValues2(
   [Out] System.bool BVal1,
   [Out] System.bool BVal2,
   [Out] System.bool BVal3,
   [Out] System.double DVal1,
   [Out] System.double DVal2,
   [Out] System.double DVal3
)
```

### Parameters

- `BVal1`: -1 or true to use DVal1 , 0 or false to not (see **Remarks**)
- `BVal2`: -1 or true to use DVal2, 0 or false to not (see **Remarks**)
- `BVal3`: -1 or true to use DVal3, 0 or false to not (see **Remarks**)
- `DVal1`: (see **Remarks**)
- `DVal2`: (see **Remarks**)
- `DVal3`: (see **Remarks**)

## VBA Syntax

See [CWRestraint::GetRotationComponentsValues2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRestraint~GetRotationComponentsValues2.html).

## Remarks

This method is valid only for beams and shell meshes with [ICWRestraint::RestraintType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~RestraintType.html) set to:

- [swsRestraintType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRestraintType_e.html).swsRestraintTypeCylindricalFaces
- swsRestraintType_e.swsRestaintTypeReferenceGeometry
- swsRestraintType_e.swsRestraintTypeSphericalSurface
  - or -
- swsRestraintType_e.swsRestraintTypeFlatFace

This method returns booleans or integers in out parameters BVal1-3, depending on their prior declarations.

If out parameters BVal1-3 are cast as:

- Booleans, true or false is returned in each out parameter.
- Longs or integers, -1 (=true) or 0 (=false) is returned in each out parameter.

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

## Availability

SOLIDWORKS Simulation API 2021 SP04
