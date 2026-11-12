---
title: "IGetAnnotations Method (ISwDMDimXpertPart)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertPart"
member: "IGetAnnotations"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart~IGetAnnotations.html"
---

# IGetAnnotations Method (ISwDMDimXpertPart)

Gets all of the DimXpert annotations in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAnnotations( _
   ByVal Count As System.Integer _
) As SwDMDimXpertAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertPart
Dim Count As System.Integer
Dim value As SwDMDimXpertAnnotation

value = instance.IGetAnnotations(Count)
```

### C#

```csharp
SwDMDimXpertAnnotation IGetAnnotations(
   System.int Count
)
```

### C++/CLI

```cpp
SwDMDimXpertAnnotation^ IGetAnnotations(
   System.int Count
)
```

### Parameters

- `Count`: Number of annotations

### Return Value

in-process, unmanaged C++: Pointer to an array of [ISwDMDimXpertAnnotation](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertAnnotation.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Use [ISwDMDimXpertPart::GetAnnotationCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertPart~GetAnnotationCount.html) to populate the Count argument.

## See Also

[ISwDMDimXpertPart Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart.html)
[ISwDMDimXpertPart Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart_members.html)
[ISwDMDimXpertPart::GetAnnotations Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart~GetAnnotations.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
