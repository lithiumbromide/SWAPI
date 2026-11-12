---
title: "SetIncludeFriction2 Method (ICWMultipleComponentContactsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager"
member: "SetIncludeFriction2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetIncludeFriction2.html"
---

# SetIncludeFriction2 Method (ICWMultipleComponentContactsEditManager)

Sets whether to include friction.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetIncludeFriction2( _
   ByVal BIncludeFriction As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleComponentContactsEditManager
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

See [CWMultipleComponentContactsEditManager::SetIncludeFriction2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleComponentContactsEditManager~SetIncludeFriction2.html).

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleComponentContactsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
