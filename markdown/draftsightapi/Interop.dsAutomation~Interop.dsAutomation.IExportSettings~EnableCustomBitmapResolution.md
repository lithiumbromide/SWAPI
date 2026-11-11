---
title: "EnableCustomBitmapResolution Property (IExportSettings)"
project: ""
interface: "IExportSettings"
member: "EnableCustomBitmapResolution"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExportSettings~EnableCustomBitmapResolution.html"
---

# EnableCustomBitmapResolution Property (IExportSettings)

Gets or sets whether to enable custom bitmap resolution.

## Syntax

### Visual Basic

```vb
Property EnableCustomBitmapResolution As System.Boolean
```

### C#

```csharp
System.bool EnableCustomBitmapResolution {get; set;}
```

### JScript

```
function get,set EnableCustomBitmapResolution : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_EnableCustomBitmapResolution();
__property void set_EnableCustomBitmapResolution(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool EnableCustomBitmapResolution {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to enable, false to not (default)

## Examples

See the [IExportSettings](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html) examples.

## Remarks

If this property is set to true, then use [IExportSettings::CustomBitmapResolution](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~CustomBitmapResolution.html) to set the custom bitmap resolution.

## See Also

[IExportSettings Interface](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html)
[IExportSettings Members](Interop.dsAutomation~Interop.dsAutomation.IExportSettings_members.html)

## Availability

DraftSight 2018 SP0
