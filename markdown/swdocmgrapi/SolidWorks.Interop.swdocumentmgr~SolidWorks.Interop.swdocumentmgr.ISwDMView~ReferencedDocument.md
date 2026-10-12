---
title: "ReferencedDocument Property (ISwDMView)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMView"
member: "ReferencedDocument"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView~ReferencedDocument.html"
---

# ReferencedDocument Property (ISwDMView)

Gets or sets the name of the document for this drawing view.

**NOTE:** **This property is a get-only property. Set is not implemented.**

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferencedDocument As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMView
Dim value As System.String

instance.ReferencedDocument = value

value = instance.ReferencedDocument
```

### C#

```csharp
System.string ReferencedDocument {get; set;}
```

### C++/CLI

```cpp
property System.String^ ReferencedDocument {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of document

## VBA Syntax

See [SwDMView::ReferencedDocument](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMView~ReferencedDocument.html).

## See Also

[ISwDMView Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView.html)
[ISwDMView Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView_members.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
