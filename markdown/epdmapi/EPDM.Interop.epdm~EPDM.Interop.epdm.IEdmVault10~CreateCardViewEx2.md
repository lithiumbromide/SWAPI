---
title: "CreateCardViewEx2 Method (IEdmVault10)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault10"
member: "CreateCardViewEx2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault10~CreateCardViewEx2.html"
---

# CreateCardViewEx2 Method (IEdmVault10)

Displays a file or folder data card.

## Syntax

### Visual Basic

```vb
Function CreateCardViewEx2( _
   ByRef poArgs As EdmCardViewParams, _
   ByVal poCallback As System.Object _
) As IEdmCardView63
```

### C#

```csharp
IEdmCardView63 CreateCardViewEx2(
   ref EdmCardViewParams poArgs,
   System.object poCallback
)
```

### C++/CLI

```cpp
IEdmCardView63^ CreateCardViewEx2(
   EdmCardViewParams% poArgs,
   System.Object^ poCallback
)
```

### Parameters

- `poArgs`: [EdmCardViewParams](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardViewParams.html) structure containing various members that control the creation of the view
- `poCallback`: Pointer to a class that implements [IEdmCardViewCallback6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6.html)

### Return Value

[IEdmCardView63](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView63.html)

## Examples

[Create Custom Card View (VB.NET)](Create_Custom_Card_View_Example_VBNET.htm)
[Create Custom Card View (C#)](Create_Custom_Card_View_Example_CSharp.htm)

## Remarks

Use this method if you want complete control of the loading and saving of data to and from a custom file or folder data card. Use [IEdmFolder5::CreateCardView](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CreateCardView.html) if you want SOLIDWORKS PDM Professional to handle the loading and saving of data to and from a simple file or folder data card.

This method supersedes [IEdmVault6::CreateCardViewEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault6~CreateCardViewEx.html) by allowing you to pass a structure instead of individual parameters.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault10 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault10.html)
[IEdmVault10 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault10_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
