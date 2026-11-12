---
title: "CreateLispFunction Method (IDocument)"
project: ""
interface: "IDocument"
member: "CreateLispFunction"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateLispFunction.html"
---

# CreateLispFunction Method (IDocument)

Creates a LISP function that can be called from LISP.

## Syntax

### Visual Basic

```vb
Function CreateLispFunction( _
   ByVal ApiUuid As System.String, _
   ByVal Name As System.String, _
   ByRef Error As dsCreateCommandError_e _
) As LispFunction
```

### C#

```csharp
LispFunction CreateLispFunction(
   System.string ApiUuid,
   System.string Name,
   out dsCreateCommandError_e Error
)
```

### JScript

```
function CreateLispFunction(
   ApiUuid : System.String,
   Name : System.String,
   Error : dsCreateCommandError_e
) : LispFunction;
```

### Managed Extensions for C++

```
LispFunction* CreateLispFunction(
   System.string* ApiUuid,
   System.string* Name,
   [PARAMFLAG::Out] dsCreateCommandError_e Error
)
```

### C++/CLI

```cpp
LispFunction^ CreateLispFunction(
   System.String^ ApiUuid,
   System.String^ Name,
   [Out] dsCreateCommandError_e Error
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or non add-in application
- `Name`: Unique name for the LISP function
- `Error`: Result as defined in [dsCreateCommandError_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateCommandError_e.html)

### Return Value

[LISP function](Interop.dsAutomation~Interop.dsAutomation.ILispFunction.html)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::RemoveLispFunction Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~RemoveLispFunction.html)
[ILispParameter Interface](Interop.dsAutomation~Interop.dsAutomation.ILispParameter.html)

## Availability

DraftSight V1R4.0
