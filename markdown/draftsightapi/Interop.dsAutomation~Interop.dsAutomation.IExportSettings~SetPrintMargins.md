---
title: "SetPrintMargins Method (IExportSettings)"
project: ""
interface: "IExportSettings"
member: "SetPrintMargins"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExportSettings~SetPrintMargins.html"
---

# SetPrintMargins Method (IExportSettings)

Sets the specified print margins.

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

## Examples

See the [IExportSettings](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html) examples.

## Remarks

The margin units depend on the current paper size. See [IExportSettings::GetAvailablePaperSizes](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~GetAvailablePaperSizes.html) and [IExportSettings::PaperSize](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~PaperSize.html).

## See Also

[IExportSettings Interface](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html)
[IExportSettings Members](Interop.dsAutomation~Interop.dsAutomation.IExportSettings_members.html)

## Availability

DraftSight 2018 SP0
