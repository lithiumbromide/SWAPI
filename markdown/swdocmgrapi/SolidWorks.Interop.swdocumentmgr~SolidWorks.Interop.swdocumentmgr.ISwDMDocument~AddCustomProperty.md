---
title: "AddCustomProperty Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "AddCustomProperty"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~AddCustomProperty.html"
---

# AddCustomProperty Method (ISwDMDocument)

Adds a custom property to document.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCustomProperty( _
   ByVal FieldName As System.String, _
   ByVal FieldType As SwDmCustomInfoType, _
   ByVal FieldValue As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim FieldName As System.String
Dim FieldType As SwDmCustomInfoType
Dim FieldValue As System.String
Dim value As System.Boolean

value = instance.AddCustomProperty(FieldName, FieldType, FieldValue)
```

### C#

```csharp
System.bool AddCustomProperty(
   System.string FieldName,
   SwDmCustomInfoType FieldType,
   System.string FieldValue
)
```

### C++/CLI

```cpp
System.bool AddCustomProperty(
   System.String^ FieldName,
   SwDmCustomInfoType FieldType,
   System.String^ FieldValue
)
```

### Parameters

- `FieldName`: Name of custom property
- `FieldType`: Type of custom property as defined by [SwDmCustomInfoType](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmCustomInfoType.html)
- `FieldValue`: Value for custom property

### Return Value

True if custom property is added, false if not

## VBA Syntax

See [SwDMDocument::AddCustomProperty](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~AddCustomProperty.html).

## Remarks

This method also returns false if you attempt to add a custom property name that already exists.

If you call this method to add a linked custom property with an expression value, then you need to open and save the file in SOLIDWORKS before calling [ISwDMDocument::GetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.html), [ISwDMDocument17::GetCustomProperty2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2.html), [ISwDMDocument3::GetAllCustomPropertyNamesAndValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3~GetAllCustomPropertyNamesAndValues.html), or [ISwDMDocument5::GetCustomPropertyValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetCustomPropertyValues.html). SOLIDWORKS needs to process the linked custom property before your DocumentMgr application attempts to get its evaluated value.

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~DeleteCustomProperty.html)
[ISwDMDocument::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyCount.html)
[ISwDMDocument::GetCustomPropertyNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyNames.html)
[ISwDMDocument::SetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SetCustomProperty.html)
[ISwDMConfiguration::AddCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~AddCustomProperty.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
