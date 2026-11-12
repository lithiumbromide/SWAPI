---
title: "DeleteCustomProperty Method (ISwDMConfiguration)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration"
member: "DeleteCustomProperty"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~DeleteCustomProperty.html"
---

# DeleteCustomProperty Method (ISwDMConfiguration)

Deletes the specified custom property from this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteCustomProperty( _
   ByVal FieldName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration
Dim FieldName As System.String
Dim value As System.Boolean

value = instance.DeleteCustomProperty(FieldName)
```

### C#

```csharp
System.bool DeleteCustomProperty(
   System.string FieldName
)
```

### C++/CLI

```cpp
System.bool DeleteCustomProperty(
   System.String^ FieldName
)
```

### Parameters

- `FieldName`: Name of custom property to delete

### Return Value

True if custom property is deleted, false if not

## VBA Syntax

See [SwDMConfiguration::DeleteCustomProperty](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration~DeleteCustomProperty.html).

## Remarks

To get the names of the custom properties for this configuration, call [ISwDMConfiguration::GetCustomPropertyNames](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.html).

## See Also

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.html)
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.html)
[ISwDMConfiguration::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~AddCustomProperty.html)
[ISwDMConfiguration::GetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomProperty.html)
[ISwDMConfiguration::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyCount.html)
[ISwDMConfiguration::SetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty.html)
[ISwDMConfiguration4::GetAllCustomPropertyNamesAndValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4~GetAllCustomPropertyNamesAndValues.html)
[ISwDMConfiguration5::GetCustomPropertyValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5~GetCustomPropertyValues.html)
[ISwDMDocument::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~DeleteCustomProperty.html)
[ISwDMConfiguration14::GetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14~GetCustomProperty2.html)
[ISwDMConfiguration::GetCustomPropertyNames Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
