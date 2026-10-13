---
title: "SetToken Method (IEdmSearch6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch6"
member: "SetToken"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch6~SetToken.html"
---

# SetToken Method (IEdmSearch6)

Sets the specified token with the specified value.

## Syntax

### Visual Basic

```vb
Sub SetToken( _
   ByVal eTok As EdmSearchToken, _
   ByVal oValue As System.Object _
)
```

### C#

```csharp
void SetToken(
   EdmSearchToken eTok,
   System.object oValue
)
```

### C++/CLI

```cpp
void SetToken(
   EdmSearchToken eTok,
   System.Object^ oValue
)
```

### Parameters

- `eTok`: Search token for which to set a value as defined in [EdmSearchToken](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSearchToken.html) (see **Remarks)**
- `oValue`: New value for token

## Examples

See the [IEdmSearch6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch6.html) and [IEdmSearch9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9.html) examples.

## Remarks

For every search you must explicitly set EdmSearchToken.Edmstok_AllVersions to either true or false. If you leave it unset, unexpected search results can occur.

If the search object was obtained using [IEdmVault21::CreateSearch2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault21~CreateSearch2.html) (IEdmSearch9), then oValue may contain extended search syntax. (See [Search Syntax](SearchSyntax-epdmapi.html).)

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmSearch6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch6.html)
[IEdmSearch6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch6_members.html)

## Availability

SOLIDWORKS PDM Professional 2007
