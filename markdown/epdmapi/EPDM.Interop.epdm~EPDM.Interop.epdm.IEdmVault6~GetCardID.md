---
title: "GetCardID Method (IEdmVault6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault6"
member: "GetCardID"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault6~GetCardID.html"
---

# GetCardID Method (IEdmVault6)

Gets the ID of a card of the specified type, with the specified name, and in the specified folder.

## Syntax

### Visual Basic

```vb
Function GetCardID( _
   ByVal eType As EdmCardType, _
   ByVal bsName As System.String, _
   Optional ByVal lFolderID As System.Integer _
) As System.Integer
```

### C#

```csharp
System.int GetCardID(
   EdmCardType eType,
   System.string bsName,
   System.int lFolderID
)
```

### C++/CLI

```cpp
System.int GetCardID(
   EdmCardType eType,
   System.String^ bsName,
   System.int lFolderID
)
```

### Parameters

- `eType`: Type of card to get as defined in [EdmCardType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardType.html)
- `bsName`: Name of the card to get
- `lFolderID`: ID of the folder in which the card is stored; 0 for search cards and template

### Return Value

Card ID; 0 if not found

## Remarks

After calling this method, you can use the returned ID in calls to [IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html) or [IEdmVault6::CreateCardViewEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault6~CreateCardViewEx.html).

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: The specified card was not found.

## See Also

[IEdmVault6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault6.html)
[IEdmVault6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0
