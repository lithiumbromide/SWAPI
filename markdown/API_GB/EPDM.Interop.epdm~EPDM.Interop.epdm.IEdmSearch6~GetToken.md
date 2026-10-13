---
title: "GetToken Method (IEdmSearch6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch6"
member: "GetToken"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch6~GetToken.html"
---

# GetToken Method (IEdmSearch6)

Gets the value of a search token.

## Syntax

### Visual Basic

```vb
Function GetToken( _
   ByVal eTok As EdmSearchToken _
) As System.Object
```

### C#

```csharp
System.object GetToken(
   EdmSearchToken eTok
)
```

### C++/CLI

```cpp
System.Object^ GetToken(
   EdmSearchToken eTok
)
```

### Parameters

- `eTok`: Type of token for which to get a value as defined in [EdmSearchToken](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSearchToken.html)

### Return Value

Value of token

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmSearch6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch6.html)
[IEdmSearch6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch6_members.html)
[IEdmSearch6::SetToken Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch6~SetToken.html)

## Availability

SOLIDWORKS PDM Professional 2007
