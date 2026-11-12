---
title: "BOMPartNoSource Property (ISwDMConfiguration11)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration11"
member: "BOMPartNoSource"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~BOMPartNoSource.html"
---

# BOMPartNoSource Property (ISwDMConfiguration11)

Gets or sets the source of the part number used in the bill of materials (BOM) for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property BOMPartNoSource As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration11
Dim value As System.Integer

instance.BOMPartNoSource = value

value = instance.BOMPartNoSource
```

### C#

```csharp
System.int BOMPartNoSource {get; set;}
```

### C++/CLI

```cpp
property System.int BOMPartNoSource {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Source of part number used in the BOM as defined in [swDmBOMPartNumberSource](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmBOMPartNumberSource.html)

## VBA Syntax

See [SwDMConfiguration11::BOMPartNoSource](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration11~BOMPartNoSource.html).

## Remarks

If you set this property to anything other than swDmBOMPartNumber_UserSpecified, then [ISwDMConfiguration7::AlternateName2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~AlternateName2.html) is set to an empty string.

## See Also

[ISwDMConfiguration11 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11.html)
[ISwDMConfiguration11 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11_members.html)
[ISwDMConfiguration11::ShowChildComponentsInBOM Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~ShowChildComponentsInBOM.html)
[ISwDMTable2::GetBOMNumberIncrement Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMNumberIncrement.html)
[ISwDMTable2::GetBOMTableType Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMTableType.html)
[ISwDMTable2::GetBOMTableType Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMTableType.html)
[ISwDMTable2::GetFeatureName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetFeatureName.html)
[ISwDMTable2::ReferencedConfigurationNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~ReferencedConfigurationNames.html)
[ISwDMTable2::ReferencedDocumentName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~ReferencedDocumentName.html)
[ISwDMComponent5::ExcludeFromBOM Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent5~ExcludeFromBOM.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
