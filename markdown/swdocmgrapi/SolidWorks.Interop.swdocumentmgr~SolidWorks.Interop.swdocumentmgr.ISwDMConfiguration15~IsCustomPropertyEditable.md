---
title: "IsCustomPropertyEditable Method (ISwDMConfiguration15)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration15"
member: "IsCustomPropertyEditable"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration15~IsCustomPropertyEditable.html"
---

# IsCustomPropertyEditable Method (ISwDMConfiguration15)

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
Dim instance As ISwDMConfiguration15
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

- `FieldName`: Name of the custom property (see **Remarks**)
- `IsEditable`: True if editable, false if not

## VBA Syntax

See [SwDMConfiguration15::IsCustomPropertyEditable](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration15~IsCustomPropertyEditable.html).

## Remarks

To populate FieldName, use [ISwDMConfiguration::GetCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.html) to get the names of all of the custom properties.

## See Also

[ISwDMConfiguration15 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration15.html)
[ISwDMConfiguration15 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration15_members.html)
[ISwDMConfiguration14::GetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14~GetCustomProperty2.html)
[ISwDMConfiguration4::GetAllCustomPropertyNamesAndValues Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4~GetAllCustomPropertyNamesAndValues.html)

## Availability

SOLIDWORKS Document Manager API 2018 SP0
