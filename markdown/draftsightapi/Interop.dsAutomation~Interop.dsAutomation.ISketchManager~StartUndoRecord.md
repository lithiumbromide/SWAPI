---
title: "StartUndoRecord Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "StartUndoRecord"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~StartUndoRecord.html"
---

# StartUndoRecord Method (ISketchManager)

Starts the undo recording of a set of sketch operations.

## Syntax

### Visual Basic

```vb
Sub StartUndoRecord()
```

### C#

```csharp
void StartUndoRecord()
```

### JScript

```
function StartUndoRecord();
```

### Managed Extensions for C++

```
void StartUndoRecord();
```

### C++/CLI

```cpp
void StartUndoRecord();
```

## Remarks

Use this method and [ISketchManager::StopUndoRecord](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~StopUndoRecord.html) to bracket the set of entity-creation operations you want to add to the undo stack.

After populating the undo register, you can use **UndoN** in the command window to reverse the operations.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight 2019 SP0
