---
title: "IncludeClearance2 Method (ICWMultipleComponentContactsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager"
member: "IncludeClearance2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~IncludeClearance2.html"
---

# IncludeClearance2 Method (ICWMultipleComponentContactsEditManager)

Sets whether to include clearance for non-touching faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function IncludeClearance2( _
   ByVal BNonTouching As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleComponentContactsEditManager
Dim BNonTouching As System.Boolean
Dim value As System.Integer

value = instance.IncludeClearance2(BNonTouching)
```

### C#

```csharp
System.int IncludeClearance2(
   System.bool BNonTouching
)
```

### C++/CLI

```cpp
System.int IncludeClearance2(
   System.bool BNonTouching
)
```

### Parameters

- `BNonTouching`: -1 or true to include clearance for non-touching faces, 0 or false to not

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleComponentContactsEditManager::IncludeClearance2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleComponentContactsEditManager~IncludeClearance2.html).

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleComponentContactsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
