---
title: "SetCustomProperty Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "SetCustomProperty"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SetCustomProperty.html"
---

# SetCustomProperty Method (ISwDMDocument)

Obsolete. Superseded by [ISwDMDocument29::SetCustomProperty2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument29~SetCustomProperty2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCustomProperty( _
   ByVal FieldName As System.String, _
   ByVal newValue As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim FieldName As System.String
Dim newValue As System.String

instance.SetCustomProperty(FieldName, newValue)
```

### C#

```csharp
void SetCustomProperty(
   System.string FieldName,
   System.string newValue
)
```

### C++/CLI

```cpp
void SetCustomProperty(
   System.String^ FieldName,
   System.String^ newValue
)
```

### Parameters

- `FieldName`: Name of custom property
- `newValue`: Value for custom property

## VBA Syntax

See [SwDMDocument::SetCustomProperty](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~SetCustomProperty.html).

## Remarks

Before calling this method, call [ISwDMDocument::GetCustomPropertyNames](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyNames.html) to populate FieldName.

If you call this method to set a linked custom property with an expression value, then you need to open and save the file in SOLIDWORKS before calling [ISwDMDocument::GetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.html), [ISwDMDocument17::GetCustomProperty2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2.html), [ISwDMDocument3::GetAllCustomPropertyNamesAndValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3~GetAllCustomPropertyNamesAndValues.html), or [ISwDMDocument5::GetCustomPropertyValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetCustomPropertyValues.html). SOLIDWORKS needs to process the linked custom property before your DocumentMgr application attempts to get its evaluated value.

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~AddCustomProperty.html)
[ISwDMDocument::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~DeleteCustomProperty.html)
[ISwDMDocument::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyCount.html)
[ISwDMConfiguration::SetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
