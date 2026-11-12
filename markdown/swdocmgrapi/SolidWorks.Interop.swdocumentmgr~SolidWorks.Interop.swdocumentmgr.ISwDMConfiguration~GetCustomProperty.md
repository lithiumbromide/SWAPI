---
title: "GetCustomProperty Method (ISwDMConfiguration)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration"
member: "GetCustomProperty"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomProperty.html"
---

# GetCustomProperty Method (ISwDMConfiguration)

Gets the specified custom property for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomProperty( _
   ByVal FieldName As System.String, _
   ByRef type As SwDmCustomInfoType _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration
Dim FieldName As System.String
Dim type As SwDmCustomInfoType
Dim value As System.String

value = instance.GetCustomProperty(FieldName, type)
```

### C#

```csharp
System.string GetCustomProperty(
   System.string FieldName,
   out SwDmCustomInfoType type
)
```

### C++/CLI

```cpp
System.String^ GetCustomProperty(
   System.String^ FieldName,
   [Out] SwDmCustomInfoType type
)
```

### Parameters

- `FieldName`: Name of the custom property
- `type`: Type of custom property as defined by [SwDmCustomInfoType](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmCustomInfoType.html)

### Return Value

Value of the custom property

## VBA Syntax

See [SwDMConfiguration::GetCustomProperty](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration~GetCustomProperty.html).

## Examples

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## Remarks

To get the names of all the custom properties for this configuration, call [ISwDMConfiguration::GetCustomPropertyNames](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.html).

This method returns an evaluated value:

- from when the file was last saved in SOLIDWORKS. If you used [ISwDMConfiguration::SetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty.html) to set a linked custom property, then you need to open and save the file in SOLIDWORKS before your DocumentMgr application calls this method to retrieve the evaluated value of the linked custom property.

- prefaced with **fromparent+** for external referenced documents. Use [ISwConfiguration14::GetCustomProperty2](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration14~GetCustomProperty2.html) to return resolved evaluated values without the **fromparent+** preface.

## See Also

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.html)
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.html)
[ISwDMConfiguration::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~AddCustomProperty.html)
[ISwDMConfiguration::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~DeleteCustomProperty.html)
[ISwDMConfiguration::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyCount.html)
[ISwDMConfiguration4::GetAllCustomPropertyNamesAndValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4~GetAllCustomPropertyNamesAndValues.html)
[ISwDMConfiguration5::GetCustomPropertyValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5~GetCustomPropertyValues.html)
[ISwDMDocument::GetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.html)
[ISwDMDocument17::GetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
