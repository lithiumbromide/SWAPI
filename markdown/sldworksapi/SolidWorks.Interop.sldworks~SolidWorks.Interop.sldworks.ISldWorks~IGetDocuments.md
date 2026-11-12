---
title: "IGetDocuments Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetDocuments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocuments.html"
---

# IGetDocuments Method (ISldWorks)

Gets the open documents is this SOLIDWORKS Design session.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDocuments( _
   ByVal NumDocuments As System.Integer _
) As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim NumDocuments As System.Integer
Dim value As ModelDoc2

value = instance.IGetDocuments(NumDocuments)
```

### C#

```csharp
ModelDoc2 IGetDocuments(
   System.int NumDocuments
)
```

### C++/CLI

```cpp
ModelDoc2^ IGetDocuments(
   System.int NumDocuments
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumDocuments`: Number of open documents

### Return Value

- in-process, unmanaged C++: Pointer ot an array of open [documents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) in this SOLIDWORKS Design session

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISldWorks::GetDocumentCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetDocumentCount.html) to get NumDocuments.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.html)
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html)
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.html)
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.html)
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html)
[ISldWorks::GetDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocuments.html)
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.html)
[ISldWorks::IGetOpenDocumentByName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
