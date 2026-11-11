---
title: "UseCustomPaperSize Property (IExportSettings)"
project: ""
interface: "IExportSettings"
member: "UseCustomPaperSize"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExportSettings~UseCustomPaperSize.html"
---

# UseCustomPaperSize Property (IExportSettings)

Gets or sets whether to use a custom paper size.

## Syntax

### Visual Basic

```vb
Property UseCustomPaperSize As System.Boolean
```

### C#

```csharp
System.bool UseCustomPaperSize {get; set;}
```

### JScript

```
function get,set UseCustomPaperSize : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_UseCustomPaperSize();
__property void set_UseCustomPaperSize(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool UseCustomPaperSize {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to use a custom paper size, false to not

## Remarks

This property corresponds to the PDF Export dialog **Paper size > Custom** toggle. After setting this property to true, set the custom paper [height](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~CustomPaperHeight.html), [width](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~CustomPaperWidth.html), and [units](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~CustomPlotPaperUnit.html).

## See Also

[IExportSettings Interface](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html)
[IExportSettings Members](Interop.dsAutomation~Interop.dsAutomation.IExportSettings_members.html)
[IExportSettings::CustomPaperHeight Property ()](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~CustomPaperHeight.html)
[IExportSettings::CustomPaperWidth Property ()](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~CustomPaperWidth.html)
[IExportSettings::CustomPlotPaperUnit Property ()](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~CustomPlotPaperUnit.html)

## Availability

DraftSight 2024 SP1
