---
title: "GetAnnotations Method (ISwDMDimXpertPart)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertPart"
member: "GetAnnotations"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart~GetAnnotations.html"
---

# GetAnnotations Method (ISwDMDimXpertPart)

Gets all of the DimXpert annotations in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertPart
Dim value As System.Object

value = instance.GetAnnotations()
```

### C#

```csharp
System.object GetAnnotations()
```

### C++/CLI

```cpp
System.Object^ GetAnnotations();
```

### Return Value

Array of [ISwDMDimXpertAnnotation](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertAnnotation.html)s

## VBA Syntax

See [SwDMDimXpertPart::GetAnnotations](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertPart~GetAnnotations.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertPart Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart.html)
[ISwDMDimXpertPart Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart_members.html)
[ISwDMDimxpertPart::IGetAnnotations Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart~IGetAnnotations.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
