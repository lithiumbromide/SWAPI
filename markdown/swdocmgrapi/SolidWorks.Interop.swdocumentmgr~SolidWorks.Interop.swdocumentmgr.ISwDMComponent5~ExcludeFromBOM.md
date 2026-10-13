---
title: "ExcludeFromBOM Property (ISwDMComponent5)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent5"
member: "ExcludeFromBOM"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent5~ExcludeFromBOM.html"
---

# ExcludeFromBOM Property (ISwDMComponent5)

Gets whether this component is excluded from the bill of materials (BOM).

## Syntax

### Visual Basic (Declaration)

```vb
Property ExcludeFromBOM As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent5
Dim value As System.Integer

instance.ExcludeFromBOM = value

value = instance.ExcludeFromBOM
```

### C#

```csharp
System.int ExcludeFromBOM {get; set;}
```

### C++/CLI

```cpp
property System.int ExcludeFromBOM {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Exclude or include this component from the BOM as defined in [swDmExcludeFromBOMResults](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmExcludeFromBOMResult.html)

## VBA Syntax

See [SwDMComponent5::ExcludeFromBOM](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent5~ExcludeFromBOM.html).

## Examples

[Get Whether Component Is Envelope And Excluded From BOM (VB.NET)](Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_VBNET.htm)
[Get Whether Component Is Envelope And Excluded From BOM (C#)](Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_CSharp.htm)

## Remarks

This method only supports documents saved in SOLIDWORKS 2009 SP0 and later.

## See Also

[ISwDMComponent5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent5.html)
[ISwDMComponent5 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent5_members.html)
[ISwDMConfiguration11::ShowChildComponentsInBOM Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~ShowChildComponentsInBOM.html)
[ISwDMConfiguration11::BOMPartNoSource Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~BOMPartNoSource.html)
[ISwDMTable2::GetBOMNumberIncrement Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMNumberIncrement.html)
[ISwDMTable2::GetBOMStartNumber Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMStartNumber.html)
[ISwDMTable2::GetBOMTableType Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMTableType.html)
[ISwDMTable2::GetFeatureName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetFeatureName.html)
[ISwDMTable2::ReferencedConfigurationNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~ReferencedConfigurationNames.html)
[ISwDMTable2::ReferencedDocumentName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~ReferencedDocumentName.html)

## Availability

SOLIDWORKS Document Manager API 2008 SP2
