---
title: "GetCustomPropertyValue2 Method (ISwDMCutListItem2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMCutListItem2"
member: "GetCustomPropertyValue2"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~GetCustomPropertyValue2.html"
---

# GetCustomPropertyValue2 Method (ISwDMCutListItem2)

Gets the evaluated value of this custom property for this cut-list item.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomPropertyValue2( _
   ByVal FieldName As System.String, _
   ByRef type As SwDmCustomInfoType, _
   ByRef linkedTo As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMCutListItem2
Dim FieldName As System.String
Dim type As SwDmCustomInfoType
Dim linkedTo As System.String
Dim value As System.String

value = instance.GetCustomPropertyValue2(FieldName, type, linkedTo)
```

### C#

```csharp
System.string GetCustomPropertyValue2(
   System.string FieldName,
   out SwDmCustomInfoType type,
   out System.string linkedTo
)
```

### C++/CLI

```cpp
System.String^ GetCustomPropertyValue2(
   System.String^ FieldName,
   [Out] SwDmCustomInfoType type,
   [Out] System.String^ linkedTo
)
```

### Parameters

- `FieldName`: Custom property name (see **Remarks**)
- `type`: Property type as defined by [swDMCustomInfoType](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmCustomInfoType.html)
- `linkedTo`: Link-to value or text expresssion

### Return Value

Evaluated value

## VBA Syntax

See [SwDMCutListItem2::GetCustomPropertyValue2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMCutListItem2~GetCustomPropertyValue2.html).

## Examples

[Get, Add, Change, and Delete Cut-List Custom Properties (C#)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm)
[Get, Add, Change, and Delete Cut-List Custom Properties (VB.NET)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm)

## Remarks

This method only supports model documents saved in SOLIDWORKS 2009 or later.

To populate FieldName, use [ISwDMCutListItem::GetCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem~GetCustomPropertyNames.html) to get the names of all of the custom properties.

If you called [ISwDMCutListItem2::SetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~SetCustomProperty.html) to set a linked custom property, then you must open and save the file in SOLIDWORKS before calling this method. SOLIDWORKS must process the linked custom property before your DocumentMgr application can retrieve its evaluated value.

## See Also

[ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.html)
[ISwDMCutListItem2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2_members.html)
[ISwDMCutListItem2::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~AddCustomProperty.html)
[ISwDMCutListItem2::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~DeleteCustomProperty.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
