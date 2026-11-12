---
title: "IGetFirstDocument2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetFirstDocument2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.html"
---

# IGetFirstDocument2 Method (ISldWorks)

Gets the document opened first in this SOLIDWORKS Design session.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstDocument2() As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As ModelDoc2

value = instance.IGetFirstDocument2()
```

### C#

```csharp
ModelDoc2 IGetFirstDocument2()
```

### C++/CLI

```cpp
ModelDoc2^ IGetFirstDocument2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) first opened

## VBA Syntax

See [SldWorks::IGetFirstDocument2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IGetFirstDocument2.html).

## Remarks

If the document first opened is an assembly, then this method returns the name of the first component document opened in that assembly.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.html)
[ISldWorks::ActiveDoc Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.html)
[ISldWorks::IActiveDoc2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.html)
[ISldWorks::EnumDocuments2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnumDocuments2.html)
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.html)
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html)
[ISldWorks::CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.html)
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html)

## Availability

SOLIDWORKS 98Plus, datecode 1998319
