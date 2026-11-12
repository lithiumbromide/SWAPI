---
title: "SetObjectVisible Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "SetObjectVisible"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SetObjectVisible.html"
---

# SetObjectVisible Method (ISketchManager)

Sets whether the specified sketch entity is visible.

## Syntax

### Visual Basic

```vb
Sub SetObjectVisible( _
   ByVal Obj As System.Object, _
   ByVal Visible As System.Boolean _
)
```

### C#

```csharp
void SetObjectVisible(
   System.object Obj,
   System.bool Visible
)
```

### JScript

```
function SetObjectVisible(
   Obj : System.Object,
   Visible : System.boolean
);
```

### Managed Extensions for C++

```
void SetObjectVisible(
   System.Object* Obj,
   System.bool Visible
)
```

### C++/CLI

```cpp
void SetObjectVisible(
   System.Object^ Obj,
   System.bool Visible
)
```

### Parameters

- `Obj`: Sketch entity
- `Visible`: True if visible, false if not

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::IsObjectVisible Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~IsObjectVisible.html)

## Availability

DraftSight V1R1.4
