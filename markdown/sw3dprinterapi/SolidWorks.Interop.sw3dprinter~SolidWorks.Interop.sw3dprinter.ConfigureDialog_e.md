---
title: "ConfigureDialog_e Enumeration"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ConfigureDialog_e"
member: ""
kind: "enum"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ConfigureDialog_e.html"
---

# ConfigureDialog_e Enumeration

Disables buttons and fields on Print dialog. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum ConfigureDialog_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As ConfigureDialog_e
```

### C#

```csharp
public enum ConfigureDialog_e : System.Enum
```

### C++/CLI

```cpp
public enum class ConfigureDialog_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| DisableAdvancedSettingsButton | 16 |
| DisableCostField | 32 |
| DisableOrientationBestSurfaceQualityOption | 4 |
| DisableOrientationMinimumBuildTimeOption | 2 |
| DisableOrientationSpecifyInAdvancedOption | 8 |
| DisablePrintQualitySpecifyInAdvancedOption | 1 |
| DisableQuantityControl | 64 |
| DisableUpdateStatisticsButton | 128 |
| OkButtonAlwaysEnabled | 256 |

## See Also

[SolidWorks.Interop.sw3dprinter Namespace](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter_namespace.html)
