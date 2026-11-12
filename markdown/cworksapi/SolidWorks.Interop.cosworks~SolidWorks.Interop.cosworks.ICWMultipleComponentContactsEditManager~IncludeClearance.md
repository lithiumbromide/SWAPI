---
title: "IncludeClearance Method (ICWMultipleComponentContactsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager"
member: "IncludeClearance"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~IncludeClearance.html"
---

# IncludeClearance Method (ICWMultipleComponentContactsEditManager)

Obsolete. Superseded by [ICWMultipleComponentContactsEditManager::IncludeClearance2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~IncludeClearance2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IncludeClearance( _
   ByVal BNonTouching As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleComponentContactsEditManager
Dim BNonTouching As System.Integer
Dim value As System.Integer

value = instance.IncludeClearance(BNonTouching)
```

### C#

```csharp
System.int IncludeClearance(
   System.int BNonTouching
)
```

### C++/CLI

```cpp
System.int IncludeClearance(
   System.int BNonTouching
)
```

### Parameters

- `BNonTouching`: 1 to include clearance for non-touching faces, 0 to not

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleComponentContactsEditManager::IncludeClearance](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleComponentContactsEditManager~IncludeClearance.html).

## Remarks

This method is valid only if [ICWMultipleComponentContactsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetContactType.html)'s NType is set to [swsContactType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactType_e.html).swsContactTypeBonded.

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleComponentContactsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html)
[ICWMultipleComponentContactsEditManager::SetClearanceUnit Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetClearanceUnit.html)
[ICWMultipleComponentContactsEditManager::SetClearanceValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetClearanceValue.html)
**ICWMultipleComponentContactsEditManager::GetClearanceUnit Method ()**
**ICWMultipleComponentContactsEditManager::GetClearanceValue Method ()**
**ICWMultipleComponentContactsEditManager::GetIncludeClearance Method ()**

## Availability

SOLIDWORKS Simulation API 2017 SP0
