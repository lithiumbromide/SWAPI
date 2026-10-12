---
title: "fwAdvancedOptions_e Enumeration"
project: "FeatureWorks API Help"
interface: "fwAdvancedOptions_e"
member: ""
kind: "enum"
source: "fworksapi/SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.fwAdvancedOptions_e.html"
---

# fwAdvancedOptions_e Enumeration

Feature advanced options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum fwAdvancedOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As fwAdvancedOptions_e
```

### C#

```csharp
public enum fwAdvancedOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class fwAdvancedOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| fwAdvAddConstraintsToSketch | 0x1 = Add constraints to a feature's sketch |
| fwAdvAllowFailFeatureCreation | 0x2 = Allow creation of a feature even if the feature has a rebuild error |
| fwAdvAllowWizardHoleRecognition | 0x4 = Recognize a hole as a wizard hole |

## See Also

[SolidWorks.Interop.fworks Namespace](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks_namespace.html)
