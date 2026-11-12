---
title: "SetPropt Method (IEdmFindUser)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFindUser"
member: "SetPropt"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser~SetPropt.html"
---

# SetPropt Method (IEdmFindUser)

Sets the search criteria for finding users.

## Syntax

### Visual Basic

```vb
Sub SetPropt( _
   ByVal eProp As EdmFindUserProp, _
   ByVal oValue As System.Object _
)
```

### C#

```csharp
void SetPropt(
   EdmFindUserProp eProp,
   System.object oValue
)
```

### C++/CLI

```cpp
void SetPropt(
   EdmFindUserProp eProp,
   System.Object^ oValue
)
```

### Parameters

- `eProp`: User property to search for as defined by [EdmFindUserProp](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFindUserProp.html)
- `oValue`: Value of the property specified in eProp

## Examples

See the [IEdmFindUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser.html) examples.

## Remarks

After calling this method, call one of the following:

- [IEdmFindUser::SilentFind](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser~SilentFind.html) to silently search for users matching the criteria specified by this method.
- [IEdmFindUser::ShowFindUI](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser~ShowFindUI.html) to display a search user interface that is populated with the criteria specified by this method.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmFindUser Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser.html)
[IEdmFindUser Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
