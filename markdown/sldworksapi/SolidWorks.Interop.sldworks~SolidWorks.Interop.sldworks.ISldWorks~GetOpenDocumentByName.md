---
title: "GetOpenDocumentByName Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetOpenDocumentByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html"
---

# GetOpenDocumentByName Method (ISldWorks)

Gets the open document with the specified name.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOpenDocumentByName( _
   ByVal DocumentName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DocumentName As System.String
Dim value As System.Object

value = instance.GetOpenDocumentByName(DocumentName)
```

### C#

```csharp
System.object GetOpenDocumentByName(
   System.string DocumentName
)
```

### C++/CLI

```cpp
System.Object^ GetOpenDocumentByName(
   System.String^ DocumentName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentName`: Fully qualified name of the open document (path, filename, and file extension)

### Return Value

Open [model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) or NULL if the operation fails

## VBA Syntax

See [SldWorks::GetOpenDocumentByName](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetOpenDocumentByName.html).

## Examples

[Get Differences Between Parts (VBA)](Get_Differences_Between_Parts_Example_VB.htm)

## Remarks

Only call this method for a document that has already been opened in its own window. If you call this method for a document that has not been opened in its own window, then methods on the returned object may not work as expected.

This method is useful for getting a SOLIDWORKS document object when you only have the document name. For example, SOLIDWORKS event [FileOpenNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler.html) provides the file name of the document opened, and you can use that name with this method to get the document's object pointer.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.html)
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html)
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.html)
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.html)
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.html)
[ISldWorks::EnumDocuments2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnumDocuments2.html)
[ISldWorks::IGetOpenDocumentByName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.html)
[ISldWorks::GetDocumentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentCount.html)
[ISldWorks::GetDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocuments.html)
[ISldWorks::IGetDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocuments.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
