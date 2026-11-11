---
title: "SetBlock Method (IMLeader)"
project: ""
interface: "IMLeader"
member: "SetBlock"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~SetBlock.html"
---

# SetBlock Method (IMLeader)

Sets the Block of this MLeader.

## Syntax

### Visual Basic

```vb
Sub SetBlock( _
   ByVal BlockName As System.String, _
   ByVal InsertPoint As MathPoint _
)
```

### C#

```csharp
void SetBlock(
   System.string BlockName,
   MathPoint InsertPoint
)
```

### JScript

```
function SetBlock(
   BlockName : System.String,
   InsertPoint : MathPoint
);
```

### Managed Extensions for C++

```
void SetBlock(
   System.string* BlockName,
   MathPoint* InsertPoint
)
```

### C++/CLI

```cpp
void SetBlock(
   System.String^ BlockName,
   MathPoint^ InsertPoint
)
```

### Parameters

- `BlockName`: Name of Block
- `InsertPoint`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)

## Remarks

This property is valid only if this MLeader was created with Block content, [ISketchManager::InsertMLeaderWithBlockContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithBlockContentType.html) ([dsMLeaderContentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderContentType_e.html).dsMLeaderContentType_Block).

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
