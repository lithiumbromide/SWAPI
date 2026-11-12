---
title: "SetClearanceUnit Method (ICWMultipleComponentContactsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager"
member: "SetClearanceUnit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetClearanceUnit.html"
---

# SetClearanceUnit Method (ICWMultipleComponentContactsEditManager)

Sets the units of clearance distance.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetClearanceUnit( _
   ByVal NGapUnit As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleComponentContactsEditManager
Dim NGapUnit As System.Integer
Dim value As System.Integer

value = instance.SetClearanceUnit(NGapUnit)
```

### C#

```csharp
System.int SetClearanceUnit(
   System.int NGapUnit
)
```

### C++/CLI

```cpp
System.int SetClearanceUnit(
   System.int NGapUnit
)
```

### Parameters

- `NGapUnit`: Units of clearance as defined in [swsPinballUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPinballUnit_e.html)

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleComponentContactsEditManager::SetClearanceUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleComponentContactsEditManager~SetClearanceUnit.html).

## Remarks

This method is valid only if:

- [ICWMultipleComponentContactsEditManager::IncludeClearance](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~IncludeClearance.html)'s BNonTouching is set to 1,

- and -

- [ICWMultipleComponentContactsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetContactType.html)'s NType is set to [swsContactType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactType_e.html).swsContactTypeBonded.

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleComponentContactsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html)
[ICWMultipleComponentContactsEditManager::SetClearanceValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetClearanceValue.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
