---
title: "fwInteractiveRecognitionOptions_e Enumeration"
project: "FeatureWorks API Help"
interface: "fwInteractiveRecognitionOptions_e"
member: ""
kind: "enum"
source: "fworksapi/SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.fwInteractiveRecognitionOptions_e.html"
---

# fwInteractiveRecognitionOptions_e Enumeration

Interactive recognition options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum fwInteractiveRecognitionOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As fwInteractiveRecognitionOptions_e
```

### C#

```csharp
public enum fwInteractiveRecognitionOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class fwInteractiveRecognitionOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| fwChainFeatures | 0x1 = Chain feature faces. Applies to these features: Fillets Chamfers Boss revolve Cut revolve Holes |
| fwNormalToSketch | 0x2 = Turn on or turn off normal to sketch |

## See Also

[SolidWorks.Interop.fworks Namespace](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks_namespace.html)
