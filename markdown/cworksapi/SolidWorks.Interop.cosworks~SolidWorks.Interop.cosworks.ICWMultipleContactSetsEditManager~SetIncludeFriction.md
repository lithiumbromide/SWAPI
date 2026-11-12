---
title: "SetIncludeFriction Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "SetIncludeFriction"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetIncludeFriction.html"
---

# SetIncludeFriction Method (ICWMultipleContactSetsEditManager)

Obsolete. Superseded by [ICWMultipleContactSetsEditManager::SetIncludeFriction2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetIncludeFriction2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetIncludeFriction( _
   ByVal BIncludeFriction As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
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

See [CWMultipleContactSetsEditManager::SetIncludeFriction](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~SetIncludeFriction.html).

## Remarks

This property is valid only if [ICWMultipleContactSetsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetContactType.html) is:

- [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearVirtualWall

- or -

- swsContactSetTypeStaticNonLinear_e.swsContactSetTypeStaticNonLinearNoPenetration

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)
[ICWMultipleContactSetsEditManager::SetFrictionValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetFrictionValue.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
