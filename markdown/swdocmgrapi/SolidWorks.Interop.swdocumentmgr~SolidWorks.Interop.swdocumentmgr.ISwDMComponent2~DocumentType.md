---
title: "DocumentType Property (ISwDMComponent2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent2"
member: "DocumentType"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent2~DocumentType.html"
---

# DocumentType Property (ISwDMComponent2)

Gets the component's document type.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DocumentType As SwDmDocumentType
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent2
Dim value As SwDmDocumentType

value = instance.DocumentType
```

### C#

```csharp
SwDmDocumentType DocumentType {get;}
```

### C++/CLI

```cpp
property SwDmDocumentType DocumentType {
   SwDmDocumentType get();
}
```

### Property Value

Component's document type as defined in [swDMDocumentType](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmDocumentType.html)

## VBA Syntax

See [SwDMComponent2::DocumentType](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent2~DocumentType.html).

## Remarks

This property can distinguish between components and sub-assemblies whose names are the same.

## See Also

[ISwDMComponent2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent2.html)
[ISwDMComponent2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent2_members.html)

## Availability

SOLIDWORKS Document Manager API 2005 FCS
