---
title: "GetFirstDocument Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetFirstDocument"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.html"
---

# GetFirstDocument Method (ISldWorks)

Gets the document opened first in this SOLIDWORKS Design session.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstDocument() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Object

value = instance.GetFirstDocument()
```

### C#

```csharp
System.object GetFirstDocument()
```

### C++/CLI

```cpp
System.Object^ GetFirstDocument();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) first opened

## VBA Syntax

See [SldWorks::GetFirstDocument](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetFirstDocument.html).

## Examples

[Determine If Document is Dirty (VBA)](Determine_if_Document_is_Dirty_Example_VB.htm)
[Get Names of Open Documents (VBA)](Get_Names_of_Open_Documents_Example_VB.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (C#)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_CSharp.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (VB.NET)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VBNET.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (VBA)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VB.htm)

## Remarks

If the document first opened is an assembly, then this method returns the name of the first component document opened in that assembly.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.html)
[ISldWorks::ActiveDoc Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.html)
[ISldWorks::IActiveDoc2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.html)
[ISldWorks::EnumDocuments2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnumDocuments2.html)
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.html)
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html)
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html)
[ISldWorks::CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.html)
[ISldWorks::GetDocumentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentCount.html)
[ISldWorks::GetDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocuments.html)
[ISldWorks::IGetDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocuments.html)

## Availability

SOLIDWORKS 98Plus, datecode 1998319
