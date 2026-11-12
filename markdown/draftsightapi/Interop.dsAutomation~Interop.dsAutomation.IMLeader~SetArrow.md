---
title: "SetArrow Method (IMLeader)"
project: ""
interface: "IMLeader"
member: "SetArrow"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~SetArrow.html"
---

# SetArrow Method (IMLeader)

Sets the arrow of this MLeader.

## Syntax

### Visual Basic

```vb
Sub SetArrow( _
   ByVal ArrowType As dsDimensionArrowType_e, _
   ByVal CustomArrowBlockName As System.String _
)
```

### C#

```csharp
void SetArrow(
   dsDimensionArrowType_e ArrowType,
   System.string CustomArrowBlockName
)
```

### JScript

```
function SetArrow(
   ArrowType : dsDimensionArrowType_e,
   CustomArrowBlockName : System.String
);
```

### Managed Extensions for C++

```
void SetArrow(
   dsDimensionArrowType_e ArrowType,
   System.string* CustomArrowBlockName
)
```

### C++/CLI

```cpp
void SetArrow(
   dsDimensionArrowType_e ArrowType,
   System.String^ CustomArrowBlockName
)
```

### Parameters

- `ArrowType`: Type of arrow as defined by [dsDimensionArrowType_e](Interop.dsAutomation~Interop.dsAutomation.dsDimensionArrowType_e.html)
- `CustomArrowBlockName`: Custom arrow Block name

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
