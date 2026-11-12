---
title: "ClearSelections Method (ISelectionManager)"
project: ""
interface: "ISelectionManager"
member: "ClearSelections"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~ClearSelections.html"
---

# ClearSelections Method (ISelectionManager)

Clears the specified command from the selection set.

## Syntax

### Visual Basic

```vb
Sub ClearSelections( _
   ByVal SSType As dsSelectionSetType_e _
)
```

### C#

```csharp
void ClearSelections(
   dsSelectionSetType_e SSType
)
```

### JScript

```
function ClearSelections(
   SSType : dsSelectionSetType_e
);
```

### Managed Extensions for C++

```
void ClearSelections(
   dsSelectionSetType_e SSType
)
```

### C++/CLI

```cpp
void ClearSelections(
   dsSelectionSetType_e SSType
)
```

### Parameters

- `SSType`: Type of command to clear from the selection set as defined in [dsSelectionSetType_e](Interop.dsAutomation~Interop.dsAutomation.dsSelectionSetType_e.html)

## Examples

[Rotate and Copy Entities (C#)](Rotate_and_Copy_Entities_Example_CSharp.htm)
[Rotate and Copy Entities (VB.NET)](Rotate_and_Copy_Entities_Example_VBNET.htm)
[Rotate and Copy Entities (VBA)](Rotate_and_Copy_Entities_Example_VBA.htm)

## See Also

[ISelectionManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager.html)
[ISelectionManager Members](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager_members.html)

## Availability

DraftSight V1R1
