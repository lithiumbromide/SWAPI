---
title: "GetCustomProperty2 Method (ISwDMConfiguration14)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration14"
member: "GetCustomProperty2"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14~GetCustomProperty2.html"
---

# GetCustomProperty2 Method (ISwDMConfiguration14)

Gets the specified custom property for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomProperty2( _
   ByVal FieldName As System.String, _
   ByRef type As SwDmCustomInfoType _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration14
Dim FieldName As System.String
Dim type As SwDmCustomInfoType
Dim value As System.String

value = instance.GetCustomProperty2(FieldName, type)
```

### C#

```csharp
System.string GetCustomProperty2(
   System.string FieldName,
   out SwDmCustomInfoType type
)
```

### C++/CLI

```cpp
System.String^ GetCustomProperty2(
   System.String^ FieldName,
   [Out] SwDmCustomInfoType type
)
```

### Parameters

- `FieldName`: Name of custom property (see **Remarks**)
- `type`: Type of custom property as defined by [SwDmCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.html)

### Return Value

Value of custom property

## VBA Syntax

See [SwDMConfiguration14::GetCustomProperty2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~swDMConfiguration14~GetCustomProperty2.html).

## Examples

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## Remarks

To populate FieldName, use [ISwDMConfiguration::GetCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.html) to get the names of all of the custom properties.

This method returns an evaluated value:

- from when the file was last saved in SOLIDWORKS. If you used [ISwDMConfiguration::SetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty.html) to set a linked custom property, then you need to open and save the file in SOLIDWORKS before your DocumentMgr application calls this method to retrieve the evaluated value of the linked custom property.
- without the **fromparent+** preface for external referenced documents. Use [ISwDMConfiguration::GetCustomProperty](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomProperty.html) to return resolved evaluated values prefaced with **fromparent+**.

## See Also

[ISwDMConfiguration14 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14.html)
[ISwDMConfiguration14 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14_members.html)
[ISwDMConfiguration::AddCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~AddCustomProperty.html)
[ISwDMConfiguration::DeleteCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~DeleteCustomProperty.html)
[ISwDMConfiguration::GetCustomPropertyCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyCount.html)
[ISwDMConfiguration4::GetAllCustomPropertyNamesAndValues Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4~GetAllCustomPropertyNamesAndValues.html)
[ISwDMConfiguration5::GetCustomPropertyValues Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5~GetCustomPropertyValues.html)
[ISwDMDocument::GetCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.html)
[ISwDMDocument17::GetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2.html)
[ISwDMConfiguration15::IsCustomPropertyEditable Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration15~IsCustomPropertyEditable.html)

## Availability

SOLIDWORKS Document Manager API 2013 FCS
