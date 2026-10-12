---
title: "IsCustomPropertyEditable Method (ISwDMCutListItem3)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMCutListItem3"
member: "IsCustomPropertyEditable"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem3~IsCustomPropertyEditable.html"
---

# IsCustomPropertyEditable Method (ISwDMCutListItem3)

Gets whether the specified custom property is editable.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IsCustomPropertyEditable( _
   ByVal FieldName As System.String, _
   ByRef IsEditable As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMCutListItem3
Dim FieldName As System.String
Dim IsEditable As System.Boolean

instance.IsCustomPropertyEditable(FieldName, IsEditable)
```

### C#

```csharp
void IsCustomPropertyEditable(
   System.string FieldName,
   out System.bool IsEditable
)
```

### C++/CLI

```cpp
void IsCustomPropertyEditable(
   System.String^ FieldName,
   [Out] System.bool IsEditable
)
```

### Parameters

- `FieldName`: Name of the custom property
- `IsEditable`: True if editable, false if not

## VBA Syntax

See [SwDMCutListItem3::IsCustomPropertyEditable](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMCutListItem3~IsCustomPropertyEditable.html).

## Remarks

To populate FieldName, use [ISwDMCutListItem::GetCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem~GetCustomPropertyNames.html) to get the names of all of the custom properties.

## See Also

[ISwDMCutListItem3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem3.html)
[ISwDMCutListItem3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem3_members.html)

## Availability

SOLIDWORKS Document Manager API 2018 SP0
