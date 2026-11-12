---
title: "GetCustomProperty2 Method (ISwDMDocument17)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument17"
member: "GetCustomProperty2"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2.html"
---

# GetCustomProperty2 Method (ISwDMDocument17)

Gets the specified custom property for this document.

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
Dim instance As ISwDMDocument17
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
- `type`: Type of custom property as defined by [SwDmCustomInfoType](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmCustomInfoType.html)

### Return Value

Value of custom property

## VBA Syntax

See [SwDMDocument17::GetCustomProperty2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument17~GetCustomProperty2.html).

## Examples

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## Remarks

To populate FieldName, use [ISwDMDocument::GetCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyNames.html) to get the names of all of the custom properties.

This method returns an evaluated value:

- from when the document was last saved in SOLIDWORKS.

  If you called [ISwDMDocument::SetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SetCustomProperty.html) to set a linked custom property, then you must open and save the file in SOLIDWORKS before calling this method. SOLIDWORKS must process the linked custom property before your DocumentMgr application can retrieve its evaluated value.
- without the **fromparent+** preface for externally referenced documents. Use [ISwDMDocument::GetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.html) to return resolved evaluated values prefaced with **fromparent+**.

## See Also

[ISwDMDocument17 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17.html)
[ISwDMDocument17 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17_members.html)
[ISwDMDocument::AddCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~AddCustomProperty.html)
[ISwDMDocument::DeleteCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~DeleteCustomProperty.html)
[ISwDMDocument::GetCustomPropertyCount Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyCount.html)
[ISwDMDocument5::GetCustomPropertyValues Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetCustomPropertyValues.html)
[ISwDMConfiguration::GetCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomProperty.html)
[ISwDMConfiguration14::GetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14~GetCustomProperty2.html)

## Availability

SOLIDWORKS Document Manager API 2013 FCS
