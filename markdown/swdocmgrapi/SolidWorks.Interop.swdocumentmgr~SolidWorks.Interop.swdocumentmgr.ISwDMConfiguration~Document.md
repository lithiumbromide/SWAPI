---
title: "Document Property (ISwDMConfiguration)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration"
member: "Document"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~Document.html"
---

# Document Property (ISwDMConfiguration)

Gets the document for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Document As SwDMDocument
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration
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

Pointer to the [ISwDMDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument.html) object

## VBA Syntax

See [SwDMConfiguration::Document](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration~Document.html).

## See Also

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.html)
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
