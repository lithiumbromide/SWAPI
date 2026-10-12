---
title: "SetFrictionValue Method (ICWMultipleComponentContactsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager"
member: "SetFrictionValue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetFrictionValue.html"
---

# SetFrictionValue Method (ICWMultipleComponentContactsEditManager)

Sets the friction coefficient.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFrictionValue( _
   ByVal DFrictionValue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleComponentContactsEditManager
Dim DFrictionValue As System.Double
Dim value As System.Integer

value = instance.SetFrictionValue(DFrictionValue)
```

### C#

```csharp
System.int SetFrictionValue(
   System.double DFrictionValue
)
```

### C++/CLI

```cpp
System.int SetFrictionValue(
   System.double DFrictionValue
)
```

### Parameters

- `DFrictionValue`: 0.0 <= Coefficient of friction <= 1.0

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleComponentContactsEditManager::SetFrictionValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleComponentContactsEditManager~SetFrictionValue.html).

## Remarks

This method is valid only if:

- [ICWMultipleComponentContactsEditManager::SetIncludeFriction](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetIncludeFriction.html)'s BIncludeFriction is set to 1,

- and -

- [ICWMultipleComponentContactsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetContactType.html)'s NType is set to swsContactType_e.swsContactTypeStaticNoPenetration.

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleComponentContactsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
