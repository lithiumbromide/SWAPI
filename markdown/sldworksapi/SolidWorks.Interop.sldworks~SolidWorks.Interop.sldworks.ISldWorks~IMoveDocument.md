---
title: "IMoveDocument Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IMoveDocument"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IMoveDocument.html"
---

# IMoveDocument Method (ISldWorks)

Moves a document and optionally updates references to it.

## Syntax

### Visual Basic (Declaration)

```vb
Function IMoveDocument( _
   ByVal SourceDoc As System.String, _
   ByVal DestDoc As System.String, _
   ByVal ChildCount As System.Integer, _
   ByRef FromChildren As System.String, _
   ByRef ToChildren As System.String, _
   ByVal Option As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim SourceDoc As System.String
Dim DestDoc As System.String
Dim ChildCount As System.Integer
Dim FromChildren As System.String
Dim ToChildren As System.String
Dim Option As System.Integer
Dim value As System.Integer

value = instance.IMoveDocument(SourceDoc, DestDoc, ChildCount, FromChildren, ToChildren, Option)
```

### C#

```csharp
System.int IMoveDocument(
   System.string SourceDoc,
   System.string DestDoc,
   System.int ChildCount,
   ref System.string FromChildren,
   ref System.string ToChildren,
   System.int Option
)
```

### C++/CLI

```cpp
System.int IMoveDocument(
   System.String^ SourceDoc,
   System.String^ DestDoc,
   System.int ChildCount,
   System.String^% FromChildren,
   System.String^% ToChildren,
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SourceDoc`: Full path and filename of the document to move
- `DestDoc`: Full path and filename of the new document to which to move the document specified for SourceDoc
- `ChildCount`: Number of child documents for SourceDoc
- `FromChildren`: Array of strings containing the full path and filenames of the child documents dependent on the document specified for SourceDoc
- `ToChildren`: Array of strings containing the new full path and filenames for the child documents to which to move the documents specified for FromChildren
- `Option`: Move options as defined by [swMoveCopyOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveCopyOptions_e.html)

### Return Value

Success or error code as defined by [swMoveCopyError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveCopyError_e.html)

## VBA Syntax

See [SldWorks::IMoveDocument](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IMoveDocument.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::MoveDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~MoveDocument.html)
[ISldWorks::ICopyDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ICopyDocument.html)
[ISldWorks::CopyDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyDocument.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
