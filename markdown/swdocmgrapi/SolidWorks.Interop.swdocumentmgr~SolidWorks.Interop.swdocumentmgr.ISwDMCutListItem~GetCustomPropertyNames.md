---
title: "GetCustomPropertyNames Method (ISwDMCutListItem)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMCutListItem"
member: "GetCustomPropertyNames"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem~GetCustomPropertyNames.html"
---

# GetCustomPropertyNames Method (ISwDMCutListItem)

Gets the names of custom property names for this cut-list item.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomPropertyNames() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMCutListItem
Dim value As System.Object

value = instance.GetCustomPropertyNames()
```

### C#

```csharp
System.object GetCustomPropertyNames()
```

### C++/CLI

```cpp
System.Object^ GetCustomPropertyNames();
```

### Return Value

Array of custom property names

## VBA Syntax

See [SwDMCutListItem::GetCustomPropertyNames](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMCutListItem~GetCustomPropertyNames.html).

## Examples

[Get, Add, Change, and Delete Cut-List Custom Properties (C#)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm)
[Get, Add, Change, and Delete Cut-List Custom Properties (VB.NET)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm)

## See Also

[ISwDMCutListItem Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem.html)
[ISwDMCutListItem Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem_members.html)
[ISwDMCutListItem2::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~DeleteCustomProperty.html)
[ISwDMCutListItem2::SetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~SetCustomProperty.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
