---
title: "Name Property (ISwDMCutListItem)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMCutListItem"
member: "Name"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem~Name.html"
---

# Name Property (ISwDMCutListItem)

Gets the name of this cut-list item.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMCutListItem
Dim value As System.String

instance.Name = value

value = instance.Name
```

### C#

```csharp
System.string Name {get; set;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of cut-list item

## VBA Syntax

See [SwDMCutListItem::Name](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMCutListItem~Name.html).

## Examples

[Get, Add, Change, and Delete Cut-List Custom Properties (C#)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm)
[Get, Add, Change, and Delete Cut-List Custom Properties (VB.NET)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm)

## See Also

[ISwDMCutListItem Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem.html)
[ISwDMCutListItem Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem_members.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
