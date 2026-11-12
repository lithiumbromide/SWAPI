---
title: "SetClearanceUnit Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "SetClearanceUnit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetClearanceUnit.html"
---

# SetClearanceUnit Method (ICWMultipleContactSetsEditManager)

Sets the units of clearance (gap) for the contact sets to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetClearanceUnit( _
   ByVal NClearanceUnit As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
Dim NClearanceUnit As System.Integer
Dim value As System.Integer

value = instance.SetClearanceUnit(NClearanceUnit)
```

### C#

```csharp
System.int SetClearanceUnit(
   System.int NClearanceUnit
)
```

### C++/CLI

```cpp
System.int SetClearanceUnit(
   System.int NClearanceUnit
)
```

### Parameters

- `NClearanceUnit`: Units of clearance (gap) as defined in [swsLinearUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinearUnit_e.html)

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleContactSetsEditManager::SetClearanceUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~SetClearanceUnit.html).

## Remarks

This property is valid only if [ICWMultipleContactSetsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetContactType.html) is:

- [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearVirtualWall

- or -

- swsContactSetTypeStaticNonLinear_e.swsContactSetTypeStaticNonLinearNoPenetration

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)
[ICWMultipleContactSetsEditManager::SetClearanceValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetClearanceValue.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
