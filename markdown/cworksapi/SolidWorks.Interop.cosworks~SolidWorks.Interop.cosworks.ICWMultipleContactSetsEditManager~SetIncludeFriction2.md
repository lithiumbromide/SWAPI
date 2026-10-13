---
title: "SetIncludeFriction2 Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "SetIncludeFriction2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetIncludeFriction2.html"
---

# SetIncludeFriction2 Method (ICWMultipleContactSetsEditManager)

Sets whether to include friction in the contact sets to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetIncludeFriction2( _
   ByVal BIncludeFriction As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
Dim BIncludeFriction As System.Boolean
Dim value As System.Integer

value = instance.SetIncludeFriction2(BIncludeFriction)
```

### C#

```csharp
System.int SetIncludeFriction2(
   System.bool BIncludeFriction
)
```

### C++/CLI

```cpp
System.int SetIncludeFriction2(
   System.bool BIncludeFriction
)
```

### Parameters

- `BIncludeFriction`: -1 or true to include friction, 0 or false to not

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleContactSetsEditManager::SetIncludeFriction2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~SetIncludeFriction2.html).

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
