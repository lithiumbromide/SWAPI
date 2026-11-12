---
title: "Sheet Property (ISwDMView)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMView"
member: "Sheet"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView~Sheet.html"
---

# Sheet Property (ISwDMView)

Gets or sets the sheet for this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Property Sheet As SwDMSheet
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMView
Dim value As SwDMSheet

instance.Sheet = value

value = instance.Sheet
```

### C#

```csharp
SwDMSheet Sheet {get; set;}
```

### C++/CLI

```cpp
property SwDMSheet^ Sheet {
   SwDMSheet^ get();
   void set (    SwDMSheet^ value);
}
```

### Property Value

[Sheet](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSheet.html)

## VBA Syntax

See [SwDMView::Sheet](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMView~Sheet.html).

## See Also

[ISwDMView Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView.html)
[ISwDMView Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView_members.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
