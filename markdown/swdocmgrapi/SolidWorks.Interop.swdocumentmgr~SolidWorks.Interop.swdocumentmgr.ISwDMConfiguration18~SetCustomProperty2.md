---
title: "SetCustomProperty2 Method (ISwDMConfiguration18)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration18"
member: "SetCustomProperty2"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration18~SetCustomProperty2.html"
---

# SetCustomProperty2 Method (ISwDMConfiguration18)

Sets the specified custom property for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCustomProperty2( _
   ByVal FieldName As System.String, _
   ByVal newValue As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration18
Dim FieldName As System.String
Dim newValue As System.String
Dim value As System.Boolean

value = instance.SetCustomProperty2(FieldName, newValue)
```

### C#

```csharp
System.bool SetCustomProperty2(
   System.string FieldName,
   System.string newValue
)
```

### C++/CLI

```cpp
System.bool SetCustomProperty2(
   System.String^ FieldName,
   System.String^ newValue
)
```

### Parameters

- `FieldName`: Custom property to set
- `newValue`: Value for custom property

### Return Value

True if custom property successfully set, false if not

## VBA Syntax

See [SwDMConfiguration18::SetCustomProperty2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration18~SetCustomProperty2.html).

## Remarks

This method sets an existing custom property.

Before calling this method, call [ISwDMConfiguration::GetCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.html) to populate FieldName.

If you call this method to set a linked custom property with an expression value, then you need to open and save the file in SOLIDWORKS before calling [ISwDMConfiguration::GetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomProperty.html), [ISwDMConfiguration14::GetCustomProperty2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14~GetCustomProperty2.html), [ISwDMConfiguration4::GetAllCustomPropertyNamesAndValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4~GetAllCustomPropertyNamesAndValues.html), or [ISwDMConfiguration5::GetCustomPropertyValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5~GetCustomPropertyValues.html). SOLIDWORKS needs to process the linked custom property before your DocumentMgr application attempts to get its evaluated value.

## See Also

[ISwDMConfiguration18 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration18.html)
[ISwDMConfiguration18 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration18_members.html)
[ISwDMConfiguration::AddCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~AddCustomProperty.html)
[ISwDMConfiguration::DeleteCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~DeleteCustomProperty.html)
[ISwDMConfiguration::GetCustomPropertyCount Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyCount.html)
[ISwDMConfiguration::GetCustomPropertyNames Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.html)
[ISwDMDocument29::SetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument29~SetCustomProperty2.html)

## Availability

SOLIDWORKS Document Manager API 2023 FCS
