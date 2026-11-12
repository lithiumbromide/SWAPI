---
title: "GetAllCustomPropertyNamesAndValues Method (ISwDMDocument3)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument3"
member: "GetAllCustomPropertyNamesAndValues"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3~GetAllCustomPropertyNamesAndValues.html"
---

# GetAllCustomPropertyNamesAndValues Method (ISwDMDocument3)

Gets all of the custom properties for this document.

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
Dim instance As ISwDMDocument3
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
- `types`: Array of Types
- `linkedTo`: Array of linked to Values/Text Expressions (see Remarks)
- `values`: Array of Evaluated Values

## VBA Syntax

See [SwDMDocument3::GetAllCustomPropertyNamesAndValues](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument3~GetAllCustomPropertyNamesAndValues.html).

## Remarks

| If the properties are... | Then this method returns... |
| --- | --- |
| Linked | The evaluated results of linkedTo |
| Not linked | Empty strings. This method returns the same values as returned by ISwDMDocument::GetCustomProperty |

This method returns evaluated values from when the document was last saved in SOLIDWORKS.

If you called [ISwDMDocument::SetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SetCustomProperty.html) to set a linked custom property, then you must open and save the file in SOLIDWORKS before calling this method. SOLIDWORKS must process the linked custom property before your DocumentMgr application can retrieve its evaluated value.

## See Also

[ISwDMDocument3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3.html)
[ISwDMDocument3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3_members.html)
[ISwDMDocument::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~DeleteCustomProperty.html)
[ISwDMDocument::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyCount.html)
[ISwDMDocument::GetCustomPropertyNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyNames.html)
[ISwDMConfiguration4::GetAllCustomPropertyNamesAndValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4~GetAllCustomPropertyNamesAndValues.html)
[ISwDMDocument5::GetCustomPropertyValues Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetCustomPropertyValues.html)
[ISwDMDocument17::GetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2.html)

## Availability

SOLIDWORKS Document Manager API 2004 SP4
