---
title: "GetView Method (IEdmBom)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBom"
member: "GetView"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBom~GetView.html"
---

# GetView Method (IEdmBom)

Gets the BOM view for the specified BOM version. The BOM view allows you to read and manipulate the contents of the BOM.

## Syntax

### Visual Basic

```vb
Function GetView( _
   Optional ByVal lVersionNo As System.Integer _
) As EdmBomView
```

### C#

```csharp
EdmBomView GetView(
   System.int lVersionNo
)
```

### C++/CLI

```cpp
EdmBomView^ GetView(
   System.int lVersionNo
)
```

### Parameters

- `lVersionNo`: Version of the BOM whose view you want

### Return Value

[IEdmBomView](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView.html)

## Examples

[Add Row to Bill of Materials (VB.NET)](Add_Row_to_Bill_of_Materials_Example_VBNET.htm)
[Add Row to Bill of Materials (C#)](Add_Row_to_Bill_of_Materials_Example_CSharp.htm)

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBom Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBom.html)
[IEdmBom Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBom_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
