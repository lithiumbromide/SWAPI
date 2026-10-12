---
title: "DeleteCustomProperty Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "DeleteCustomProperty"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~DeleteCustomProperty.html"
---

# DeleteCustomProperty Method (ISwDMDocument)

Deletes the specified custom property from this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteCustomProperty( _
   ByVal FieldName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
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

See [SwDMDocument::DeleteCustomProperty](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~DeleteCustomProperty.html).

## Remarks

Before calling this method, call [ISwDMDocument::GetCustomPropertyNames](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyNames.html).

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~AddCustomProperty.html)
[ISwDMDocument::GetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.html)
[ISwDMDocument::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyCount.html)
[ISwDMDocument::SetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SetCustomProperty.html)
[ISwDMDocument3::GetAllCustomPropertyNamesAndValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3~GetAllCustomPropertyNamesAndValues.html)
[ISwDMConfiguration::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~DeleteCustomProperty.html)
[ISwDMDocument17::GetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2.html)
[ISwDocument5::GetCustomPropertyValues Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetCustomPropertyValues.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
