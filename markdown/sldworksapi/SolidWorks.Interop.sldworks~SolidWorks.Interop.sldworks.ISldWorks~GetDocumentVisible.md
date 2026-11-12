---
title: "GetDocumentVisible Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetDocumentVisible"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentVisible.html"
---

# GetDocumentVisible Method (ISldWorks)

Gets the visibility of the document to open.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDocumentVisible( _
   ByVal Type As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Type As System.Integer
Dim value As System.Boolean

value = instance.GetDocumentVisible(Type)
```

### C#

```csharp
System.bool GetDocumentVisible(
   System.int Type
)
```

### C++/CLI

```cpp
System.bool GetDocumentVisible(
   System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Document type as defined by [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

### Return Value

True if the document will be visible when opened, false if not

## VBA Syntax

See [SldWorks::GetDocumentVisible](ms-its:sldworksapivb6.chm::/Sldworks~SldWorks~GetDocumentVisible.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
