---
title: "AddUniformBaseExcitation Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddUniformBaseExcitation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddUniformBaseExcitation.html"
---

# AddUniformBaseExcitation Method (ICWLoadsAndRestraintsManager)

Obsolete. Superseded by [ICWLoadsAndRestraintsManager::AddUniformBaseExcitation2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddUniformBaseExcitation2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddUniformBaseExcitation( _
   ByVal NType As System.Integer, _
   ByVal DirectionEntity As System.Object, _
   ByVal NUnits As System.Integer, _
   ByVal BDir1 As System.Integer, _
   ByVal DVal1 As System.Double, _
   ByVal BDir2 As System.Integer, _
   ByVal DVal2 As System.Double, _
   ByVal BDir3 As System.Integer, _
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
Dim BDir1 As System.Integer
Dim DVal1 As System.Double
Dim BDir2 As System.Integer
Dim DVal2 As System.Double
Dim BDir3 As System.Integer
Dim DVal3 As System.Double
Dim ErrorCode As System.Integer
Dim value As CWBaseExcitation

value = instance.AddUniformBaseExcitation(NType, DirectionEntity, NUnits, BDir1, DVal1, BDir2, DVal2, BDir3, DVal3, ErrorCode)
```

### C#

```csharp
CWBaseExcitation AddUniformBaseExcitation(
   System.int NType,
   System.object DirectionEntity,
   System.int NUnits,
   System.int BDir1,
   System.double DVal1,
   System.int BDir2,
   System.double DVal2,
   System.int BDir3,
   System.double DVal3,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWBaseExcitation^ AddUniformBaseExcitation(
   System.int NType,
   System.Object^ DirectionEntity,
   System.int NUnits,
   System.int BDir1,
   System.double DVal1,
   System.int BDir2,
   System.double DVal2,
   System.int BDir3,
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
- `BDir1`: 1 to add excitation along plane direction 1, 0 to not; valid only if DirectionEntity is a face, plane, or unspecified
- `DVal1`: Excitation along plane direction 1; valid only if BDir1 = 1 and DirectionEntity is a face, plane, or unspecified (see **Remarks**)
- `BDir2`: 1 to add excitation along plane direction 2; 0 to not; valid only if DirectionEntity is a face, plane, or unspecified
- `DVal2`: Excitation along plane direction 2; valid only if BDir2 = 1 and DirectionEntity is a face, plane, or unspecified (see **Remarks**)
- `BDir3`: 1 to add excitation along normal to the plane or along an edge; 0 to not; valid only if DirectionEntity is a face, edge plane, or unspecified
- `DVal3`: Excitation along normal to the plane or along an edge; valid only if BDir3 = 1 and DirectionEntity is a face, edge, plane, or unspecified (see **Remarks**)
- `ErrorCode`: Error code as defined in [swsRestraintError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRestraintError_e.html)

### Return Value

[ICWBaseExcitation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddUniformBaseExcitation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddUniformBaseExcitation.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## Remarks

Set negative values in DVal1, DVal2, and DVal3 to indicate reverse directions.

If this is a random vibration dynamic study, then DVal1, DVal2, and DVal3 are the Power Spectral Densities of the specified NType.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)
[ICWLoadsAndRestraintsManager::AddSelectedBaseExcitation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddSelectedBaseExcitation.html)
[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
