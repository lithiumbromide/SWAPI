---
title: "GetBlock Method (IMLeader)"
project: ""
interface: "IMLeader"
member: "GetBlock"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~GetBlock.html"
---

# GetBlock Method (IMLeader)

Gets the BlockInstance of this MLeader.

## Syntax

### Visual Basic

```vb
Function GetBlock() As BlockInstance
```

### C#

```csharp
BlockInstance GetBlock()
```

### JScript

```
function GetBlock() : BlockInstance;
```

### Managed Extensions for C++

```
BlockInstance* GetBlock();
```

### C++/CLI

```cpp
BlockInstance^ GetBlock();
```

### Return Value

[IBlockInstance](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)

## Remarks

This property is valid only if this MLeader was created with Block content, [ISketchManager::InsertMLeaderWithBlockContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithBlockContentType.html) ([dsMLeaderContentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderContentType_e.html).dsMLeaderContentType_Block).

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
