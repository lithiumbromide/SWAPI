---
title: "AddInitialConditionForDynamicStudy2 Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddInitialConditionForDynamicStudy2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddInitialConditionForDynamicStudy2.html"
---

# AddInitialConditionForDynamicStudy2 Method (ICWLoadsAndRestraintsManager)

Creates the initial (time = 0) condition for displacements, velocities, or accelerations in modal time history and nonlinear dynamic studies.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddInitialConditionForDynamicStudy2( _
   ByVal NType As System.Integer, _
   ByVal NSelectionType As System.Integer, _
   ByVal DispArray As System.Object, _
   ByVal RefEntity As System.Object, _
   ByVal NUnits As System.Integer, _
   ByVal BDir1 As System.Boolean, _
   ByVal DVal1 As System.Double, _
   ByVal BDir2 As System.Boolean, _
   ByVal DVal2 As System.Double, _
   ByVal BDir3 As System.Boolean, _
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
Dim BDir1 As System.Boolean
Dim DVal1 As System.Double
Dim BDir2 As System.Boolean
Dim DVal2 As System.Double
Dim BDir3 As System.Boolean
Dim DVal3 As System.Double
Dim ErrorCode As System.Integer
Dim value As CWDynamicInitialCondition

value = instance.AddInitialConditionForDynamicStudy2(NType, NSelectionType, DispArray, RefEntity, NUnits, BDir1, DVal1, BDir2, DVal2, BDir3, DVal3, ErrorCode)
```

### C#

```csharp
CWDynamicInitialCondition AddInitialConditionForDynamicStudy2(
   System.int NType,
   System.int NSelectionType,
   System.object DispArray,
   System.object RefEntity,
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
CWDynamicInitialCondition^ AddInitialConditionForDynamicStudy2(
   System.int NType,
   System.int NSelectionType,
   System.Object^ DispArray,
   System.Object^ RefEntity,
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
- `BDir1`: -1 or true to set a value along plane direction 1 or along a radial direction, 0 or false to not; valid only if RefEntity is set to a planar face, reference plane, cylindrical face, or null
- `DVal1`: Value along plane direction 1 or along a radial direction; valid only if BDir1 = -1
- `BDir2`: -1 or true to set a value along plane direction 2 or along a circumferential direction, 0 or false to not; valid only if RefEntity is set to a planar face, reference plane, cylindrical face, or null
- `DVal2`: Value along plane direction 2 or along a circumferential direction; valid only if BDir2 = -1
- `BDir3`: -1 or true to set a value along the normal to the plane or along an edge, 0 or false to not; valid only if RefEntity is set to a planar face, reference plane, cylindrical face, edge, or null
- `DVal3`: Value along the normal to the plane or along an edge; valid only if BDir3 = -1
- `ErrorCode`: Error code as defined in [swsDynamicInitialConditionError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDynamicInitialConditionError_e.html)

### Return Value

[ICWDynamicInitialCondition](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicInitialCondition.html)

## Examples

See the [ICWDynamicInitialCondition](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html) examples.

## Remarks

This method returns booleans or integers in out parameters BDir1, BDir2, and BDir3, depending on their prior declarations.

If out parameters BDir1, BDir2, and BDir3 are cast as:

- Booleans, true or false is returned in each out parameter.
- Longs or integers, -1 (=true) or 0 (=false) is returned in each out parameter.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
