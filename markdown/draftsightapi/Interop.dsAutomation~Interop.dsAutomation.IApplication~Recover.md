---
title: "Recover Method (IApplication)"
project: ""
interface: "IApplication"
member: "Recover"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~Recover.html"
---

# Recover Method (IApplication)

Recovers a damaged drawing file.

## Syntax

### Visual Basic

```vb
Function Recover( _
   ByVal FilePath As System.String, _
   ByRef ProcessedEntitiesNumber As System.Integer, _
   ByRef ErrorsNumber As System.Integer, _
   ByRef FixedErrorsNumber As System.Integer, _
   ByRef ReportStrArray As System.Object _
) As Document
```

### C#

```csharp
Document Recover(
   System.string FilePath,
   out System.int ProcessedEntitiesNumber,
   out System.int ErrorsNumber,
   out System.int FixedErrorsNumber,
   out System.object ReportStrArray
)
```

### JScript

```
function Recover(
   FilePath : System.String,
   ProcessedEntitiesNumber : System.int,
   ErrorsNumber : System.int,
   FixedErrorsNumber : System.int,
   ReportStrArray : System.Object
) : Document;
```

### Managed Extensions for C++

```
Document* Recover(
   System.string* FilePath,
   [PARAMFLAG::Out] System.int ProcessedEntitiesNumber,
   [PARAMFLAG::Out] System.int ErrorsNumber,
   [PARAMFLAG::Out] System.int FixedErrorsNumber,
   [PARAMFLAG::Out] System.Object* ReportStrArray
)
```

### C++/CLI

```cpp
Document^ Recover(
   System.String^ FilePath,
   [Out] System.int ProcessedEntitiesNumber,
   [Out] System.int ErrorsNumber,
   [Out] System.int FixedErrorsNumber,
   [Out] System.Object^ ReportStrArray
)
```

### Parameters

- `FilePath`: Path and file name of drawing to recover
- `ProcessedEntitiesNumber`: Number of entities that were processed
- `ErrorsNumber`: Number of errors found
- `FixedErrorsNumber`: Number of errors fixed
- `ReportStrArray`: Array of strings of the error messages

### Return Value

[IDocument](Interop.dsAutomation~Interop.dsAutomation.IDocument.html) or null if drawing is not recovered

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

## Availability

DraftSight V1R1.4
