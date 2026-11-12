---
title: "SetWallType Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "SetWallType"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetWallType.html"
---

# SetWallType Method (ICWMultipleContactSetsEditManager)

Sets the virtual wall type of the contact sets to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetWallType( _
   ByVal NWallType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
Dim NWallType As System.Integer
Dim value As System.Integer

value = instance.SetWallType(NWallType)
```

### C#

```csharp
System.int SetWallType(
   System.int NWallType
)
```

### C++/CLI

```cpp
System.int SetWallType(
   System.int NWallType
)
```

### Parameters

- `NWallType`: Virtual wall type as defined in [swsWallType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWallType_e.html)

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleContactSetsEditManager::SetWallType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~SetWallType.html).

## Remarks

This property is valid only if [ICWMultipleContactSetsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetContactType.html) sets [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearVirtualWall.

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)
[ICWMultipleContactSetsEditManager::SetAxialStiffnessValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetAxialStiffnessValue.html)
[ICWMultipleContactSetsEditManager::SetTangentialStiffnessValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetTangentialStiffnessValue.html)
[ICWMultipleContactSetsEditManager::SetWallStiffnessUnitSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetWallStiffnessUnitSystem.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
