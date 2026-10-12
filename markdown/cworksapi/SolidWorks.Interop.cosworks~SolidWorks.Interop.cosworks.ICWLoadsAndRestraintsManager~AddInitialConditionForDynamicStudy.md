---
title: "AddInitialConditionForDynamicStudy Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddInitialConditionForDynamicStudy"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddInitialConditionForDynamicStudy.html"
---

# AddInitialConditionForDynamicStudy Method (ICWLoadsAndRestraintsManager)

Obsolete. Superseded by [ICWLoadsAndRestraintsManager::AddInitialConditionForDynamicStudy2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddInitialConditionForDynamicStudy2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddInitialConditionForDynamicStudy( _
   ByVal NType As System.Integer, _
   ByVal NSelectionType As System.Integer, _
   ByVal DispArray As System.Object, _
   ByVal RefEntity As System.Object, _
   ByVal NUnits As System.Integer, _
   ByVal BDir1 As System.Integer, _
   ByVal DVal1 As System.Double, _
   ByVal BDir2 As System.Integer, _
   ByVal DVal2 As System.Double, _
   ByVal BDir3 As System.Integer, _
   ByVal DVal3 As System.Double, _
   ByRef ErrorCode As System.Integer _
) As CWDynamicInitialCondition
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim NType As System.Integer
Dim NSelectionType As System.Integer
Dim DispArray As System.Object
Dim RefEntity As System.Object
Dim NUnits As System.Integer
Dim BDir1 As System.Integer
Dim DVal1 As System.Double
Dim BDir2 As System.Integer
Dim DVal2 As System.Double
Dim BDir3 As System.Integer
Dim DVal3 As System.Double
Dim ErrorCode As System.Integer
Dim value As CWDynamicInitialCondition

value = instance.AddInitialConditionForDynamicStudy(NType, NSelectionType, DispArray, RefEntity, NUnits, BDir1, DVal1, BDir2, DVal2, BDir3, DVal3, ErrorCode)
```

### C#

```csharp
CWDynamicInitialCondition AddInitialConditionForDynamicStudy(
   System.int NType,
   System.int NSelectionType,
   System.object DispArray,
   System.object RefEntity,
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
CWDynamicInitialCondition^ AddInitialConditionForDynamicStudy(
   System.int NType,
   System.int NSelectionType,
   System.Object^ DispArray,
   System.Object^ RefEntity,
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

- `NType`: Type of dynamic initial condition as defined in [swsDynamicInitialConditionType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDynamicInitialConditionType_e.html)
- `NSelectionType`: Type of selection as defined in [swsSelectionType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSelectionType_e.html)
- `DispArray`: Array of components, bodies, or faces to which to apply the initial condition
- `RefEntity`: Face, edge, or plane reference geometry
- `NUnits`:

  | If NType is swsDynamicInitialConditionType_e.... | Then units are as defined in ... |
  | --- | --- |
  | swsDynamicInitialConditionType_Displacement | swsLinearUnit_e |
  | swsDynamicInitialConditionType_Velocity | swsVelocityUnit_e |
  | swsDynamicInitialConditionType_Acceleration | swsAccelerationUnit_e |
- `BDir1`: 1 to set a value along plane direction 1 or along a radial direction, 0 to not; valid only if RefEntity is set to a planar face, reference plane, cylindrical face, or null
- `DVal1`: Value along plane direction 1 or along a radial direction; valid only if BDir1 = 1
- `BDir2`: 1 to set a value along plane direction 2 or along a circumferential direction, 0 to not; valid only if RefEntity is set to a planar face, reference plane, cylindrical face, or null
- `DVal2`: Value along plane direction 2 or along a circumferential direction; valid only if BDir2 = 1
- `BDir3`: 1 to set a value along the normal to the plane or along an edge, 0 to not; valid only if RefEntity is set to a planar face, reference plane, cylindrical face, edge, or null
- `DVal3`: Value along the normal to the plane or along an edge; valid only if BDir3 = 1
- `ErrorCode`: Error code as defined in [swsDynamicInitialConditionError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDynamicInitialConditionError_e.html)

### Return Value

[ICWDynamicInitialCondition](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicInitialCondition.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddInitialConditionForDynamicStudy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddInitialConditionForDynamicStudy.html).

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
