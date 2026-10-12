---
title: "DimXpertPart Property (ISwDMConfiguration12)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration12"
member: "DimXpertPart"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~DimXpertPart.html"
---

# DimXpertPart Property (ISwDMConfiguration12)

Gets the DimXpert part associated with this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DimXpertPart As SwDMDimXpertPart
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration12
Dim value As SwDMDimXpertPart

value = instance.DimXpertPart
```

### C#

```csharp
SwDMDimXpertPart DimXpertPart {get;}
```

### C++/CLI

```cpp
property SwDMDimXpertPart^ DimXpertPart {
   SwDMDimXpertPart^ get();
}
```

### Property Value

[ISwDMDimXpertPart](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertPart.html)

## VBA Syntax

See [SwDMConfiguration12::DimXpertPart](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration12~DimXpertPart.html).

## Examples

[Get DimXpert Block Tolerance (VB.NET)](Get_DimXpert_Block_Tolerance_Example_VBNET.htm)
[Get DimXpert Block Tolerance (C#)](Get_DimXpert_Block_Tolerance_Example_CSharp.htm)

## See Also

[ISwDMConfiguration12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12.html)
[ISwDMConfiguration12 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
