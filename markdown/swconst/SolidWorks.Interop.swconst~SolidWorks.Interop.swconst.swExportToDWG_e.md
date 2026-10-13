---
title: "swExportToDWG_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swExportToDWG_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swExportToDWG_e.html"
---

# swExportToDWG_e Enumeration

Options for the Action parameter of [IPartDoc::ExportToDWG2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IExportToDWG2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swExportToDWG_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swExportToDWG_e
```

### C#

```csharp
public enum swExportToDWG_e : System.Enum
```

### C++/CLI

```cpp
public enum class swExportToDWG_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swExportToDWG_ExportAnnotationViews | 3 |
| swExportToDWG_ExportSelectedFacesOrLoops | 2 |
| swExportToDWG_ExportSheetMetal | 1; Valid only if the active document contains sheet metal |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
