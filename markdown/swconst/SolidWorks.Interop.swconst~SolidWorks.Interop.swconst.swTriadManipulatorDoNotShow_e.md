---
title: "swTriadManipulatorDoNotShow_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swTriadManipulatorDoNotShow_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTriadManipulatorDoNotShow_e.html"
---

# swTriadManipulatorDoNotShow_e Enumeration

Triad manipulator visibility options. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swTriadManipulatorDoNotShow_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swTriadManipulatorDoNotShow_e
```

### C#

```csharp
public enum swTriadManipulatorDoNotShow_e : System.Enum
```

### C++/CLI

```cpp
public enum class swTriadManipulatorDoNotShow_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swTriadManipulatorDoNotShowOrigin | 1 or 0x1; Not used. |
| swTriadManipulatorDoNotShowXAxis | 2 or 0x2; Do not show x axis |
| swTriadManipulatorDoNotShowXYPlane | 16 or 0x10; Do not show xy plane |
| swTriadManipulatorDoNotShowXYRING | 128 or 0x80; Do not show xy ring |
| swTriadManipulatorDoNotShowYAxis | 4 or 0x4; Do not show y axis |
| swTriadManipulatorDoNotShowYZPlane | 32 or 0x20; Do not show yz plane |
| swTriadManipulatorDoNotShowYZRING | 256 or 0x100; Do not show yz ring |
| swTriadManipulatorDoNotShowZAxis | 8 or 0x8; Do not show z axis |
| swTriadManipulatorDoNotShowZXPlane | 64 or 0x40; Do not show zx plane |
| swTriadManipulatorDoNotShowZXRING | 512 or 0x200; Do not show zx ring |
| swTriadManipulatorShowAll | 0 or 0x0; Show all |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
