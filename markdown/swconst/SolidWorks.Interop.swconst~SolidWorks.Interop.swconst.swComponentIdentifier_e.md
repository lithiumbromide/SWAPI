---
title: "swComponentIdentifier_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swComponentIdentifier_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentIdentifier_e.html"
---

# swComponentIdentifier_e Enumeration

Component display options for the FeatureManager design tree. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swComponentIdentifier_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swComponentIdentifier_e
```

### C#

```csharp
public enum swComponentIdentifier_e : System.Enum
```

### C++/CLI

```cpp
public enum class swComponentIdentifier_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swComponentIdentifier_ComponentDescription | 4 |
| swComponentIdentifier_ComponentName | 2 |
| swComponentIdentifier_ConfigurationDescription | 64 |
| swComponentIdentifier_ConfigurationName | 32 |
| swComponentIdentifier_DisplayStateName | 128 |
| swComponentIdentifier_EnterpriseItemNumber | 8 (valid only in SOLIDWORKS Design connected to the 3DEXPERIENCE platform) |
| swComponentIdentifier_FileTitle | 256 (valid only in SOLIDWORKS Design connected to the 3DEXPERIENCE platform) |
| swComponentIdentifier_None | 0 |
| swComponentIdentifier_PhysicalProductDescription | 16 (valid only in SOLIDWORKS Design connected to the 3DEXPERIENCE platform) |
| swComponentIdentifier_PhysicalProductTitle | 1 (valid only in SOLIDWORKS Design connected to the 3DEXPERIENCE platform) |
| swComponentIdentifier_PLMRevision | 512 (valid only in SOLIDWORKS Design connected to the 3DEXPERIENCE platform) |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
