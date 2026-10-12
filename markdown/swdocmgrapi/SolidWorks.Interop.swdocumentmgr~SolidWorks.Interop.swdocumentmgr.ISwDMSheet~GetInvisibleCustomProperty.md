---
title: "GetInvisibleCustomProperty Method (ISwDMSheet)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMSheet"
member: "GetInvisibleCustomProperty"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet~GetInvisibleCustomProperty.html"
---

# GetInvisibleCustomProperty Method (ISwDMSheet)

Gets the sheet's specified invisible sheet custom property.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInvisibleCustomProperty( _
   ByVal FieldName As System.String, _
   ByRef type As SwDmCustomInfoType _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMSheet
Dim FieldName As System.String
Dim type As SwDmCustomInfoType
Dim value As System.String

value = instance.GetInvisibleCustomProperty(FieldName, type)
```

### C#

```csharp
System.string GetInvisibleCustomProperty(
   System.string FieldName,
   out SwDmCustomInfoType type
)
```

### C++/CLI

```cpp
System.String^ GetInvisibleCustomProperty(
   System.String^ FieldName,
   [Out] SwDmCustomInfoType type
)
```

### Parameters

- `FieldName`: Name of the custom property
- `type`: Type of custom property as defined by [swDMCustomInfoType](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmCustomInfoType.html)

### Return Value

Value of the custom property

## VBA Syntax

See [SwDMSheet::GetInvisibleCustomProperty](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMSheet~GetInvisibleCustomProperty.html).

## Remarks

Before calling this method, call [ISwDMSheet::GetInvisibleCustomPropertyNames](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSheet~GetInvisibleCustomPropertyNames.html).

## See Also

[ISwDMSheet Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet.html)
[ISwDMSheet Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet_members.html)
[ISwDMSheet::GetInvisibleCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet~GetInvisibleCustomPropertyCount.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
