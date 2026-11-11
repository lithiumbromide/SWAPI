---
title: "GetLineWeight Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "GetLineWeight"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetLineWeight.html"
---

# GetLineWeight Method (IEntityHelper)

Gets the LineWeight for the specified entity.

## Syntax

### Visual Basic

```vb
Function GetLineWeight( _
   ByVal Obj As System.Object _
) As dsLineWeight_e
```

### C#

```csharp
dsLineWeight_e GetLineWeight(
   System.object Obj
)
```

### JScript

```
function GetLineWeight(
   Obj : System.Object
) : dsLineWeight_e;
```

### Managed Extensions for C++

```
dsLineWeight_e GetLineWeight(
   System.Object* Obj
)
```

### C++/CLI

```cpp
dsLineWeight_e GetLineWeight(
   System.Object^ Obj
)
```

### Parameters

- `Obj`: Entity

### Return Value

LineWeight as defined in [dsLineWeight_e](Interop.dsAutomation~Interop.dsAutomation.dsLineWeight_e.html)

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)
[IEntityHelper::SetLineWeight Method](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~SetLineWeight.html)

## Availability

DraftSight V1R3.0
