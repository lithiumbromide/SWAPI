---
title: "GetPrintMargins Method (IExportSettings)"
project: ""
interface: "IExportSettings"
member: "GetPrintMargins"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExportSettings~GetPrintMargins.html"
---

# GetPrintMargins Method (IExportSettings)

Gets the specified print margins.

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

See the [IExportSettings](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html) examples.

## Remarks

The margin units depend on the current paper size. See [IExportSettings::GetAvailablePaperSizes](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~GetAvailablePaperSizes.html) and [IExportSettings::PaperSize](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~PaperSize.html).

## See Also

[IExportSettings Interface](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html)
[IExportSettings Members](Interop.dsAutomation~Interop.dsAutomation.IExportSettings_members.html)

## Availability

DraftSight 2018 SP0
