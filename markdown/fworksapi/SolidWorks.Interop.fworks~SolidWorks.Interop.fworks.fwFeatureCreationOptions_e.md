---
title: "fwFeatureCreationOptions_e Enumeration"
project: "FeatureWorks API Help"
interface: "fwFeatureCreationOptions_e"
member: ""
kind: "enum"
source: "fworksapi/SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.fwFeatureCreationOptions_e.html"
---

# fwFeatureCreationOptions_e Enumeration

Feature creation options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum fwFeatureCreationOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As fwFeatureCreationOptions_e
```

### C#

```csharp
public enum fwFeatureCreationOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class fwFeatureCreationOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| fwAddConstraintsToSketch | 0x1 = When you specify this option, the software adds a Fix relation to each entity in a sketch, fully defining the sketch; if this option is not specified, then the sketch entities remain underdefined |
| fwAllowFailFeatureCreation | 0x2 = When you specify this option, the software allows the creation of a feature even if the feature has a rebuild error |

## See Also

[SolidWorks.Interop.fworks Namespace](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks_namespace.html)
