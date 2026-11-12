---
title: "CustomPropertyView Property (ISwDMSheet4)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMSheet4"
member: "CustomPropertyView"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet4~CustomPropertyView.html"
---

# CustomPropertyView Property (ISwDMSheet4)

Gets the drawing view on which this sheet's custom properties reside.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CustomPropertyView As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMSheet4
Dim value As System.Object

value = instance.CustomPropertyView
```

### C#

```csharp
System.object CustomPropertyView {get;}
```

### C++/CLI

```cpp
property System.Object^ CustomPropertyView {
   System.Object^ get();
}
```

### Property Value

[ISwDMView](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView.html); null if the sheet has no views

## VBA Syntax

See [SwDMSheet4::CustomPropertyView](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMSheet4~CustomPropertyView.html).

## Examples

See the [ISwDMSheet4](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet4.html) examples.

## Remarks

This property works only with documents saved in SOLIDWORKS 2017 or later.

## See Also

[ISwDMSheet4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet4.html)
[ISwDMSheet4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet4_members.html)

## Availability

SOLIDWORKS Document Manager API 2017 FCS
