---
title: "GetHandleFromObject Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetHandleFromObject"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetHandleFromObject.html"
---

# GetHandleFromObject Method (IDocument)

Gets the handle of the specified object.

## Syntax

### Visual Basic

```vb
Function GetHandleFromObject( _
   ByVal Obj As System.Object _
) As System.String
```

### C#

```csharp
System.string GetHandleFromObject(
   System.object Obj
)
```

### JScript

```
function GetHandleFromObject(
   Obj : System.Object
) : System.String;
```

### Managed Extensions for C++

```
System.string* GetHandleFromObject(
   System.Object* Obj
)
```

### C++/CLI

```cpp
System.String^ GetHandleFromObject(
   System.Object^ Obj
)
```

### Parameters

- `Obj`: Object for which to get a handle

### Return Value

Handle; empty string if Obj is not a valid DraftSight API object

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)

## Availability

DraftSight V1R1.4
