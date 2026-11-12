---
title: "Quantity Property (ISwDMCutListItem)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMCutListItem"
member: "Quantity"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem~Quantity.html"
---

# Quantity Property (ISwDMCutListItem)

Gets the number of this cut-list item.

## Syntax

### Visual Basic (Declaration)

```vb
Property Quantity As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMCutListItem
Dim value As System.Integer

instance.Quantity = value

value = instance.Quantity
```

### C#

```csharp
System.int Quantity {get; set;}
```

### C++/CLI

```cpp
property System.int Quantity {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of this cut-list item

## VBA Syntax

See [SwDMCutListItem::Quantity](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMCutListItem~Quantity.html).

## Examples

[Get, Add, Change, and Delete Cut-List Custom Properties (C#)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm)
[Get, Add, Change, and Delete Cut-List Custom Properties (VB.NET)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm)

## See Also

[ISwDMCutListItem Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem.html)
[ISwDMCutListItem Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem_members.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
