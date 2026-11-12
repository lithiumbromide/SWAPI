---
title: "PrintOut Method (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "PrintOut"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PrintOut.html"
---

# PrintOut Method (IPrintManager)

Prints the specified number of copies of the active document to the specified file or printer.

## Syntax

### Visual Basic

```vb
Sub PrintOut( _
   ByVal Copies As System.Integer, _
   ByVal FileName As System.String _
)
```

### C#

```csharp
void PrintOut(
   System.int Copies,
   System.string FileName
)
```

### JScript

```
function PrintOut(
   Copies : System.int,
   FileName : System.String
);
```

### Managed Extensions for C++

```
void PrintOut(
   System.int Copies,
   System.string* FileName
)
```

### C++/CLI

```cpp
void PrintOut(
   System.int Copies,
   System.String^ FileName
)
```

### Parameters

- `Copies`: Number of copies of the active document to print
- `FileName`: Path and file name to which to print the active document or an empty string, which indicates to print the active document to the printer specified in [IPrintManager::Printer](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~Printer.html)

## Examples

See the [IPrintManager](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html) examples.

## Remarks

Call [IPrintManager::SetSheets](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetSheets.html) before calling this method.

If a file of the same name already exists in the path specified in FileName, then that file is overwritten. You should check for the existence of a file before printing to a file.

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)

## Availability

DraftSight V1R1
