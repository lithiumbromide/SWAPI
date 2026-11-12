---
title: "SetClearanceValue Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "SetClearanceValue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetClearanceValue.html"
---

# SetClearanceValue Method (ICWMultipleContactSetsEditManager)

Sets the clearance (gap) value for the contact sets to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetClearanceValue( _
   ByVal DClearanceValue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
Dim DClearanceValue As System.Double
Dim value As System.Integer

value = instance.SetClearanceValue(DClearanceValue)
```

### C#

```csharp
System.int SetClearanceValue(
   System.double DClearanceValue
)
```

### C++/CLI

```cpp
System.int SetClearanceValue(
   System.double DClearanceValue
)
```

### Parameters

- `DClearanceValue`: Clearance value (gap)

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleContactSetsEditManager::SetClearanceValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~SetClearanceValue.html).

## Remarks

This property is valid only if [ICWMultipleContactSetsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetContactType.html) is:

- [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearVirtualWall

- or -

- swsContactSetTypeStaticNonLinear_e.swsContactSetTypeStaticNonLinearNoPenetration

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)
[ICWMultipleContactSetsEditManager::SetClearanceUnit Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetClearanceUnit.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
