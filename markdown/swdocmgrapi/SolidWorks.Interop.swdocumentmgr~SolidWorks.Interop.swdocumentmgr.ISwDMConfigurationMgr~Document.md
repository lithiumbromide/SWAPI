---
title: "Document Property (ISwDMConfigurationMgr)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfigurationMgr"
member: "Document"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~Document.html"
---

# Document Property (ISwDMConfigurationMgr)

Gets the [ISwDMDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument.html) object for this document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Document As SwDMDocument
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfigurationMgr
Dim value As SwDMDocument

value = instance.Document
```

### C#

```csharp
SwDMDocument Document {get;}
```

### C++/CLI

```cpp
property SwDMDocument^ Document {
   SwDMDocument^ get();
}
```

### Property Value

Pointer to [ISwDMDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument.html) object

## VBA Syntax

See [SwDMConfigurationMgr::Document](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfigurationMgr~Document.html).

## See Also

[ISwDMConfigurationMgr Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr.html)
[ISwDMConfigurationMgr Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
