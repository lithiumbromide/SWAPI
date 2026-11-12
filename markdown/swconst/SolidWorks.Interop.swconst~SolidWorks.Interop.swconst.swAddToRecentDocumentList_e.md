---
title: "swAddToRecentDocumentList_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAddToRecentDocumentList_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAddToRecentDocumentList_e.html"
---

# swAddToRecentDocumentList_e Enumeration

Recent Documents list actions for a document opened using [ISldWorks::OpenDoc7](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.html) and [IDocumentSpecification::AddToRecentDocumentList](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~AddToRecentDocumentList.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAddToRecentDocumentList_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAddToRecentDocumentList_e
```

### C#

```csharp
public enum swAddToRecentDocumentList_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAddToRecentDocumentList_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAddToRecentDocumentList_Add | 1 |
| swAddToRecentDocumentList_Default | 0 = Default OpenDoc7 action: if a configuration is specified, the document is not added to the Recent Documents list; if a configuration is not specified, the document is added |
| swAddToRecentDocumentList_DontAdd | 2 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
