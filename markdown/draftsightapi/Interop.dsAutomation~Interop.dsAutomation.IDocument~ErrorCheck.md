---
title: "ErrorCheck Method (IDocument)"
project: ""
interface: "IDocument"
member: "ErrorCheck"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~ErrorCheck.html"
---

# ErrorCheck Method (IDocument)

Checks the integrity of this document and optionally corrects errors.

## Syntax

### Visual Basic

```vb
Sub ErrorCheck( _
   ByVal FixErrors As System.Boolean, _
   ByRef ProcessedEntitiesNumber As System.Integer, _
   ByRef ErrorsNumber As System.Integer, _
   ByRef FixedErrorsNumber As System.Integer, _
   ByRef ReportStrArray As System.Object _
)
```

### C#

```csharp
void ErrorCheck(
   System.bool FixErrors,
   out System.int ProcessedEntitiesNumber,
   out System.int ErrorsNumber,
   out System.int FixedErrorsNumber,
   out System.object ReportStrArray
)
```

### JScript

```
function ErrorCheck(
   FixErrors : System.boolean,
   ProcessedEntitiesNumber : System.int,
   ErrorsNumber : System.int,
   FixedErrorsNumber : System.int,
   ReportStrArray : System.Object
);
```

### Managed Extensions for C++

```
void ErrorCheck(
   System.bool FixErrors,
   [PARAMFLAG::Out] System.int ProcessedEntitiesNumber,
   [PARAMFLAG::Out] System.int ErrorsNumber,
   [PARAMFLAG::Out] System.int FixedErrorsNumber,
   [PARAMFLAG::Out] System.Object* ReportStrArray
)
```

### C++/CLI

```cpp
void ErrorCheck(
   System.bool FixErrors,
   [Out] System.int ProcessedEntitiesNumber,
   [Out] System.int ErrorsNumber,
   [Out] System.int FixedErrorsNumber,
   [Out] System.Object^ ReportStrArray
)
```

### Parameters

- `FixErrors`: True to fix errors, false to not
- `ProcessedEntitiesNumber`: Number of entities that were processed
- `ErrorsNumber`: Number of errors found
- `FixedErrorsNumber`: Number of errors fixed
- `ReportStrArray`: Array of strings of the error messages

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)

## Availability

DraftSight V1R1.4
