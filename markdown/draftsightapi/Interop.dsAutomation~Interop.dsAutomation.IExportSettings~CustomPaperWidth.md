---
title: "CustomPaperWidth Property (IExportSettings)"
project: ""
interface: "IExportSettings"
member: "CustomPaperWidth"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExportSettings~CustomPaperWidth.html"
---

# CustomPaperWidth Property (IExportSettings)

Gets or sets the custom paper width.

## Syntax

### Visual Basic

```vb
Property CustomPaperWidth As System.Double
```

### C#

```csharp
System.double CustomPaperWidth {get; set;}
```

### JScript

```
function get,set CustomPaperWidth : System.double
```

### Managed Extensions for C++

```
__property System.double get_CustomPaperWidth();
__property void set_CustomPaperWidth(
   System.double value
);
```

### C++/CLI

```cpp
property System.double CustomPaperWidth {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Custom paper width

## Remarks

This property is valid only if [IExportSettings::UseCustomPaperSize](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~UseCustomPaperSize.html) is set to true.

## See Also

[IExportSettings Interface](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html)
[IExportSettings Members](Interop.dsAutomation~Interop.dsAutomation.IExportSettings_members.html)
[IExportSettings::CustomPaperHeight Property ()](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~CustomPaperHeight.html)
[IExportSettings::CustomPlotPaperUnit Property ()](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~CustomPlotPaperUnit.html)

## Availability

DraftSight 2024 SP1
