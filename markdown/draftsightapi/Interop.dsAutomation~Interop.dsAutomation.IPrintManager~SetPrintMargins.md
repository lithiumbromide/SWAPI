---
title: "SetPrintMargins Method (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "SetPrintMargins"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetPrintMargins.html"
---

# SetPrintMargins Method (IPrintManager)

Sets the size of the margins for the [paper size](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PaperSize.html) specified to use for printing.

## Syntax

### Visual Basic

```vb
Sub SetPrintMargins( _
   ByVal Top As System.Double, _
   ByVal Bottom As System.Double, _
   ByVal Left As System.Double, _
   ByVal Right As System.Double _
)
```

### C#

```csharp
void SetPrintMargins(
   System.double Top,
   System.double Bottom,
   System.double Left,
   System.double Right
)
```

### JScript

```
function SetPrintMargins(
   Top : System.double,
   Bottom : System.double,
   Left : System.double,
   Right : System.double
);
```

### Managed Extensions for C++

```
void SetPrintMargins(
   System.double Top,
   System.double Bottom,
   System.double Left,
   System.double Right
)
```

### C++/CLI

```cpp
void SetPrintMargins(
   System.double Top,
   System.double Bottom,
   System.double Left,
   System.double Right
)
```

### Parameters

- `Top`: Top margin
- `Bottom`: Bottom margin
- `Left`: Left margin
- `Right`: Right margin

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::GetPrintMargins Method ()](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetPrintMargins.html)

## Availability

DraftSight V1R4.0
