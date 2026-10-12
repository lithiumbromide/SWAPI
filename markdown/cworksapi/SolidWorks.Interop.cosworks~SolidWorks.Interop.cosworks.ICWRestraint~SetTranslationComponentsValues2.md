---
title: "SetTranslationComponentsValues2 Method (ICWRestraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRestraint"
member: "SetTranslationComponentsValues2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetTranslationComponentsValues2.html"
---

# SetTranslationComponentsValues2 Method (ICWRestraint)

Sets the translation components for this restraint.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetTranslationComponentsValues2( _
   ByVal BVal1 As System.Boolean, _
   ByVal BVal2 As System.Boolean, _
   ByVal BVal3 As System.Boolean, _
   ByVal DVal1 As System.Double, _
   ByVal DVal2 As System.Double, _
   ByVal DVal3 As System.Double _
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

instance.SetTranslationComponentsValues2(BVal1, BVal2, BVal3, DVal1, DVal2, DVal3)
```

### C#

```csharp
void SetTranslationComponentsValues2(
   System.bool BVal1,
   System.bool BVal2,
   System.bool BVal3,
   System.double DVal1,
   System.double DVal2,
   System.double DVal3
)
```

### C++/CLI

```cpp
void SetTranslationComponentsValues2(
   System.bool BVal1,
   System.bool BVal2,
   System.bool BVal3,
   System.double DVal1,
   System.double DVal2,
   System.double DVal3
)
```

### Parameters

- `BVal1`: -1 or true to set DVal1, 0 or false to not (see **Remarks**)
- `BVal2`: -1 or true to set DVal2, 0 or false to not (see **Remarks**)
- `BVal3`: -1 or true to set DVal3, 0 or false to not (see **Remarks**)
- `DVal1`: (see **Remarks**)
- `DVal2`: (see **Remarks**)
- `DVal3`: (see **Remarks**)

## VBA Syntax

See [CWRestraint::SetTranslationComponentsValues2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRestraint~SetTranslationComponentsValues2.html).

## Remarks

This method is valid for all [ICWRestraint::RestraintType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~RestraintType.html)s except:

- [swsRestraintType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRestraintType_e.html).swsRestraintSymmetric
- swsRestraintType_e.swsRestaintTypeFixed
- swsRestraintType_e.swsRestraintTypeImmovable

Specify booleans or integers in parameters BVal1-3: true = -1 and false = 0.

| If the direction reference of this restraint is... | Then set... |
| --- | --- |
| An axis or cylindrical face | DVal1 in the radial direction, DVal2 in the circumferential direction, and DVal3 in the axial direction. |
| A spherical face | DVal1 in the radial direction, DVal2 in the longitudinal direction, and DVal3 in the latitudinal direction. |
| A flat face | DVal1 in face direction 1, DVal2 in face direction 2, and DVal3 in the normal to the face. |
| A model edge | DVal3 along the edge. |

Call [ICWRestraint::SetReferenceGeometry](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetReferenceGeometry.html) to set the direction reference of this restraint.

## See Also

[ICWRestraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)
[ICWRestraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
