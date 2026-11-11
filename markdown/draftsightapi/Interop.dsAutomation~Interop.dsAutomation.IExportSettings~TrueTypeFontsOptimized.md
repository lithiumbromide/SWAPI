---
title: "TrueTypeFontsOptimized Property (IExportSettings)"
project: ""
interface: "IExportSettings"
member: "TrueTypeFontsOptimized"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExportSettings~TrueTypeFontsOptimized.html"
---

# TrueTypeFontsOptimized Property (IExportSettings)

Gets or sets whether to use TrueType font-related optimization when creating the PDF file.

## Syntax

### Visual Basic

```vb
Property TrueTypeFontsOptimized As System.Boolean
```

### C#

```csharp
System.bool TrueTypeFontsOptimized {get; set;}
```

### JScript

```
function get,set TrueTypeFontsOptimized : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_TrueTypeFontsOptimized();
__property void set_TrueTypeFontsOptimized(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool TrueTypeFontsOptimized {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True (default) to use TrueType font-related optimization, false to not

## Remarks

If this property is set to true, creating the PDF may take longer, but the size of the PDF may be smaller.

## See Also

[IExportSettings Interface](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html)
[IExportSettings Members](Interop.dsAutomation~Interop.dsAutomation.IExportSettings_members.html)
[IExportSettings::TrueTypeFontsType Property ()](Interop.dsAutomation~Interop.dsAutomation.IExportSettings~TrueTypeFontsType.html)

## Availability

DraftSight 2018 SP2
