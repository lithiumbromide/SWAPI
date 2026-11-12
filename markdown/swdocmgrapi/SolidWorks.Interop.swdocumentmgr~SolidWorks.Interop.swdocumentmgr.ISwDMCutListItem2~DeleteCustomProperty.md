---
title: "DeleteCustomProperty Method (ISwDMCutListItem2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMCutListItem2"
member: "DeleteCustomProperty"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~DeleteCustomProperty.html"
---

# DeleteCustomProperty Method (ISwDMCutListItem2)

Deletes the specified custom property from this cut-list item.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteCustomProperty( _
   ByVal FieldName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMCutListItem2
Dim FieldName As System.String
Dim value As System.Boolean

value = instance.DeleteCustomProperty(FieldName)
```

### C#

```csharp
System.bool DeleteCustomProperty(
   System.string FieldName
)
```

### C++/CLI

```cpp
System.bool DeleteCustomProperty(
   System.String^ FieldName
)
```

### Parameters

- `FieldName`: Custom property to delete from the cut-list item

### Return Value

True if the custom property is deleted, false if not

## VBA Syntax

See [SwDMCutListItem2::DeleteCustomProperty](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMCutListItem2~DeleteCustomProperty.html).

## Examples

[Get, Add, Change, and Delete Cut-List Custom Properties (C#)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm)
[Get, Add, Change, and Delete Cut-List Custom Properties (VB.NET)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm)

## Remarks

This method only supports model documents saved in SOLIDWORKS 2009 or later.

Before calling this method, call [ISwDMCutListItem::GetCustomPropertyNames](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMCutListItem~GetCustomPropertyNames.html).

## See Also

[ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.html)
[ISwDMCutListItem2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2_members.html)
[ISwDMCutListItem2::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~AddCustomProperty.html)
[ISwDMCutListItem2::GetCustomPropertyValue2 Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~GetCustomPropertyValue2.html)
[ISwDMCutListItem2::SetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~SetCustomProperty.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
