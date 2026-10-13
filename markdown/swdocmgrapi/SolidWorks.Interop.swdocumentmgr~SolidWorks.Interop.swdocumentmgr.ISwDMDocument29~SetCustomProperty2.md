---
title: "SetCustomProperty2 Method (ISwDMDocument29)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument29"
member: "SetCustomProperty2"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument29~SetCustomProperty2.html"
---

# SetCustomProperty2 Method (ISwDMDocument29)

Sets a custom property for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCustomProperty2( _
   ByVal FieldName As System.String, _
   ByVal newValue As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument29
Dim FieldName As System.String
Dim newValue As System.String
Dim value As System.Boolean

value = instance.SetCustomProperty2(FieldName, newValue)
```

### C#

```csharp
System.bool SetCustomProperty2(
   System.string FieldName,
   System.string newValue
)
```

### C++/CLI

```cpp
System.bool SetCustomProperty2(
   System.String^ FieldName,
   System.String^ newValue
)
```

### Parameters

- `FieldName`: Name of custom property
- `newValue`: Value for custom property

### Return Value

True if custom property successfully set, false if not

## VBA Syntax

See [SwDMDocument29::SetCustomProperty2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument29~SetCustomProperty2.html).

## Remarks

This method sets an existing custom property.

Before calling this method, call [ISwDMDocument::GetCustomPropertyNames](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyNames.html) to populate FieldName.

If you call this method to set a linked custom property with an expression value, then you need to open and save the file in SOLIDWORKS before calling [ISwDMDocument::GetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.html), [ISwDMDocument17::GetCustomProperty2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2.html), [ISwDMDocument3::GetAllCustomPropertyNamesAndValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3~GetAllCustomPropertyNamesAndValues.html), or [ISwDMDocument5::GetCustomPropertyValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetCustomPropertyValues.html). SOLIDWORKS needs to process the linked custom property before your DocumentMgr application attempts to get its evaluated value.

## See Also

[ISwDMDocument29 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument29.html)
[ISwDMDocument29 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument29_members.html)
[ISwDMDocument::AddCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~AddCustomProperty.html)
[ISwDMDocument::DeleteCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~DeleteCustomProperty.html)
[ISwDMDocument::GetCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.html)
[ISwDMConfiguration18::SetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty.html)

## Availability

SOLIDWORKS Document Manager API 2023 FCS
