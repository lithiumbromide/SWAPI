---
title: "GetCustomPropertyValue Method (ISwDMCutListItem)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMCutListItem"
member: "GetCustomPropertyValue"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem~GetCustomPropertyValue.html"
---

# GetCustomPropertyValue Method (ISwDMCutListItem)

Obsolete. Superseded by [ISwDMCutListItem2::GetCustomPropertyValue2](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMCutListItem~GetCustomPropertyValue.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomPropertyValue( _
   ByVal FieldName As System.String, _
   ByRef type As SwDmCustomInfoType, _
   ByRef linkedTo As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMCutListItem
Dim FieldName As System.String
Dim type As SwDmCustomInfoType
Dim linkedTo As System.String
Dim value As System.String

value = instance.GetCustomPropertyValue(FieldName, type, linkedTo)
```

### C#

```csharp
System.string GetCustomPropertyValue(
   System.string FieldName,
   out SwDmCustomInfoType type,
   out System.string linkedTo
)
```

### C++/CLI

```cpp
System.String^ GetCustomPropertyValue(
   System.String^ FieldName,
   [Out] SwDmCustomInfoType type,
   [Out] System.String^ linkedTo
)
```

### Parameters

- `FieldName`:
- `type`:
- `linkedTo`:

## VBA Syntax

See [SwDMCutListItem::GetCustomPropertyValue](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMCutListItem~GetCustomPropertyValue.html).

## See Also

[ISwDMCutListItem Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem.html)
[ISwDMCutListItem Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem_members.html)
