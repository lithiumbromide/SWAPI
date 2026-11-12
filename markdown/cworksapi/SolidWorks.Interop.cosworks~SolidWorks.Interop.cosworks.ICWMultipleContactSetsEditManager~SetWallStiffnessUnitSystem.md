---
title: "SetWallStiffnessUnitSystem Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "SetWallStiffnessUnitSystem"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetWallStiffnessUnitSystem.html"
---

# SetWallStiffnessUnitSystem Method (ICWMultipleContactSetsEditManager)

Sets the units of wall stiffness for flexible virtual wall contact sets to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetWallStiffnessUnitSystem( _
   ByVal NUnitSystem As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
Dim NUnitSystem As System.Integer
Dim value As System.Integer

value = instance.SetWallStiffnessUnitSystem(NUnitSystem)
```

### C#

```csharp
System.int SetWallStiffnessUnitSystem(
   System.int NUnitSystem
)
```

### C++/CLI

```cpp
System.int SetWallStiffnessUnitSystem(
   System.int NUnitSystem
)
```

### Parameters

- `NUnitSystem`: Unit system as defined in [swsUnitSystem_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnitSystem_e.html)

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleContactSetsEditManager::SetWallStiffnessUnitSystem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~SetWallStiffnessUnitSystem.html).

## Remarks

This property is valid only if [ICWMultipleContactSetsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetContactType.html) sets [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearVirtualWall, and [ICWMultipleContactSetsEditManager::SetWallType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetWallType.html) sets [swsWallType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsWallType_e.html).swsWallTypeFlexible.

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)
[ICWMultipleContactSetsEditManager::SetAxialStiffnessValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetAxialStiffnessValue.html)
[ICWMultipleContactSetsEditManager::SetTangentialStiffnessValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetTangentialStiffnessValue.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
