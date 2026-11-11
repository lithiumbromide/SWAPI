---
title: "GetArrow Method (IMLeader)"
project: ""
interface: "IMLeader"
member: "GetArrow"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~GetArrow.html"
---

# GetArrow Method (IMLeader)

Gets the arrow of this MLeader.

## Syntax

### Visual Basic

```vb
Sub GetArrow( _
   ByRef ArrowType As dsDimensionArrowType_e, _
   ByRef CustomArrowBlockName As System.String _
)
```

### C#

```csharp
void GetArrow(
   out dsDimensionArrowType_e ArrowType,
   out System.string CustomArrowBlockName
)
```

### JScript

```
function GetArrow(
   ArrowType : dsDimensionArrowType_e,
   CustomArrowBlockName : System.String
);
```

### Managed Extensions for C++

```
void GetArrow(
   [PARAMFLAG::Out] dsDimensionArrowType_e ArrowType,
   [PARAMFLAG::Out] System.string* CustomArrowBlockName
)
```

### C++/CLI

```cpp
void GetArrow(
   [Out] dsDimensionArrowType_e ArrowType,
   [Out] System.String^ CustomArrowBlockName
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
