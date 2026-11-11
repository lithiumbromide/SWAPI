---
title: "GetObjectType Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetObjectType"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetObjectType.html"
---

# GetObjectType Method (IApplication)

Gets the type of specified object.

## Syntax

### Visual Basic

```vb
Function GetObjectType( _
   ByVal Obj As System.Object _
) As dsObjectType_e
```

### C#

```csharp
dsObjectType_e GetObjectType(
   System.object Obj
)
```

### JScript

```
function GetObjectType(
   Obj : System.Object
) : dsObjectType_e;
```

### Managed Extensions for C++

```
dsObjectType_e GetObjectType(
   System.Object* Obj
)
```

### C++/CLI

```cpp
dsObjectType_e GetObjectType(
   System.Object^ Obj
)
```

### Parameters

- `Obj`: Object

### Return Value

Type of Obj as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

## Availability

DraftSight V1R1.4
