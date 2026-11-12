---
title: "SetObjectLayer Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "SetObjectLayer"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SetObjectLayer.html"
---

# SetObjectLayer Method (ISketchManager)

Sets the specified Layer of the specified sketch entity.

## Syntax

### Visual Basic

```vb
Sub SetObjectLayer( _
   ByVal Obj As System.Object, _
   ByVal Layer As System.String _
)
```

### C#

```csharp
void SetObjectLayer(
   System.object Obj,
   System.string Layer
)
```

### JScript

```
function SetObjectLayer(
   Obj : System.Object,
   Layer : System.String
);
```

### Managed Extensions for C++

```
void SetObjectLayer(
   System.Object* Obj,
   System.string* Layer
)
```

### C++/CLI

```cpp
void SetObjectLayer(
   System.Object^ Obj,
   System.String^ Layer
)
```

### Parameters

- `Obj`: Sketch object
- `Layer`: Name of the Layer

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::GetObjectLayer Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetObjectLayer.html)

## Availability

DraftSight V1R1.4
