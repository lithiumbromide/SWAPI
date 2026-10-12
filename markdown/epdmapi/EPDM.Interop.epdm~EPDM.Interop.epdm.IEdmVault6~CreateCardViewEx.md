---
title: "CreateCardViewEx Method (IEdmVault6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault6"
member: "CreateCardViewEx"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault6~CreateCardViewEx.html"
---

# CreateCardViewEx Method (IEdmVault6)

Obsolete. Superseded by [IEdmVault10::CreateCardViewEx2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault10~CreateCardViewEx2.html).

## Syntax

### Visual Basic

```vb
Function CreateCardViewEx( _
   ByVal lEdmCardViewFlags As System.Integer, _
   ByVal lCardID As System.Integer, _
   ByVal lParentWindow As System.Integer, _
   ByVal lX As System.Integer, _
   ByVal lY As System.Integer, _
   ByVal poCallback As IEdmCardViewCallback6 _
) As IEdmCardView6
```

### C#

```csharp
IEdmCardView6 CreateCardViewEx(
   System.int lEdmCardViewFlags,
   System.int lCardID,
   System.int lParentWindow,
   System.int lX,
   System.int lY,
   IEdmCardViewCallback6 poCallback
)
```

### C++/CLI

```cpp
IEdmCardView6^ CreateCardViewEx(
   System.int lEdmCardViewFlags,
   System.int lCardID,
   System.int lParentWindow,
   System.int lX,
   System.int lY,
   IEdmCardViewCallback6^ poCallback
)
```

### Parameters

- `lEdmCardViewFlags`: Combination of [EdmCardViewFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardViewFlag.html) bits
- `lCardID`: ID of card to display (see **Remarks**)
- `lParentWindow`: Parent window handle
- `lX`: X-position in pixels of the parent window
- `lY`: Y-position in pixels of the parent window
- `poCallback`: Pointer to a class that implements [IEdmCardViewCallback6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6.html)

### Return Value

[IEdmCardView6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView6.html)

## Remarks

Use this method if you want complete control of the loading and saving of data to and from a custom file or folder data card. Use [IEdmFolder5::CreateCardView](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CreateCardView.html) if you want SOLIDWORKS PDM Professional to handle the loading and saving of data to and from a simple file or folder data card.

To obtain lCardID, call [IEdmVault6::GetCardID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault6~GetCardID.html).

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_INVALID_ID: The specified card ID is invalid.

## See Also

[IEdmVault6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault6.html)
[IEdmVault6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0
