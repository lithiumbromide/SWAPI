---
title: "IGetOpenDocumentByName Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetOpenDocumentByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName.html"
---

# IGetOpenDocumentByName Method (ISldWorks)

Obsolete. Superseded [ISldWorks::IGetOpenDocumentByName2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetOpenDocumentByName( _
   ByVal DocumentName As System.String _
) As ModelDoc
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DocumentName As System.String
Dim value As ModelDoc

value = instance.IGetOpenDocumentByName(DocumentName)
```

### C#

```csharp
ModelDoc IGetOpenDocumentByName(
   System.string DocumentName
)
```

### C++/CLI

```cpp
ModelDoc^ IGetOpenDocumentByName(
   System.String^ DocumentName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentName`:

## VBA Syntax

See [SldWorks::IGetOpenDocumentByName](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IGetOpenDocumentByName.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
