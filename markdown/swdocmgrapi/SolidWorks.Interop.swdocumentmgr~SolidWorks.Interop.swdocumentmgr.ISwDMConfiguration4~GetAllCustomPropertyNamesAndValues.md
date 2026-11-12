---
title: "GetAllCustomPropertyNamesAndValues Method (ISwDMConfiguration4)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration4"
member: "GetAllCustomPropertyNamesAndValues"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4~GetAllCustomPropertyNamesAndValues.html"
---

# GetAllCustomPropertyNamesAndValues Method (ISwDMConfiguration4)

Gets all of the custom properties for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetAllCustomPropertyNamesAndValues( _
   ByRef names As System.Object, _
   ByRef types As System.Object, _
   ByRef linkedTo As System.Object, _
   ByRef values As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration4
Dim names As System.Object
Dim types As System.Object
Dim linkedTo As System.Object
Dim values As System.Object

instance.GetAllCustomPropertyNamesAndValues(names, types, linkedTo, values)
```

### C#

```csharp
void GetAllCustomPropertyNamesAndValues(
   out System.object names,
   out System.object types,
   out System.object linkedTo,
   out System.object values
)
```

### C++/CLI

```cpp
void GetAllCustomPropertyNamesAndValues(
   [Out] System.Object^ names,
   [Out] System.Object^ types,
   [Out] System.Object^ linkedTo,
   [Out] System.Object^ values
)
```

### Parameters

- `names`: Array of Property Names
- `types`: Array of Types as defined in [SwDmCustomInfoType](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmCustomInfoType.html)
- `linkedTo`: Array of Estimated Values
- `values`: Array of linked to Values/Text Expressions (see **Remarks**)

### Return Value

| If the properties are... | Then this method returns... |
| --- | --- |
| Linked | The evaluated results of values |
| Not linked | Empty strings. This method returns the same values as returned by ISwDMConfiguration::GetCustomProperty |

## VBA Syntax

See [SwDMConfiguration4::GetAllCustomPropertyNamesAndValues](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration4~GetAllCustomPropertyNamesAndValues.html).

## Remarks

If you called [ISwDMConfiguration::SetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty.html) to set a linked custom property, then you must open and save the file in SOLIDWORKS before calling this method. SOLIDWORKS must process the linked custom property before your DocumentMgr application can retrieve its evaluated value.

## See Also

[ISwDMConfiguration4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4.html)
[ISwDMConfiguration4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4_members.html)
[ISwDMConfiguration::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~AddCustomProperty.html)
[ISwDMConfiguration::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~DeleteCustomProperty.html)
[ISwDMConfiguration::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyCount.html)
[ISwDMConfiguration::GetCustomPropertyNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.html)
[ISwDMConfiguration5::GetCustomPropertyValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5~GetCustomPropertyValues.html)
[ISwDMDocument3::GetAllCustomPropertyNamesAndValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3~GetAllCustomPropertyNamesAndValues.html)
[ISwDMConfiguration14::GetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14~GetCustomProperty2.html)
[ISwDMConfiguration15::IsCustomPropertyEditable Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration15~IsCustomPropertyEditable.html)

## Availability

SOLIDWORKS Document Manager API 2004 SP4
