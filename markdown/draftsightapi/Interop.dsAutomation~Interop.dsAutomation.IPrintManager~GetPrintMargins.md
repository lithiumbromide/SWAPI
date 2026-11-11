---
title: "GetPrintMargins Method (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "GetPrintMargins"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetPrintMargins.html"
---

# GetPrintMargins Method (IPrintManager)

Gets the size of the margins of the [paper size](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PaperSize.html) specified to use for printing.

## Syntax

### Visual Basic

```vb
Sub GetPrintMargins( _
   ByRef Top As System.Double, _
   ByRef Bottom As System.Double, _
   ByRef Left As System.Double, _
   ByRef Right As System.Double _
)
```

### C#

```csharp
void GetPrintMargins(
   out System.double Top,
   out System.double Bottom,
   out System.double Left,
   out System.double Right
)
```

### JScript

```
function GetPrintMargins(
   Top : System.double,
   Bottom : System.double,
   Left : System.double,
   Right : System.double
);
```

### Managed Extensions for C++

```
void GetPrintMargins(
   [PARAMFLAG::Out] System.double Top,
   [PARAMFLAG::Out] System.double Bottom,
   [PARAMFLAG::Out] System.double Left,
   [PARAMFLAG::Out] System.double Right
)
```

### C++/CLI

```cpp
void GetPrintMargins(
   [Out] System.double Top,
   [Out] System.double Bottom,
   [Out] System.double Left,
   [Out] System.double Right
)
```

### Parameters

- `Top`: Top margin
- `Bottom`: Bottom margin
- `Left`: Left margin
- `Right`: Right margin

## Examples

See the [IPrintManager](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html) examples.

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::SetPrintMargins Method ()](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetPrintMargins.html)

## Availability

DraftSight V1R1
