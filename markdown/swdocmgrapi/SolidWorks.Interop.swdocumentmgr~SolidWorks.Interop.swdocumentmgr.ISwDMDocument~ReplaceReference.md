---
title: "ReplaceReference Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "ReplaceReference"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.html"
---

# ReplaceReference Method (ISwDMDocument)

Changes all instances of the specified original reference to the specified replacement reference in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReplaceReference( _
   ByVal OriginalReference As System.String, _
   ByVal ReplacementReference As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim OriginalReference As System.String
Dim ReplacementReference As System.String

instance.ReplaceReference(OriginalReference, ReplacementReference)
```

### C#

```csharp
void ReplaceReference(
   System.string OriginalReference,
   System.string ReplacementReference
)
```

### C++/CLI

```cpp
void ReplaceReference(
   System.String^ OriginalReference,
   System.String^ ReplacementReference
)
```

### Parameters

- `OriginalReference`: Name of original reference to replace
- `ReplacementReference`: Name of reference with which to replace OriginalReference

## VBA Syntax

See [SwDMDocument::ReplaceReference](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~ReplaceReference.html).

## Remarks

Before calling this method, you must call [ISwDMDocument13::GetAllExternalReferences4](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument13~GetAllExternalReferences4.html).

ISwDMDocument::ReplaceReference expects the fully qualified path names, exactly as those returned by ISwDMDocument13::GetAllExternalReferences4.

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument8::GetChangedReferences Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetChangedReferences.html)
**ISwDMDocument30::ClearChangedReferences Method ()**

## Availability

SOLIDWORKS Document Manager API 2004 FCS
