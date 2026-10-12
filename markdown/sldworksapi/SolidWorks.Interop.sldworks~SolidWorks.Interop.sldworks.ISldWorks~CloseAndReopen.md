---
title: "CloseAndReopen Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "CloseAndReopen"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAndReopen.html"
---

# CloseAndReopen Method (ISldWorks)

Closes and reopens the specified drawing document without unloading its references from memory.

## Syntax

### Visual Basic (Declaration)

```vb
Function CloseAndReopen( _
   ByVal Doc As ModelDoc2, _
   ByVal Option As System.Integer, _
   ByRef NewDoc As ModelDoc2 _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Doc As ModelDoc2
Dim Option As System.Integer
Dim NewDoc As ModelDoc2
Dim value As System.Integer

value = instance.CloseAndReopen(Doc, Option, NewDoc)
```

### C#

```csharp
System.int CloseAndReopen(
   ModelDoc2 Doc,
   System.int Option,
   out ModelDoc2 NewDoc
)
```

### C++/CLI

```cpp
System.int CloseAndReopen(
   ModelDoc2^ Doc,
   System.int Option,
   [Out] ModelDoc2^ NewDoc
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Doc`: [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html); drawing document to close and reopen
- `Option`: Reopen options as defined in [swCloseReopenOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCloseReopenOption_e.html)
- `NewDoc`: [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html); reopened drawing document

### Return Value

Error code as defined in [swCloseReopenError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCloseReopenError_e.html)

## VBA Syntax

See [SldWorks::CloseAndReopen](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~CloseAndReopen.html).

## Examples

Contact SOLIDWORKS API Support to obtain **Close and Reopen a Drawing Document (VBA, VB.NET, C#)**.

## Remarks

Before a third-party application can process a drawing document that is open in SOLIDWORKS, it must close the document. Usually when a drawing document is closed, its references are unloaded from memory, and reopening the drawing document takes a lot of time. This method closes a drawing document, keeps its references in memory, and quickly reopens it.

After the drawing document is closed and before it is reopened, SOLIDWORKS fires a [FileCloseNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_FileCloseNotifyEventHandler.html) event with reason [swFileCloseNotifyReason_e.swFileCloseNotifyReason_CloseForReload](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileCloseNotifyReason_e.html). In the handler of this event, a third-party application can call [ISldWorks::SetPromptFileName2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetPromptFilename2.html) to open a different file, or it can process the specified document before it is reopened in SOLIDWORKS.

See [IModelDoc2::ReloadOrReplace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ReloadOrReplace.html) to perform a similar function with part and assembly documents.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.html)
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html)
[ISldWorks::QuitDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~QuitDoc.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
