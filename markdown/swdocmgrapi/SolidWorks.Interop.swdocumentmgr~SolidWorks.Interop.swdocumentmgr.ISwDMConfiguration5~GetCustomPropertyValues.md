---
title: "GetCustomPropertyValues Method (ISwDMConfiguration5)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration5"
member: "GetCustomPropertyValues"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5~GetCustomPropertyValues.html"
---

# GetCustomPropertyValues Method (ISwDMConfiguration5)

Gets the specified custom property value for this configuration.

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
Dim instance As ISwDMConfiguration5
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

See **Remarks**

## VBA Syntax

See [SwDMConfiguration5::GetCustomPropertyValues](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration5~GetCustomPropertyValues.html).

## Remarks

| If the property is... | Then this method returns... |
| --- | --- |
| Linked | The evaluated result of linkedTo |
| Not linked | An empty string. This method returns the same value as returned by ISwDMConfiguration::GetCustomProperty |

This property only supports documents saved in SOLIDWORKS 2005 and later. To get the version of a document, use [ISwDMDocument::GetVersion](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetVersion.html).

If you called [ISwDMConfiguration::SetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty.html) to set a linked custom property, then you must open and save the file in SOLIDWORKS before calling this method. SOLIDWORKS must process the linked custom property before your DocumentMgr application can retrieve its evaluated value.

## See Also

[ISwDMConfiguration5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5.html)
[ISwDMConfiguration5 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5_members.html)

## Availability

SOLIDWORKS Document Manager API 2005 FCS
