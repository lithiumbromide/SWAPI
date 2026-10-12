---
title: "GetBOMTableType Method (ISwDMTable2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable2"
member: "GetBOMTableType"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMTableType.html"
---

# GetBOMTableType Method (ISwDMTable2)

Gets the type of bill of materials (BOM) table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBOMTableType( _
   ByRef Error As SwDmTableError _
) As swDmBOMTableType
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable2
Dim Error As SwDmTableError
Dim value As swDmBOMTableType

value = instance.GetBOMTableType(Error)
```

### C#

```csharp
swDmBOMTableType GetBOMTableType(
   out SwDmTableError Error
)
```

### C++/CLI

```cpp
swDmBOMTableType GetBOMTableType(
   [Out] SwDmTableError Error
)
```

### Parameters

- `Error`: Error as defined by [SwDmTableError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableError.html)

### Return Value

Type of BOM table as defined in [swDmBOMTableType](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmBOMTableType.html)

## VBA Syntax

See [SwDMTable2::GetBOMTableType](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable2~GetBOMTableType.html).

## Remarks

This method only supports documents saved in SOLIDWORKS 2009 and later.

## See Also

[ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.html)
[ISwDMTable2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2_members.html)
[ISwDMTable2::GetBOMNumberIncrement Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMNumberIncrement.html)
[ISwDMTable2::GetBOMStartNumber Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMStartNumber.html)
[ISwDMConfiguration11::BOMPartNoSource Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~BOMPartNoSource.html)
[ISwDMConfiguration11::ShowChildComponentsInBOM Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~ShowChildComponentsInBOM.html)
[ISwDMComponent5::ExcludeFromBOM Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent5~ExcludeFromBOM.html)
[ISwDMTable2::GetFeatureName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetFeatureName.html)
[ISwDMTable2::ReferencedConfigurationNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~ReferencedConfigurationNames.html)
[ISwDMTable2::ReferencedDocumentName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~ReferencedDocumentName.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
