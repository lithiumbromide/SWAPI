---
title: "Sheet Property (ISwDMTable5)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable5"
member: "Sheet"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5~Sheet.html"
---

# Sheet Property (ISwDMTable5)

Gets the drawing sheet for this table.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Sheet As SwDMSheet
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable5
Dim value As SwDMSheet

value = instance.Sheet
```

### C#

```csharp
SwDMSheet Sheet {get;}
```

### C++/CLI

```cpp
property SwDMSheet^ Sheet {
   SwDMSheet^ get();
}
```

### Property Value

[ISwDMSheet](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet.html)

## VBA Syntax

See [SwDMTable5::Sheet](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable5~Sheet.html).

## Examples

See the [ISwDMTable5](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5.html) examples.

## Remarks

This property works only with documents saved in SOLIDWORKS 2017 or later.

## See Also

[ISwDMTable5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5.html)
[ISwDMTable5 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5_members.html)

## Availability

SOLIDWORKS Document Manager API 2017 FCS
