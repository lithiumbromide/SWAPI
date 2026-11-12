---
title: "SetCustomProperty Method (ISwDMConfiguration)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration"
member: "SetCustomProperty"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty.html"
---

# SetCustomProperty Method (ISwDMConfiguration)

Obsolete. Superseded by [ISwDMConfiguration18::SetCustomProperty2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration18~SetCustomProperty2.html).

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
Dim instance As ISwDMConfiguration
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

- `FieldName`: Custom property to set
- `newValue`: Value for custom property

## VBA Syntax

See [SwDMConfiguration::SetCustomProperty](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration~SetCustomProperty.html).

## Remarks

Before calling this method, call [ISwDMConfiguration::GetCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.html) to populate FieldName.

If you call this method to set a linked custom property with an expression value, then you need to open and save the file in SOLIDWORKS before calling [ISwDMConfiguration::GetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomProperty.html), [ISwDMConfiguration14::GetCustomProperty2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14~GetCustomProperty2.html), [ISwDMConfiguration4::GetAllCustomPropertyNamesAndValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4~GetAllCustomPropertyNamesAndValues.html), or [ISwDMConfiguration5::GetCustomPropertyValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5~GetCustomPropertyValues.html). SOLIDWORKS needs to process the linked custom property before your DocumentMgr application attempts to get its evaluated value.

## See Also

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.html)
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.html)
[ISwDMConfiguration::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~AddCustomProperty.html)
[ISwDMConfiguration::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~DeleteCustomProperty.html)
[ISwDMConfiguration::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyCount.html)
[ISwDMConfiguration::GetCustomPropertyNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.html)
[ISwDMDocument::SetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SetCustomProperty.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
