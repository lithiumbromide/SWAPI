---
title: "IsObjectErased Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "IsObjectErased"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~IsObjectErased.html"
---

# IsObjectErased Method (ISketchManager)

Gets whether the specified sketch entity is erased.

## Syntax

### Visual Basic

```vb
Function IsObjectErased( _
   ByVal Obj As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool IsObjectErased(
   System.object Obj
)
```

### JScript

```
function IsObjectErased(
   Obj : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool IsObjectErased(
   System.Object* Obj
)
```

### C++/CLI

```cpp
System.bool IsObjectErased(
   System.Object^ Obj
)
```

### Parameters

- `Obj`: Sketch entity

### Return Value

True if sketch entity is erased, false if not

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::SetObjectErased Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SetObjectErased.html)

## Availability

DraftSight V1R1.4
