---
title: "GetHandle Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "GetHandle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetHandle.html"
---

# GetHandle Method (IEntityHelper)

Gets the value of the handle for the specified entity.

## Syntax

### Visual Basic

```vb
Function GetHandle( _
   ByVal Obj As System.Object _
) As System.String
```

### C#

```csharp
System.string GetHandle(
   System.object Obj
)
```

### JScript

```
function GetHandle(
   Obj : System.Object
) : System.String;
```

### Managed Extensions for C++

```
System.string* GetHandle(
   System.Object* Obj
)
```

### C++/CLI

```cpp
System.String^ GetHandle(
   System.Object^ Obj
)
```

### Parameters

- `Obj`: Entity for which to get the value of its handle

### Return Value

Value of the handle

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)
[IEntityHelper::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~DeleteCustomData.html)
[IEntityHelper::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetCustomData.html)
[IEntityHelper::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~SetCustomData.html)

## Availability

DraftSight V1R5.0
