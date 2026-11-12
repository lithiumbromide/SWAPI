---
title: "ReferencedDocumentName Method (ISwDMTable2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable2"
member: "ReferencedDocumentName"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~ReferencedDocumentName.html"
---

# ReferencedDocumentName Method (ISwDMTable2)

Gets the document name used by this bill of materials (BOM) table.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReferencedDocumentName( _
   ByRef Error As SwDmTableError _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable2
Dim Error As SwDmTableError
Dim value As System.String

value = instance.ReferencedDocumentName(Error)
```

### C#

```csharp
System.string ReferencedDocumentName(
   out SwDmTableError Error
)
```

### C++/CLI

```cpp
System.String^ ReferencedDocumentName(
   [Out] SwDmTableError Error
)
```

### Parameters

- `Error`: Error as defined by [SwDmTableError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableError.html)

### Return Value

Document name

## VBA Syntax

See [SwDMTable2::ReferencedDocumentName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable2~ReferencedDocumentName.html).

## Remarks

This method only supports documents saved in SOLIDWORKS 2009 and later.

## See Also

[ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.html)
[ISwDMTable2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2_members.html)
[ISwDMTable2::ReferencedConfigurationNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~ReferencedConfigurationNames.html)
[ISwDMTable2::GetFeatureName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetFeatureName.html)
[ISwDMTable2::GetBOMTableType Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMTableType.html)
[ISwDMTable2::GetBOMStartNumber Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMStartNumber.html)
[ISwDMTable2::GetBOMNumberIncrement Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMNumberIncrement.html)
[ISwDMConfiguration11::ShowChildComponentsInBOM Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~ShowChildComponentsInBOM.html)
[ISwDMConfiguration11::BOMPartNoSource Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~BOMPartNoSource.html)
[ISwDMComponent5::ExcludeFromBOM Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent5~ExcludeFromBOM.html)

## Availability

SOLIDWORKS Document Manager 2009 SP0
