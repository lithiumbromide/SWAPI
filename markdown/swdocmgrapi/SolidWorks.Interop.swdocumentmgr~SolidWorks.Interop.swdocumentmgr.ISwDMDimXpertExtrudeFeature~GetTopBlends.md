---
title: "GetTopBlends Method (ISwDMDimXpertExtrudeFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertExtrudeFeature"
member: "GetTopBlends"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetTopBlends.html"
---

# GetTopBlends Method (ISwDMDimXpertExtrudeFeature)

Gets the DimXpert blend feature at the top of this DimXpert extrude.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTopBlends() As SwDMDimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertExtrudeFeature
Dim value As SwDMDimXpertFeature

value = instance.GetTopBlends()
```

### C#

```csharp
SwDMDimXpertFeature GetTopBlends()
```

### C++/CLI

```cpp
SwDMDimXpertFeature^ GetTopBlends();
```

### Return Value

[ISwDMDimXpertFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)

## VBA Syntax

See [SwDMDimXpertExtrudeFeature::GetTopBlends](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertExtrudeFeature~GetTopBlends.html).

## Examples

See the examples on the interface page.

## Remarks

The top blend is typically an [ISwDMDimXpertFilletFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFilletFeature.html).

## See Also

[ISwDMDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature.html)
[ISwDMDimXpertExtrudeFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
