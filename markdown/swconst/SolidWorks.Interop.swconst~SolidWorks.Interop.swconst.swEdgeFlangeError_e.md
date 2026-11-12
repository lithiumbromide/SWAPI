---
title: "swEdgeFlangeError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swEdgeFlangeError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEdgeFlangeError_e.html"
---

# swEdgeFlangeError_e Enumeration

Edge flange error codes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swEdgeFlangeError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swEdgeFlangeError_e
```

### C#

```csharp
public enum swEdgeFlangeError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swEdgeFlangeError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swEdgeFlangeError_EdgeAlreadyExists | 4 = Specified edge already exists |
| swEdgeFlangeError_EdgeNotSpecified | 1 = Input array of edges is empty |
| swEdgeFlangeError_GenericError | 7 = Unknown error |
| swEdgeFlangeError_InvalidEdge | 5 = Specified edge is invalid |
| swEdgeFlangeError_MustSpecifyAtLeastOneEdge | 6 = You must specify at least one edge |
| swEdgeFlangeError_NoError | 0 = No error |
| swEdgeFlangeError_NumberOfEdgesAndSketchesNotEqual | 3 = Number of edges must equal the number of sketches |
| swEdgeFlangeError_SketchNotSpecified | 2 = Input array of sketches is empty |

## Remarks

These error codes are returned by [IEdgeFlangeFeatureData::AddEdges](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdgeFlangeFeatureData~AddEdges.html) and [IEdgeFlangeFeatureData::RemoveEdges](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdgeFlangeFeatureData~RemoveEdges.html).

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
