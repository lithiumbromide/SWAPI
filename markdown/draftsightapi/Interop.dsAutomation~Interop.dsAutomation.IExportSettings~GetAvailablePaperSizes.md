---
title: "GetAvailablePaperSizes Method (IExportSettings)"
project: ""
interface: "IExportSettings"
member: "GetAvailablePaperSizes"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExportSettings~GetAvailablePaperSizes.html"
---

# GetAvailablePaperSizes Method (IExportSettings)

Gets the currently available paper sizes.

## Syntax

### Visual Basic

```vb
Sub GetAvailablePaperSizes( _
   ByRef PaperSizesStrArray As System.Object _
)
```

### C#

```csharp
void GetAvailablePaperSizes(
   out System.object PaperSizesStrArray
)
```

### JScript

```
function GetAvailablePaperSizes(
   PaperSizesStrArray : System.Object
);
```

### Managed Extensions for C++

```
void GetAvailablePaperSizes(
   [PARAMFLAG::Out] System.Object* PaperSizesStrArray
)
```

### C++/CLI

```cpp
void GetAvailablePaperSizes(
   [Out] System.Object^ PaperSizesStrArray
)
```

### Parameters

- `PaperSizesStrArray`: Array of paper sizes

## Examples

See the [IExportSettings](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html) examples.

## See Also

[IExportSettings Interface](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html)
[IExportSettings Members](Interop.dsAutomation~Interop.dsAutomation.IExportSettings_members.html)
[IExportSettings::GetPrintMargins Method ()](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~GetPrintMargins.html)
[IExportSettings::SetPrintMargins Method ()](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~SetPrintMargins.html)

## Availability

DraftSight 2018 SP0
