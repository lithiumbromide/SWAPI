---
title: "SetIncludeFriction Method (ICWMultipleComponentContactsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager"
member: "SetIncludeFriction"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetIncludeFriction.html"
---

# SetIncludeFriction Method (ICWMultipleComponentContactsEditManager)

Obsolete. Superseded by [ICWMultipleComponentContactsEditManager::SetIncludeFriction2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetIncludeFriction2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetIncludeFriction( _
   ByVal BIncludeFriction As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleComponentContactsEditManager
Dim BIncludeFriction As System.Integer
Dim value As System.Integer

value = instance.SetIncludeFriction(BIncludeFriction)
```

### C#

```csharp
System.int SetIncludeFriction(
   System.int BIncludeFriction
)
```

### C++/CLI

```cpp
System.int SetIncludeFriction(
   System.int BIncludeFriction
)
```

### Parameters

- `BIncludeFriction`: 1 to include friction, 0 to not

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleComponentContactsEditManager::SetIncludeFriction](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleComponentContactsEditManager~SetIncludeFriction.html).

## Remarks

This method is valid only if [ICWMultipleComponentContactsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetContactType.html)'s NType is set to [swsContactType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactType_e.html).swsContactTypeStaticNoPenetration.

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleComponentContactsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html)
[ICWMultipleComponentContactsEditManager::SetFrictionValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetFrictionValue.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
