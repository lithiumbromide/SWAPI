---
title: "EnableSaveBackToDrawingPropertiesData Property (IExportSettings)"
project: ""
interface: "IExportSettings"
member: "EnableSaveBackToDrawingPropertiesData"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExportSettings~EnableSaveBackToDrawingPropertiesData.html"
---

# EnableSaveBackToDrawingPropertiesData Property (IExportSettings)

Gets or sets whether to save drawing properties back to the drawing.

## Syntax

### Visual Basic

```vb
Property EnableSaveBackToDrawingPropertiesData As System.Boolean
```

### C#

```csharp
System.bool EnableSaveBackToDrawingPropertiesData {get; set;}
```

### JScript

```
function get,set EnableSaveBackToDrawingPropertiesData : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_EnableSaveBackToDrawingPropertiesData();
__property void set_EnableSaveBackToDrawingPropertiesData(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool EnableSaveBackToDrawingPropertiesData {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True (default) to save drawing properties back to the drawing, false to not

## Remarks

If this property is set to true, current drawing properties may be overwritten during export to the PDF.

## See Also

[IExportSettings Interface](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html)
[IExportSettings Members](Interop.dsAutomation~Interop.dsAutomation.IExportSettings_members.html)

## Availability

DraftSight 2018 SP2
