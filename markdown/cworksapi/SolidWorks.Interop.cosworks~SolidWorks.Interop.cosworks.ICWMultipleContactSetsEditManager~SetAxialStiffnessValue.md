---
title: "SetAxialStiffnessValue Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "SetAxialStiffnessValue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetAxialStiffnessValue.html"
---

# SetAxialStiffnessValue Method (ICWMultipleContactSetsEditManager)

Sets the wall axial stiffness value for the flexible virtual wall contact sets to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAxialStiffnessValue( _
   ByVal DAxialStiffnessValue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
Dim DAxialStiffnessValue As System.Double
Dim value As System.Integer

value = instance.SetAxialStiffnessValue(DAxialStiffnessValue)
```

### C#

```csharp
System.int SetAxialStiffnessValue(
   System.double DAxialStiffnessValue
)
```

### C++/CLI

```cpp
System.int SetAxialStiffnessValue(
   System.double DAxialStiffnessValue
)
```

### Parameters

- `DAxialStiffnessValue`: Wall axial stiffness value

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleContactSetsEditManager::SetAxialStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~SetAxialStiffnessValue.html).

## Remarks

This property is valid only if [ICWMultipleContactSetsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetContactType.html) sets [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearVirtualWall, and [ICWMultipleContactSetsEditManager::SetWallType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetWallType.html) sets [swsWallType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsWallType_e.html).swsWallTypeFlexible.

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)
[ICWMultipleContactSetsEditManager::SetTangentialStiffnessValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetTangentialStiffnessValue.html)
[ICWMultipleContactSetsEditManager::SetWallStiffnessUnitSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetWallStiffnessUnitSystem.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
