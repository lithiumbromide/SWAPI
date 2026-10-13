---
title: "GetPropt Method (IEdmFindUser)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFindUser"
member: "GetPropt"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser~GetPropt.html"
---

# GetPropt Method (IEdmFindUser)

Gets the search criteria previously set by [IEdmFindUser::SetPropt](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser~SetPropt.html) for finding users.

## Syntax

### Visual Basic

```vb
Function GetPropt( _
   ByVal eProp As EdmFindUserProp _
) As System.Object
```

### C#

```csharp
System.object GetPropt(
   EdmFindUserProp eProp
)
```

### C++/CLI

```cpp
System.Object^ GetPropt(
   EdmFindUserProp eProp
)
```

### Parameters

- `eProp`: User property to search for as defined by [EdmFindUserProp](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFindUserProp.html)

### Return Value

Value of the property specified in eProp

## Examples

See the [IEdmFindUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmFindUser Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser.html)
[IEdmFindUser Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
