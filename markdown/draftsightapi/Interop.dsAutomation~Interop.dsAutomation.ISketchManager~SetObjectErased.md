---
title: "SetObjectErased Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "SetObjectErased"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SetObjectErased.html"
---

# SetObjectErased Method (ISketchManager)

Sets whether the specified sketch entity is erased.

## Syntax

### Visual Basic

```vb
Sub SetObjectErased( _
   ByVal Obj As System.Object, _
   ByVal Value As System.Boolean _
)
```

### C#

```csharp
void SetObjectErased(
   System.object Obj,
   System.bool Value
)
```

### JScript

```
function SetObjectErased(
   Obj : System.Object,
   Value : System.boolean
);
```

### Managed Extensions for C++

```
void SetObjectErased(
   System.Object* Obj,
   System.bool Value
)
```

### C++/CLI

```cpp
void SetObjectErased(
   System.Object^ Obj,
   System.bool Value
)
```

### Parameters

- `Obj`: Sketch entity
- `Value`: True if erased, false if not

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::IsObjectErased Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~IsObjectErased.html)

## Availability

DraftSight V1R1.4
