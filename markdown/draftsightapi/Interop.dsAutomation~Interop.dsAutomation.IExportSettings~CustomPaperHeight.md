---
title: "CustomPaperHeight Property (IExportSettings)"
project: ""
interface: "IExportSettings"
member: "CustomPaperHeight"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExportSettings~CustomPaperHeight.html"
---

# CustomPaperHeight Property (IExportSettings)

Gets or sets the custom paper height.

## Syntax

### Visual Basic

```vb
Property CustomPaperHeight As System.Double
```

### C#

```csharp
System.double CustomPaperHeight {get; set;}
```

### JScript

```
function get,set CustomPaperHeight : System.double
```

### Managed Extensions for C++

```
__property System.double get_CustomPaperHeight();
__property void set_CustomPaperHeight(
   System.double value
);
```

### C++/CLI

```cpp
property System.double CustomPaperHeight {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Custom paper height

## Remarks

This property is valid only if [IExportSettings::UseCustomPaperSize](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~UseCustomPaperSize.html) is set to true.

## See Also

[IExportSettings Interface](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html)
[IExportSettings Members](Interop.dsAutomation~Interop.dsAutomation.IExportSettings_members.html)
[IExportSettings::CustomPaperWidth Property ()](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~CustomPaperWidth.html)
[IExportSettings::CustomPlotPaperUnit Property ()](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~CustomPlotPaperUnit.html)

## Availability

DraftSight 2024 SP1
