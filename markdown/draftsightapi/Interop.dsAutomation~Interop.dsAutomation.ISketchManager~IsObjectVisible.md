---
title: "IsObjectVisible Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "IsObjectVisible"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~IsObjectVisible.html"
---

# IsObjectVisible Method (ISketchManager)

Gets whether the specified sketch entity is visible.

## Syntax

### Visual Basic

```vb
Function IsObjectVisible( _
   ByVal Obj As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool IsObjectVisible(
   System.object Obj
)
```

### JScript

```
function IsObjectVisible(
   Obj : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool IsObjectVisible(
   System.Object* Obj
)
```

### C++/CLI

```cpp
System.bool IsObjectVisible(
   System.Object^ Obj
)
```

### Parameters

- `Obj`: Sketch entity

### Return Value

True if visible, false if not

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::SetObjectVisible Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SetObjectVisible.html)

## Availability

DraftSight V1R1.4
