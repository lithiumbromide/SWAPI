---
title: "ICopyDocument Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ICopyDocument"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ICopyDocument.html"
---

# ICopyDocument Method (ISldWorks)

Copies a document and optionally updates references to it.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICopyDocument( _
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

value = instance.ICopyDocument(SourceDoc, DestDoc, ChildCount, FromChildren, ToChildren, Option)
```

### C#

```csharp
System.int ICopyDocument(
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
System.int ICopyDocument(
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

- `SourceDoc`: Full path and filename of the document to copy
- `DestDoc`: Full path and filename of the document to which to copy SourceDoc
- `ChildCount`: Number of child documents for SourceDoc
- `FromChildren`: Array containing the full path and filenames of the child documents dependent on the document specified for SourceDoc
- `ToChildren`: Array of strings containing the new full path and filenames of the child documents to which to copy the child documents specified for FromChildren
- `Option`: Copy options as defined by [swMoveCopyOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveCopyOptions_e.html)

### Return Value

Success or error code as defined by [swMoveCopyError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveCopyError_e.html)

## VBA Syntax

See [SldWorks::ICopyDocument](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ICopyDocument.html).

## Examples

[Copy Document (C++)](Copy_Document_Example_CPlusPlus_COM.htm)

## Remarks

There can be no documents open when using this method.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::MoveDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~MoveDocument.html)
[IModelDocExtension::SaveAs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.html)
[ISldWorks::CopyDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyDocument.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
