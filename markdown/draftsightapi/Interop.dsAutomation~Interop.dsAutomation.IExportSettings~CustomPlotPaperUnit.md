---
title: "CustomPlotPaperUnit Property (IExportSettings)"
project: ""
interface: "IExportSettings"
member: "CustomPlotPaperUnit"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExportSettings~CustomPlotPaperUnit.html"
---

# CustomPlotPaperUnit Property (IExportSettings)

Gets or sets the units of plot paper size.

## Syntax

### Visual Basic

```vb
Property CustomPlotPaperUnit As dsPlotPaperUnits_e
```

### C#

```csharp
dsPlotPaperUnits_e CustomPlotPaperUnit {get; set;}
```

### JScript

```
function get,set CustomPlotPaperUnit : dsPlotPaperUnits_e
```

### Managed Extensions for C++

```
__property dsPlotPaperUnits_e get_CustomPlotPaperUnit();
__property void set_CustomPlotPaperUnit(
   dsPlotPaperUnits_e value
);
```

### C++/CLI

```cpp
property dsPlotPaperUnits_e CustomPlotPaperUnit {
   dsPlotPaperUnits_e get();
   void set (    dsPlotPaperUnits_e value);
}
```

### Property Value

Units of plot paper size as defined by [dsPlotPaperUnits_e](Interop.dsAutomation~Interop.dsAutomation.dsPlotPaperUnits_e.html)

## Remarks

This property is valid only if [IExportSettings::UseCustomPaperSize](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~UseCustomPaperSize.html) is set to true.

## See Also

[IExportSettings Interface](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html)
[IExportSettings Members](Interop.dsAutomation~Interop.dsAutomation.IExportSettings_members.html)

## Availability

DraftSight 2024 SP1
