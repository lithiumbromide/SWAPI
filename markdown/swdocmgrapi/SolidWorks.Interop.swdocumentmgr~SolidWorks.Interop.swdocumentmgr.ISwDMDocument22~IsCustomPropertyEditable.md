---
title: "IsCustomPropertyEditable Method (ISwDMDocument22)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument22"
member: "IsCustomPropertyEditable"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22~IsCustomPropertyEditable.html"
---

# IsCustomPropertyEditable Method (ISwDMDocument22)

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
Dim instance As ISwDMDocument22
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

- `FieldName`: Name of the custom property in this document
- `IsEditable`: True if editable, false if not

## VBA Syntax

See [SwDMDocument22::IsCustomPropertyEditable](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument22~IsCustomPropertyEditable.html).

## Examples

See the [ISwDMDocument22](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22.html) examples.

## Remarks

To populate FieldName, use [ISwDMDocument::GetCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyNames.html) to get the names of all of the custom properties in this document.

## See Also

[ISwDMDocument22 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22.html)
[ISwDMDocument22 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22_members.html)

## Availability

SOLIDWORKS Document Manager API 2018 SP0
