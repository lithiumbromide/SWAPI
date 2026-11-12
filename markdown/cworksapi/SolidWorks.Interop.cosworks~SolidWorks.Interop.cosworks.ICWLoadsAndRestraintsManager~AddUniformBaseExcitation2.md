---
title: "AddUniformBaseExcitation2 Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddUniformBaseExcitation2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddUniformBaseExcitation2.html"
---

# AddUniformBaseExcitation2 Method (ICWLoadsAndRestraintsManager)

Adds a uniform base excitation to all locations restrained in the specified directions for dynamic studies.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddUniformBaseExcitation2( _
   ByVal NType As System.Integer, _
   ByVal DirectionEntity As System.Object, _
   ByVal NUnits As System.Integer, _
   ByVal BDir1 As System.Boolean, _
   ByVal DVal1 As System.Double, _
   ByVal BDir2 As System.Boolean, _
   ByVal DVal2 As System.Double, _
   ByVal BDir3 As System.Boolean, _
   ByVal DVal3 As System.Double, _
   ByRef ErrorCode As System.Integer _
) As CWBaseExcitation
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim NType As System.Integer
Dim DirectionEntity As System.Object
Dim NUnits As System.Integer
Dim BDir1 As System.Boolean
Dim DVal1 As System.Double
Dim BDir2 As System.Boolean
Dim DVal2 As System.Double
Dim BDir3 As System.Boolean
Dim DVal3 As System.Double
Dim ErrorCode As System.Integer
Dim value As CWBaseExcitation

value = instance.AddUniformBaseExcitation2(NType, DirectionEntity, NUnits, BDir1, DVal1, BDir2, DVal2, BDir3, DVal3, ErrorCode)
```

### C#

```csharp
CWBaseExcitation AddUniformBaseExcitation2(
   System.int NType,
   System.object DirectionEntity,
   System.int NUnits,
   System.bool BDir1,
   System.double DVal1,
   System.bool BDir2,
   System.double DVal2,
   System.bool BDir3,
   System.double DVal3,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWBaseExcitation^ AddUniformBaseExcitation2(
   System.int NType,
   System.Object^ DirectionEntity,
   System.int NUnits,
   System.bool BDir1,
   System.double DVal1,
   System.bool BDir2,
   System.double DVal2,
   System.bool BDir3,
   System.double DVal3,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NType`: Type of excitation as defined in [swsBaseExcitationType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsBaseExcitationType_e.html)
- `DirectionEntity`: Face, edge, or plane of direction for the excitation; null for global direction if Response Spectrum study
- `NUnits`:

  | If NType is ... | Then units are as defined in ... |
  | --- | --- |
  | swsBaseExcitationType_e.swsBaseExcitationType_Displacement | swsLinearUnit_e |
  | swsBaseExcitationType_e.swsBaseExcitationType_Velocity | swsVelocityUnit_e |
  | swsBaseExcitationType_e.swsBaseExcitationType_Acceleration | swsAccelerationUnit_e |
- `BDir1`: -1 or true to add excitation along plane direction 1, 0 or false to not; valid only if DirectionEntity is a face, plane, or unspecified
- `DVal1`: Excitation along plane direction 1; valid only if BDir1 = -1 and DirectionEntity is a face, plane, or unspecified (see **Remarks**)
- `BDir2`: -1 or true to add excitation along plane direction 2; 0 or false to not; valid only if DirectionEntity is a face, plane, or unspecified
- `DVal2`: Excitation along plane direction 2; valid only if BDir2 = -1 and DirectionEntity is a face, plane, or unspecified (see **Remarks**)
- `BDir3`: -1 or true to add excitation along normal to the plane or along an edge; 0 or false to not; valid only if DirectionEntity is a face, edge plane, or unspecified
- `DVal3`: Excitation along normal to the plane or along an edge; valid only if BDir3 = -1 and DirectionEntity is a face, edge, plane, or unspecified (see **Remarks**)
- `ErrorCode`: Error code as defined in [swsRestraintError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRestraintError_e.html)

### Return Value

[ICWBaseExcitation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation.html)

## Examples

See the [ICWBaseExcitation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html) examples.

## Remarks

This method returns booleans or integers in out parameters BDir1, BDir2, and BDir3, depending on their prior declarations.

If out parameters BDir1, BDir2, and BDir3 are cast as:

- Booleans, true or false is returned in each out parameter.
- Longs or integers, -1 (=true) or 0 (=false) is returned in each out parameter.

Set negative values in DVal1, DVal2, and DVal3 to indicate reverse directions.

If this is a random vibration dynamic study, then DVal1, DVal2, and DVal3 are the Power Spectral Densities of the specified NType.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
