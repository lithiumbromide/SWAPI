---
title: "GetBottomBlends Method (ISwDMDimXpertExtrudeFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertExtrudeFeature"
member: "GetBottomBlends"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetBottomBlends.html"
---

# GetBottomBlends Method (ISwDMDimXpertExtrudeFeature)

Gets the DimXpert blend feature at the bottom of this DimXpert extrude.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBottomBlends() As SwDMDimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertExtrudeFeature
Dim value As SwDMDimXpertFeature

value = instance.GetBottomBlends()
```

### C#

```csharp
SwDMDimXpertFeature GetBottomBlends()
```

### C++/CLI

```cpp
SwDMDimXpertFeature^ GetBottomBlends();
```

### Return Value

[ISwDMDimXpertFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)

## VBA Syntax

See [SwDMDimXpertExtrudeFeature::GetBottomBlends](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertExtrudeFeature~GetBottomBlends.html).

## Examples

See the examples on the interface page.

## Remarks

The bottom blend is typically an [ISwDMDimXpertFilletFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFilletFeature.html).

## See Also

[ISwDMDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature.html)
[ISwDMDimXpertExtrudeFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
