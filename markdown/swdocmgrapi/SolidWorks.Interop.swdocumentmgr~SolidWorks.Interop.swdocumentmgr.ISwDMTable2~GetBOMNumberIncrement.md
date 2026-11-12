---
title: "GetBOMNumberIncrement Method (ISwDMTable2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable2"
member: "GetBOMNumberIncrement"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMNumberIncrement.html"
---

# GetBOMNumberIncrement Method (ISwDMTable2)

Gets the increment value by which the item numbers are increased in the bill of materials (BOM) table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBOMNumberIncrement( _
   ByRef Error As SwDmTableError _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable2
Dim Error As SwDmTableError
Dim value As System.Integer

value = instance.GetBOMNumberIncrement(Error)
```

### C#

```csharp
System.int GetBOMNumberIncrement(
   out SwDmTableError Error
)
```

### C++/CLI

```cpp
System.int GetBOMNumberIncrement(
   [Out] SwDmTableError Error
)
```

### Parameters

- `Error`: Error as defined by [SwDmTableError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableError.html)

### Return Value

Increment value by which the item numbers are increased in the bill of materials (BOM) table

## VBA Syntax

See [SwDMTable2::GetBOMNumberIncrement](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable2~GetBOMNumberIncrement.html).

## Remarks

This method only supports documents saved in SOLIDWORKS 2009 and later.

## See Also

[ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.html)
[ISwDMTable2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2_members.html)
[ISwDMTable2::GetBOMStartNumber Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMStartNumber.html)
[ISwDMTable2::GetBOMTableType Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetBOMTableType.html)
[ISwDMComponent5::ExcludeFromBOM Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent5~ExcludeFromBOM.html)
[ISwDMConfiguration11::BOMPartNoSource Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~BOMPartNoSource.html)
[ISwDMConfiguration11::ShowChildComponentsInBOM Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~ShowChildComponentsInBOM.html)
[ISwDMTable2::GetFeatureName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetFeatureName.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
