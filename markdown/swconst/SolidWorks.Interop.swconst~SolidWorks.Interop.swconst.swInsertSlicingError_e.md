---
title: "swInsertSlicingError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swInsertSlicingError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInsertSlicingError_e.html"
---

# swInsertSlicingError_e Enumeration

Error codes for slicing insertion. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swInsertSlicingError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swInsertSlicingError_e
```

### C#

```csharp
public enum swInsertSlicingError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swInsertSlicingError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swInsertSlicingError_EntitiesCannotFormPlane | 0x10 = Point and provided line overlap |
| swInsertSlicingError_GenericError | 0x1 = Slicing inserted successfully |
| swInsertSlicingError_InvalidNumberOfPlanes | 0x80 = Number of planes must be <= 100 |
| swInsertSlicingError_InvalidSlicesToGenerateOption | 0x4 = Slicing method specified in ISlicingData::SlicesToGenerate is not valid |
| swInsertSlicingError_InvalidSlicingData | 0x40 = Null or invalid slicing data |
| swInsertSlicingError_InvalidSlicingPlaneEntities | 0x8 = None or invalid type of entities specified |
| swInsertSlicingError_InvalidTotalAngle | 0x2 = ( ISlicingData::NumberOfPlanes * ISlicingData::Offset ) is invalid |
| swInsertSlicingError_NoBodiesInsideBox | 0x20 = No bodies are inside the bounding box |
| swInsertSlicingError_NoError | 0x0 = Slicing inserted successfully |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
