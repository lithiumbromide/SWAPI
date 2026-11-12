---
title: "SetReturnValue Method (ILispFunction)"
project: ""
interface: "ILispFunction"
member: "SetReturnValue"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILispFunction~SetReturnValue.html"
---

# SetReturnValue Method (ILispFunction)

Sets the value for this LISP function to return to LISP.

## Syntax

### Visual Basic

```vb
Sub SetReturnValue( _
   ByVal Value As LispParameter _
)
```

### C#

```csharp
void SetReturnValue(
   LispParameter Value
)
```

### JScript

```
function SetReturnValue(
   Value : LispParameter
);
```

### Managed Extensions for C++

```
void SetReturnValue(
   LispParameter* Value
)
```

### C++/CLI

```cpp
void SetReturnValue(
   LispParameter^ Value
)
```

### Parameters

- `Value`: [Value](Interop.dsAutomation~Interop.dsAutomation.ILispParameter.html) for this LISP function to return to LISP

## See Also

[ILispFunction Interface](Interop.dsAutomation~Interop.dsAutomation.ILispFunction.html)
[ILispFunction Members](Interop.dsAutomation~Interop.dsAutomation.ILispFunction_members.html)
[ILispFunction::CreateReturnValue Method ()](Interop.dsAutomation~Interop.dsAutomation.ILispFunction~CreateReturnValue.html)

## Availability

DraftSight V1R4.0
