---
title: "CopyDocument Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "CopyDocument"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyDocument.html"
---

# CopyDocument Method (ISldWorks)

Copies a document and optionally updates references to it.

## Syntax

### Visual Basic (Declaration)

```vb
Function CopyDocument( _
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

value = instance.CopyDocument(SourceDoc, DestDoc, FromChildren, ToChildren, Option)
```

### C#

```csharp
System.int CopyDocument(
   System.string SourceDoc,
   System.string DestDoc,
   System.object FromChildren,
   System.object ToChildren,
   System.int Option
)
```

### C++/CLI

```cpp
System.int CopyDocument(
   System.String^ SourceDoc,
   System.String^ DestDoc,
   System.Object^ FromChildren,
   System.Object^ ToChildren,
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SourceDoc`: Full path and filename of the document to copy
- `DestDoc`: Full path and filename of the document to which to copy SourceDoc
- `FromChildren`: Array containing the full path and filenames of the child documents dependent on the document specified for SourceDoc
- `ToChildren`: Array of strings containing the new full path and filenames of the child documents to which to copy the child documents specified for FromChildren
- `Option`: Copy options as defined by [swMoveCopyOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveCopyOptions_e.html)

### Return Value

Success or error code as defined by [swMoveCopyError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveCopyError_e.html)

## VBA Syntax

See [SldWorks::CopyDocument](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~CopyDocument.html).

## Examples

[Copy Document (VBA)](Copy_Document_Example_VB.htm)
[Copy Document and Its Dependencies (VBA)](Copy_Document_and_Its_Dependencies_Example_VB.htm)
[Copy Document and Its Dependencies (VB.NET)](Copy_Document_and_Its_Dependencies_Example_VBNET.htm)
[Copy Document and Its Dependencies (C#)](Copy_Document_and_Its_Dependencies_Example_CSharp.htm)

## Remarks

There can be no documents open when using this method.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::MoveDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~MoveDocument.html)
[ISldWorks::ICopyDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ICopyDocument.html)
[IModelDocExtension::SaveAs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
