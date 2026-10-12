---
title: "swConfigurationOptions2_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swConfigurationOptions2_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConfigurationOptions2_e.html"
---

# swConfigurationOptions2_e Enumeration

Option bits used when setting configuration options. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swConfigurationOptions2_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swConfigurationOptions2_e
```

### C#

```csharp
public enum swConfigurationOptions2_e : System.Enum
```

### C++/CLI

```cpp
public enum class swConfigurationOptions2_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swConfigOption_DoDisolveInBOM | 256 or 0x100; True to dissolve the configuration in the BOM and promote all of its child components up one level, false to not |
| swConfigOption_DontActivate | 128 or 0x80; True to not activate the configuration, false to activate the configuration |
| swConfigOption_DontShowPartsInBOM | 2 or 0x2; True to show sub-assemblies in the Bill of Materials, false to list child components in the Bill of Materials |
| swConfigOption_HideByDefault | 8 or 0x8; True to hide newly added components, false to not |
| swConfigOption_InheritProperties | Obsolete |
| swConfigOption_LinkToParent | 64 or 0x40; True to link component to parent configuration, false to not |
| swConfigOption_MinFeatureManager | 16 or 0x10; True to suppress new components, false to not |
| swConfigOption_SuppressByDefault | 4 or 0x4; True to suppress newly added features and mates in this configuration, false to not |
| swConfigOption_UseAlternateName | 1 or 0x1; True to use an alternate configuration name, false to not |
| swConfigOption_UseDescriptionInBOM | 512 or 0x200; True to use the description in the BOM, false to not |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
