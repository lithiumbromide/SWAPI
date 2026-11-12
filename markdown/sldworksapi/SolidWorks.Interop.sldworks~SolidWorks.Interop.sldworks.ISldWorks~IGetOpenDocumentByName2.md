---
title: "IGetOpenDocumentByName2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetOpenDocumentByName2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.html"
---

# IGetOpenDocumentByName2 Method (ISldWorks)

Gets the open document with the specified name.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetOpenDocumentByName2( _
   ByVal DocumentName As System.String _
) As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DocumentName As System.String
Dim value As ModelDoc2

value = instance.IGetOpenDocumentByName2(DocumentName)
```

### C#

```csharp
ModelDoc2 IGetOpenDocumentByName2(
   System.string DocumentName
)
```

### C++/CLI

```cpp
ModelDoc2^ IGetOpenDocumentByName2(
   System.String^ DocumentName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentName`: Fully qualified name of the open document (path, filename, and file extension)

### Return Value

Open [model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) or NULL if the operation fails

## VBA Syntax

See [SldWorks::IGetOpenDocumentByName2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IGetOpenDocumentByName2.html).

## Remarks

Only call this method for a document that has already been opened in its own window. If you call this method for a document that has not been opened in its own window, then methods on the returned object may not work as expected.

This method is useful for getting a SOLIDWORKS document object when you only have the document name. For example, SOLIDWORKS event [FileOpenNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler.html) provides the filename of the document opened, and you can use that name with this method to get the document's object pointer.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.html)
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html)
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.html)
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html)
[ISldWorks::EnumDocuments2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnumDocuments2.html)
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.html)
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
