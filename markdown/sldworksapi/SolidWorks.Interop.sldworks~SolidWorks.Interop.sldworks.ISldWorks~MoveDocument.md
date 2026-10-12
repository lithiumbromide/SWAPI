---
title: "MoveDocument Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "MoveDocument"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~MoveDocument.html"
---

# MoveDocument Method (ISldWorks)

Moves a document and optionally updates references to it.

## Syntax

### Visual Basic (Declaration)

```vb
Function MoveDocument( _
   ByVal SourceDoc As System.String, _
   ByVal DestDoc As System.String, _
   ByVal FromChildren As System.Object, _
   ByVal ToChildren As System.Object, _
   ByVal Option As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim SourceDoc As System.String
Dim DestDoc As System.String
Dim FromChildren As System.Object
Dim ToChildren As System.Object
Dim Option As System.Integer
Dim value As System.Integer

value = instance.MoveDocument(SourceDoc, DestDoc, FromChildren, ToChildren, Option)
```

### C#

```csharp
System.int MoveDocument(
   System.string SourceDoc,
   System.string DestDoc,
   System.object FromChildren,
   System.object ToChildren,
   System.int Option
)
```

### C++/CLI

```cpp
System.int MoveDocument(
   System.String^ SourceDoc,
   System.String^ DestDoc,
   System.Object^ FromChildren,
   System.Object^ ToChildren,
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SourceDoc`: Full path and filename of the document to move
- `DestDoc`: Full path and filename of the new document to which to move the document specified for SourceDoc
- `FromChildren`: Array of strings containing the full path and filenames of the child documents dependent on the document specified for SourceDoc
- `ToChildren`: Array of strings containing the new full path and filenames for the child documents to which to move the documents specified for FromChildren
- `Option`: Move options as defined by [swMoveCopyOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveCopyOptions_e.html)

### Return Value

Success or error code as defined by [swMoveCopyError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveCopyError_e.html)

## VBA Syntax

See [SldWorks::MoveDocument](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~MoveDocument.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::IMoveDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IMoveDocument.html)
[ISldWorks::ICopyDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ICopyDocument.html)
[ISldWorks::CopyDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyDocument.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
