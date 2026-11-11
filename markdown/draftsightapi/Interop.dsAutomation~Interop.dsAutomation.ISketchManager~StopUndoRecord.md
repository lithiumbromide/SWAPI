---
title: "StopUndoRecord Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "StopUndoRecord"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~StopUndoRecord.html"
---

# StopUndoRecord Method (ISketchManager)

Stops the undo recording of a set of sketch operations.

## Syntax

### Visual Basic

```vb
Sub StopUndoRecord()
```

### C#

```csharp
void StopUndoRecord()
```

### JScript

```
function StopUndoRecord();
```

### Managed Extensions for C++

```
void StopUndoRecord();
```

### C++/CLI

```cpp
void StopUndoRecord();
```

## Remarks

Use [ISketchManager::StartUndoRecord](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~StartUndoRecord.html) and this method to bracket the set of entity-creation operations you want to add to the undo register.

After populating the undo register, you can use **UndoN** in the command window to reverse the operations.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight 2019 SP0
