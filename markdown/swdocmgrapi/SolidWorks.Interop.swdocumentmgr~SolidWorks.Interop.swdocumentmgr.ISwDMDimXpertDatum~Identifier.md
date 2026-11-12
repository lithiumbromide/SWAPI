---
title: "Identifier Property (ISwDMDimXpertDatum)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertDatum"
member: "Identifier"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDatum~Identifier.html"
---

# Identifier Property (ISwDMDimXpertDatum)

Gets the label for this DimXpert datum.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Identifier As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertDatum
Dim value As System.String

value = instance.Identifier
```

### C#

```csharp
System.string Identifier {get;}
```

### C++/CLI

```cpp
property System.String^ Identifier {
   System.String^ get();
}
```

### Property Value

Label for the datum

## VBA Syntax

See [SwDMDimXpertDatum::Identifier](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertDatum~Identifier.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertDatum Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDatum.html)
[ISwDMDimXpertDatum Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDatum_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
