---
title: "GetObjectLayer Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "GetObjectLayer"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetObjectLayer.html"
---

# GetObjectLayer Method (ISketchManager)

Gets the name of the Layer where the specified sketch entity resides.

## Syntax

### Visual Basic

```vb
Function GetObjectLayer( _
   ByVal Obj As System.Object _
) As System.String
```

### C#

```csharp
System.string GetObjectLayer(
   System.object Obj
)
```

### JScript

```
function GetObjectLayer(
   Obj : System.Object
) : System.String;
```

### Managed Extensions for C++

```
System.string* GetObjectLayer(
   System.Object* Obj
)
```

### C++/CLI

```cpp
System.String^ GetObjectLayer(
   System.Object^ Obj
)
```

### Parameters

- `Obj`: Sketch entity

### Return Value

Name of Layer; empty string if Obj is not a valid DraftSight API object

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::SetObjectLayer Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SetObjectLayer.html)

## Availability

DraftSight V1R1.4
