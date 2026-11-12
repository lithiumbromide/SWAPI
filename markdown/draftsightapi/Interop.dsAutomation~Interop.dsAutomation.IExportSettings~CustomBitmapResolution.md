---
title: "CustomBitmapResolution Property (IExportSettings)"
project: ""
interface: "IExportSettings"
member: "CustomBitmapResolution"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExportSettings~CustomBitmapResolution.html"
---

# CustomBitmapResolution Property (IExportSettings)

Gets or sets the custom bitmap resolution.

## Syntax

### Visual Basic

```vb
Property CustomBitmapResolution As System.Double
```

### C#

```csharp
System.double CustomBitmapResolution {get; set;}
```

### JScript

```
function get,set CustomBitmapResolution : System.double
```

### Managed Extensions for C++

```
__property System.double get_CustomBitmapResolution();
__property void set_CustomBitmapResolution(
   System.double value
);
```

### C++/CLI

```cpp
property System.double CustomBitmapResolution {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Custom bitmap resolution; default is 150 dpi

## Examples

See the [IExportSettings](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html) examples.

## Remarks

This property is valid only if [IExportSettings::EnableCustomBitmapResolution](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~EnableCustomBitmapResolution.html) is set to true.

## See Also

[IExportSettings Interface](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html)
[IExportSettings Members](Interop.dsAutomation~Interop.dsAutomation.IExportSettings_members.html)

## Availability

DraftSight 2018 SP0
