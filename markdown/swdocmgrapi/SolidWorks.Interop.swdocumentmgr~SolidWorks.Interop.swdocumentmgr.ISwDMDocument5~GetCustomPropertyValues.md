---
title: "GetCustomPropertyValues Method (ISwDMDocument5)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument5"
member: "GetCustomPropertyValues"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetCustomPropertyValues.html"
---

# GetCustomPropertyValues Method (ISwDMDocument5)

Gets the specified custom property value for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomPropertyValues( _
   ByVal FieldName As System.String, _
   ByRef type As SwDmCustomInfoType, _
   ByRef linkedTo As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument5
Dim FieldName As System.String
Dim type As SwDmCustomInfoType
Dim linkedTo As System.String
Dim value As System.String

value = instance.GetCustomPropertyValues(FieldName, type, linkedTo)
```

### C#

```csharp
System.string GetCustomPropertyValues(
   System.string FieldName,
   out SwDmCustomInfoType type,
   out System.string linkedTo
)
```

### C++/CLI

```cpp
System.String^ GetCustomPropertyValues(
   System.String^ FieldName,
   [Out] SwDmCustomInfoType type,
   [Out] System.String^ linkedTo
)
```

### Parameters

- `FieldName`: Property Name
- `type`: Type of custom property as defined in [SwDmCustomInfoType](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmCustomInfoType.html)
- `linkedTo`: Linked to Value/Text Expression (see Remarks)

### Return Value

Evaluated Value

## VBA Syntax

See [SwDMDocument5::GetCustomPropertyValues](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument5~GetCustomPropertyValues.html).

## Remarks

This property only supports documents saved in SOLIDWORKS 2005 and later.

| If the property is... | Then this method returns... |
| --- | --- |
| Linked | The evaluated result of linkedTo. |
| Not linked | An empty string. This method returns the same value as returned by ISwDMDocument::GetCustomProperty |

This method returns evaluated values from when the document was last saved in SOLIDWORKS.

If you called [ISwDMDocument::SetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SetCustomProperty.html) to set a linked custom property, then you must open and save the file in SOLIDWORKS before calling this method. SOLIDWORKS must process the linked custom property before your DocumentMgr application can retrieve its evaluated value.

## See Also

[ISwDMDocument5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5.html)
[ISwDMDocument5 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5_members.html)
[ISwDocument::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~AddCustomProperty.html)
[ISwDocument::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~DeleteCustomProperty.html)
[ISwDocument::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyCount.html)
[ISwDocument::GetCustomPropertyNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyNames.html)
[ISwDMDocument3::GetAllCustomPropertyNamesAndValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3~GetAllCustomPropertyNamesAndValues.html)
[ISwConfiguration::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~AddCustomProperty.html)
[ISwConfiguration::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~DeleteCustomProperty.html)
[ISwConfiguration::GetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomProperty.html)
[ISwConfiguration::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyCount.html)
[ISwConfiguration::GetCustomPropertyNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.html)
[ISwConfiguration::SetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty.html)
[ISwConfiguration4::GetAllCustomPropertyNamesAndValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4~GetAllCustomPropertyNamesAndValues.html)
[ISwConfiguration5::GetCustomPropertyValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5~GetCustomPropertyValues.html)

## Availability

SOLIDWORKS Document Manager API 2005 FCS
