---
title: "GetBOMStartNumber Method (ISwDMTable2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable2"
member: "GetBOMStartNumber"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMStartNumber.html"
---

# GetBOMStartNumber Method (ISwDMTable2)

Gets the starting item number for this bill of materials (BOM) table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBOMStartNumber( _
   ByRef Error As SwDmTableError _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable2
Dim Error As SwDmTableError
Dim value As System.Integer

value = instance.GetBOMStartNumber(Error)
```

### C#

```csharp
System.int GetBOMStartNumber(
   out SwDmTableError Error
)
```

### C++/CLI

```cpp
System.int GetBOMStartNumber(
   [Out] SwDmTableError Error
)
```

### Parameters

- `Error`: Error as defined by [SwDmTableError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableError.html)

### Return Value

Starting item number for this bill of materials (BOM) table

## VBA Syntax

See [SwDMTable2::GetBOMStartNumber](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable2~GetBOMStartNumber.html).

## Remarks

This method only supports documents saved in SOLIDWORKS 2009 and later.

## See Also

[ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.html)
[ISwDMTable2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2_members.html)
[ISwDMTable2::GetBOMNumberIncrement Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMNumberIncrement.html)
[ISwDMTable2::GetBOMTableType Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMTableType.html)
[ISwDMConfiguration11::BOMPartNoSource Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~BOMPartNoSource.html)
[ISwDMConfiguration11::ShowChildComponentsInBOM Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~ShowChildComponentsInBOM.html)
[ISwDMComponent5::ExcludeFromBOM Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent5~ExcludeFromBOM.html)
[ISwDMTable2::GetFeatureName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetFeatureName.html)
[ISwDMTable2::ReferencedConfigurationNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~ReferencedConfigurationNames.html)
[ISwDMTable2::ReferencedDocumentName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~ReferencedDocumentName.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
