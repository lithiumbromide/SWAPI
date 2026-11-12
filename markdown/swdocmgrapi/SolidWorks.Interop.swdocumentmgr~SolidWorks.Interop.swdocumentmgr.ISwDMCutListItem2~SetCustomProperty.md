---
title: "SetCustomProperty Method (ISwDMCutListItem2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMCutListItem2"
member: "SetCustomProperty"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~SetCustomProperty.html"
---

# SetCustomProperty Method (ISwDMCutListItem2)

Sets a custom property for this cut-list item.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCustomProperty( _
   ByVal FieldName As System.String, _
   ByVal newValue As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMCutListItem2
Dim FieldName As System.String
Dim newValue As System.String
Dim value As System.Boolean

value = instance.SetCustomProperty(FieldName, newValue)
```

### C#

```csharp
System.bool SetCustomProperty(
   System.string FieldName,
   System.string newValue
)
```

### C++/CLI

```cpp
System.bool SetCustomProperty(
   System.String^ FieldName,
   System.String^ newValue
)
```

### Parameters

- `FieldName`: Property name
- `newValue`: Property link-to value or text expression

### Return Value

True if the custom property is updated, false if not

## VBA Syntax

See [SwDMCutListItem2::SetCustomProperty](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMCutListItem2~SetCustomProperty.html).

## Examples

[Get, Add, Change, and Delete Cut-List Custom Properties (C#)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm)
[Get, Add, Change, and Delete Cut-List Custom Properties (VB.NET)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm)

## Remarks

This method only supports model documents saved in SOLIDWORKS 2009 and later.

Before calling this method, call [ISwDMCutListItem::GetCustomPropertyNames](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMCutListItem~GetCustomPropertyNames.html) to get all of the custom properties for this cut-list item.

If you call this method to set a linked custom property with an expression value, then you need to open and save the file in SOLIDWORKS before calling [ISwDMCutListItem2::GetCustomPropertyValue2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~GetCustomPropertyValue2.html). SOLIDWORKS needs to process the linked custom property before your DocumentMgr application attempts to get its evaluated value.

## See Also

[ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.html)
[ISwDMCutListItem2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2_members.html)
[ISwDMCutListItem2::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~AddCustomProperty.html)
[ISwDMCutListItem2::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~DeleteCustomProperty.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
