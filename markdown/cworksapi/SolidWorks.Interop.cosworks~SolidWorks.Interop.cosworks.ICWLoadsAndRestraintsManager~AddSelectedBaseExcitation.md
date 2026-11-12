---
title: "AddSelectedBaseExcitation Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddSelectedBaseExcitation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddSelectedBaseExcitation.html"
---

# AddSelectedBaseExcitation Method (ICWLoadsAndRestraintsManager)

Obsolete. Superseded by [ICWLoadsAndRestraintsManager::AddSelectedBaseExcitation2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddSelectedBaseExcitation2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSelectedBaseExcitation( _
   ByVal NType As System.Integer, _
   ByVal SFixtureName As System.String, _
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
Dim SFixtureName As System.String
Dim NUnits As System.Integer
Dim BDir1 As System.Integer
Dim DVal1 As System.Double
Dim BDir2 As System.Integer
Dim DVal2 As System.Double
Dim BDir3 As System.Integer
Dim DVal3 As System.Double
Dim ErrorCode As System.Integer
Dim value As CWBaseExcitation

value = instance.AddSelectedBaseExcitation(NType, SFixtureName, NUnits, BDir1, DVal1, BDir2, DVal2, BDir3, DVal3, ErrorCode)
```

### C#

```csharp
CWBaseExcitation AddSelectedBaseExcitation(
   System.int NType,
   System.string SFixtureName,
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
CWBaseExcitation^ AddSelectedBaseExcitation(
   System.int NType,
   System.String^ SFixtureName,
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
- `SFixtureName`: Model entity to which the restraint is applied
- `NUnits`:

  | If NType is ... | Then units are as defined in ... |
  | --- | --- |
  | swsBaseExcitationType_e.swsBaseExcitationType_Displacement | swsLinearUnit_e |
  | swsBaseExcitationType_e.swsBaseExcitationType_Velocity | swsVelocityUnit_e |
  | swsBaseExcitationType_e.swsBaseExcitationType_Acceleration | swsAccelerationUnit_e |
- `BDir1`: 1 to add excitation along plane direction 1, 0 to not
- `DVal1`: Excitation along plane direction 1 (see **Remarks**)
- `BDir2`: 1 to add excitation along plane direction 2, 0 to not
- `DVal2`: Excitation along plane direction 2 (see **Remarks**)
- `BDir3`: 1 to add excitation along normal to plane, 0 to not
- `DVal3`: Excitation along normal to the plane (see **Remarks**)
- `ErrorCode`: Error code as defined in [swsRestraintError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRestraintError_e.html)

### Return Value

[ICWBaseExcitation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddSelectedBaseExcitation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddSelectedBaseExcitation.html).

## Remarks

Set negative values in DVal1, DVal2, and DVal3 to indicate reverse directions.

If this is a random vibration dynamic study, then DVal1, DVal2, and DVal3 are the Power Spectral Densities of the specified NType.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)
[ICWLoadsAndRestraintsManager::AddUniformBaseExcitation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddUniformBaseExcitation.html)
[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
