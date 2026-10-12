---
title: "AddCustomProperty Method (ISwDMConfiguration)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration"
member: "AddCustomProperty"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~AddCustomProperty.html"
---

# AddCustomProperty Method (ISwDMConfiguration)

Adds a custom property to this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCustomProperty( _
   ByVal FieldName As System.String, _
   ByVal SwDmCustomInfoType As SwDmCustomInfoType, _
   ByVal FieldValue As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration
Dim FieldName As System.String
Dim SwDmCustomInfoType As SwDmCustomInfoType
Dim FieldValue As System.String
Dim value As System.Boolean

value = instance.AddCustomProperty(FieldName, SwDmCustomInfoType, FieldValue)
```

### C#

```csharp
System.bool AddCustomProperty(
   System.string FieldName,
   SwDmCustomInfoType SwDmCustomInfoType,
   System.string FieldValue
)
```

### C++/CLI

```cpp
System.bool AddCustomProperty(
   System.String^ FieldName,
   SwDmCustomInfoType SwDmCustomInfoType,
   System.String^ FieldValue
)
```

### Parameters

- `FieldName`: Name of the custom property to add
- `SwDmCustomInfoType`: Type of custom property as defined by [SwDmCustomInfoType](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmCustomInfoType.html)
- `FieldValue`: Value for custom property to add

### Return Value

True if custom property is added, false if not

## VBA Syntax

See [SwDMConfiguration::AddCustomProperty](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration~AddCustomProperty.html).

## Remarks

If you call this method to add a linked custom property with an expression value, then you need to open and save the file in SOLIDWORKS before calling [ISwDMConfiguration::GetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomProperty.html), [ISwDMConfiguration14::GetCustomProperty2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14~GetCustomProperty2.html), [ISwDMConfiguration4::GetAllCustomPropertyNamesAndValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4~GetAllCustomPropertyNamesAndValues.html), or [ISwDMConfiguration5::GetCustomPropertyValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5~GetCustomPropertyValues.html). SOLIDWORKS needs to process the linked custom property before your DocumentMgr application attempts to get its evaluated value.

## See Also

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.html)
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.html)
[ISwDMConfiguration::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~DeleteCustomProperty.html)
[ISwDMConfiguration::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyCount.html)
[ISwDMConfiguration::GetCustomPropertyNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.html)
[ISwDMConfiguration::SetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty.html)
[ISwDMDocument::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~AddCustomProperty.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
