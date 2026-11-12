---
title: "RemoveLispFunction Method (IDocument)"
project: ""
interface: "IDocument"
member: "RemoveLispFunction"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~RemoveLispFunction.html"
---

# RemoveLispFunction Method (IDocument)

Removes the specified LISP function so that it can no longer be called from LISP.

## Syntax

### Visual Basic

```vb
Sub RemoveLispFunction( _
   ByVal FunctionName As System.String _
)
```

### C#

```csharp
void RemoveLispFunction(
   System.string FunctionName
)
```

### JScript

```
function RemoveLispFunction(
   FunctionName : System.String
);
```

### Managed Extensions for C++

```
void RemoveLispFunction(
   System.string* FunctionName
)
```

### C++/CLI

```cpp
void RemoveLispFunction(
   System.String^ FunctionName
)
```

### Parameters

- `FunctionName`: Name of the LISP function to remove

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::CreateLispFunction Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateLispFunction.html)
[ILispFunction Interface](Interop.dsAutomation~Interop.dsAutomation.ILispFunction.html)

## Availability

DraftSight V1R4.0
