---
title: "GetOpenDocument Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetOpenDocument"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.html"
---

# GetOpenDocument Method (ISldWorks)

Gets the open document with the specified name.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOpenDocument( _
   ByVal DocName As System.String _
) As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DocName As System.String
Dim value As ModelDoc2

value = instance.GetOpenDocument(DocName)
```

### C#

```csharp
ModelDoc2 GetOpenDocument(
   System.string DocName
)
```

### C++/CLI

```cpp
ModelDoc2^ GetOpenDocument(
   System.String^ DocName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocName`: Name of the document (see **Remarks**)

### Return Value

[Model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html)

## VBA Syntax

See [SldWorks::GetOpenDocument](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetOpenDocument.html).

## Examples

[Get Names of Open Documents (VBA)](Get_Names_of_Open_Documents_Example_VB.htm)

## Remarks

Only call this method for a document that has already been opened in its own window. If you call this method for a document that has not been opened in its own window, then methods on the returned object may not work as expected.

If you do not specify a file extension in the DocName argument, then the file extension of the document is ignored. This can cause problems if you have two different document types with the same name opened; for example, **12345.sldprt** and **12345.**sldasm.

If you do not specify the file extension in your call to this method, then you cannot be sure which document is retrieved. To avoid this problem, you can specify the filename extension in the DocName parameter or you can check the document type after it is activated using [IModelDoc2::GetType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetType.html).

| If DocName is an empty string, and... | Then this method returns... |
| --- | --- |
| An assembly is opened | The first part of the assembly |
| Multiple assemblies are opened | The first part of the first assembly |
| Multile parts are opened | The first part |

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.html)
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html)
[ISldWorks::EnumDocuments2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnumDocuments2.html)
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.html)
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html)
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.html)
[ISldWorks::IGetDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocuments.html)
[ISldWorks::GetDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocuments.html)
[ISldWorks::GetDocumentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentCount.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
