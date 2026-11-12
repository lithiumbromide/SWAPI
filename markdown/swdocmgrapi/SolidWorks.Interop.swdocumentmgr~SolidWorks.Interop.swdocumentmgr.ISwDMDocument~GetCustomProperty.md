---
title: "GetCustomProperty Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "GetCustomProperty"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.html"
---

# GetCustomProperty Method (ISwDMDocument)

Gets the specified custom property for this document.

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
Dim instance As ISwDMDocument
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

- `FieldName`: Name of custom property
- `type`: Type of custom property as defined by [SwDmCustomInfoType](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmCustomInfoType.html)

### Return Value

Value of custom property

## VBA Syntax

See [SwDMDocument::GetCustomProperty](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~GetCustomProperty.html).

## Examples

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## Remarks

Before calling this method, call [ISwDMDocument::GetCustomPropertyNames](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyNames.html) to populate FieldNames.

This method returns an evaluated value:

- from when the document was last saved in SOLIDWORKS. If you called [ISwDMDocument::SetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SetCustomProperty.html) to set a linked custom property, then you must open and save the file in SOLIDWORKS before calling this method. SOLIDWORKS must process the linked custom property before your DocumentMgr application can retrieve its evaluated value.

- prefaced with **fromparent+** for external referenced documents. Use [ISwDocument17::GetCustomProperty2](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2.html) to return resolved evaluated values without the **fromparent+** preface.

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~AddCustomProperty.html)
[ISwDMDocument::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~DeleteCustomProperty.html)
[ISwDMDocument::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyCount.html)
[ISwDMDocument3::GetAllCustomPropertyNamesAndValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3~GetAllCustomPropertyNamesAndValues.html)
[ISwDMDocument5::GetCustomPropertyValues Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetCustomPropertyValues.html)
[ISwDMConfiguration::GetCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomProperty.html)
[ISwDMConfiguration14::GetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14~GetCustomProperty2.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
