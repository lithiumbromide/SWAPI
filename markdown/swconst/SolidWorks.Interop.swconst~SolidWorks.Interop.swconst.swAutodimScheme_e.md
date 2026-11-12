---
title: "swAutodimScheme_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAutodimScheme_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimScheme_e.html"
---

# swAutodimScheme_e Enumeration

Dimensioning schemes for [ISketch::AutoDimension2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~AutoDimension2.html)ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~AutoDimension.html and [IDrawingDoc::AutoDimension](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IDrawingDoc~AutoDimension.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAutodimScheme_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAutodimScheme_e
```

### C#

```csharp
public enum swAutodimScheme_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAutodimScheme_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAutodimSchemeBaseline | 1 = Use a baseline dimensioning scheme |
| swAutodimSchemeCenterline | 4 = Not supported in sketches or drawings; do not use |
| swAutodimSchemeChain | 3 = Use a chain dimensioning scheme |
| swAutodimSchemeOrdinate | 2 = Use an ordinate dimensioning scheme |

## Remarks

The horizontal and vertical dimension placements are specified independently using the HorizontalPlacement and VerticalPlacement parameters in the methods.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
