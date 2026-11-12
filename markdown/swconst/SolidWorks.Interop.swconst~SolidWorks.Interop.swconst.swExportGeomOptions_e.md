---
title: "swExportGeomOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swExportGeomOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swExportGeomOptions_e.html"
---

# swExportGeomOptions_e Enumeration

DXF/DWG geometry export options.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swExportGeomOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swExportGeomOptions_e
```

### C#

```csharp
public enum swExportGeomOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swExportGeomOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swExportGeomAsPoly | -1 = Export geometry as polylines |
| swExportNone | -2 = None (default) |
| swExportTopLevelCompAsBlock | 1 = Export top-level components as blocks |
| swExportViewAsBlock | 0 = Export views as blocks (default for System Options for DXF/DWG View Geometry) |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
