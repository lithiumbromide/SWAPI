---
title: "CloseAllDocuments Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "CloseAllDocuments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.html"
---

# CloseAllDocuments Method (ISldWorks)

Closes all open documents in the SOLIDWORKS Design session.

## Syntax

### Visual Basic (Declaration)

```vb
Function CloseAllDocuments( _
   ByVal IncludeUnsaved As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim IncludeUnsaved As System.Boolean
Dim value As System.Boolean

value = instance.CloseAllDocuments(IncludeUnsaved)
```

### C#

```csharp
System.bool CloseAllDocuments(
   System.bool IncludeUnsaved
)
```

### C++/CLI

```cpp
System.bool CloseAllDocuments(
   System.bool IncludeUnsaved
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IncludeUnsaved`: - True = Close all documents, including dirty documents
  - False = Close all documents, excluding dirty documents

### Return Value

True if method executes successfully, false if not

## VBA Syntax

See [SldWorks::CloseAllDocuments](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~CloseAllDocuments.html).

## Examples

[Close All Documents (VBA)](Close_all_Documents_Example_VB.htm)
[Keep SOLIDWORKS Invisible While Activating Documents (C#)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_CSharp.htm)
[Keep SOLIDWORKS Invisible While Activating Documents (VB.NET)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VBNET.htm)
[Keep SOLIDWORKS Invisible While Activating Documents (VBA)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VB.htm)
[Switch Documents (C#)](Switch_Documents_Example_CSharp.htm)
[Switch Documents (VB.NET)](Switch_Documents_Example_VBNET.htm)
[Switch Documents (VBA)](Switch_Documents_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html)
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.html)
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html)
[ISldWorks::OpenDoc6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.html)
[ISldWorks::ActiveDoc Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.html)
[ISldWorks::IActiveDoc2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.html)
[ISldWorks::QuitDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~QuitDoc.html)
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.html)
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.html)
[ISldWorks::IGetDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocuments.html)
[ISldWorks::GetDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocuments.html)
[ISldWorks::GetDocumentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentCount.html)
[ISldWorks::CloseAndReopen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAndReopen.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
