---
title: "GetCustomProperty Method (ISwDMComponent12)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent12"
member: "GetCustomProperty"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent12~GetCustomProperty.html"
---

# GetCustomProperty Method (ISwDMComponent12)

Gets the specified custom property for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomProperty( _
   ByVal FieldName As System.String, _
   ByRef type As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent12
Dim FieldName As System.String
Dim type As System.Integer
Dim value As System.String

value = instance.GetCustomProperty(FieldName, type)
```

### C#

```csharp
System.string GetCustomProperty(
   System.string FieldName,
   out System.int type
)
```

### C++/CLI

```cpp
System.String^ GetCustomProperty(
   System.String^ FieldName,
   [Out] System.int type
)
```

### Parameters

- `FieldName`: Name of custom property
- `type`: Type of custom property as defined by [SwDMCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.html)

### Return Value

Value of the custom property

## VBA Syntax

See [SwDMComponent12::GetCustomProperty](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent12~GetCustomProperty.html).

## Examples

[Get Configuration-Specific Custom Properties for Components (VB.NET)](Get_Configuration-Specific_Custom_Properties_Example_VBNET.htm)
[Get Configuration-Specific Custom Properties for Components (C#)](Get_Configuration-Specific_Custom_Properties_Example_CSharp.htm)

## See Also

[ISwDMComponent12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent12.html)
[ISwDMComponent12 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent12_members.html)

## Availability

SOLIDWORKS Document Manager API 2024 SP0
