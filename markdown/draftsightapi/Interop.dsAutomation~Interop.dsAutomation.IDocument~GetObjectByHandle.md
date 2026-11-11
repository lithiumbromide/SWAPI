---
title: "GetObjectByHandle Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetObjectByHandle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html"
---

# GetObjectByHandle Method (IDocument)

Gets an object by its handle.

## Syntax

### Visual Basic

```vb
Function GetObjectByHandle( _
   ByVal Handle As System.String, _
   ByRef ObjType As dsObjectType_e _
) As System.Object
```

### C#

```csharp
System.object GetObjectByHandle(
   System.string Handle,
   out dsObjectType_e ObjType
)
```

### JScript

```
function GetObjectByHandle(
   Handle : System.String,
   ObjType : dsObjectType_e
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetObjectByHandle(
   System.string* Handle,
   [PARAMFLAG::Out] dsObjectType_e ObjType
)
```

### C++/CLI

```cpp
System.Object^ GetObjectByHandle(
   System.String^ Handle,
   [Out] dsObjectType_e ObjType
)
```

### Parameters

- `Handle`: Handle of the object to get
- `ObjType`: Type of object to get as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)

### Return Value

Object

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)

## Availability

DraftSight V1R1.3
