---
title: "ReferencedConfigurationNames Method (ISwDMTable2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable2"
member: "ReferencedConfigurationNames"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~ReferencedConfigurationNames.html"
---

# ReferencedConfigurationNames Method (ISwDMTable2)

Gets the configuration names used by the bill of materials (BOM) table.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReferencedConfigurationNames( _
   ByRef Error As SwDmTableError _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable2
Dim Error As SwDmTableError
Dim value As System.Object

value = instance.ReferencedConfigurationNames(Error)
```

### C#

```csharp
System.object ReferencedConfigurationNames(
   out SwDmTableError Error
)
```

### C++/CLI

```cpp
System.Object^ ReferencedConfigurationNames(
   [Out] SwDmTableError Error
)
```

### Parameters

- `Error`: Error as defined by [swDmTableError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableError.html)

### Return Value

Array of configuration names

## VBA Syntax

See [SwDMTable2::ReferencedConfigurationNames](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable2~ReferencedConfigurationNames.html).

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
[ISwDMConfiguration11::BOMPartNoSource Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~BOMPartNoSource.html)
[ISwDMConfiguration11::ShowChildComponentsInBOM Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~ShowChildComponentsInBOM.html)
[ISwDMComoponent5::ExcludeFromBOM Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent5~ExcludeFromBOM.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
