---
title: "HasRightsEx Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "HasRightsEx"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~HasRightsEx.html"
---

# HasRightsEx Method (IEdmFolder5)

Gets whether the user has the specified rights for the specified file in this folder.

## Syntax

### Visual Basic

```vb
Function HasRightsEx( _
   ByVal lRights As System.Integer, _
   Optional ByVal lFileID As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool HasRightsEx(
   System.int lRights,
   System.int lFileID
)
```

### C++/CLI

```cpp
System.bool HasRightsEx(
   System.int lRights,
   System.int lFileID
)
```

### Parameters

- `lRights`: Combination of [EdmRightFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRightFlags.html) bits
- `lFileID`: Optional ID of file on which to check lRights; 0 or null to check lRights on this folder only

### Return Value

True if the user has all of the specified permissions, false if the user is missing one or more of the specified permissions

## Examples

[Vault Utilities (VB.NET)](Vault_Utilities_Example_VBNET.htm)
[Vault Utilities (C#)](Vault_Utilities_Example_CSharp.htm)

## Remarks

This method takes into account both the rights set explicitly on the user and those inherited from groups of which the user is a member. Optionally, you can specify the ID of a file for which to check rights. In that case, the rights-check includes workflow rights set on the current status of the file. If no file ID is specified, or it is 0, the rights-check is performed only on this folder.

**Note**: This method is only available in SOLIDWORKS PDM Professional Version 5.3 and later. If the program must have backward compatibility with SOLIDWORKS PDM Professional 5.2, use [IEdmFolder5::HasRights](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~HasRights.html) instead.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: The user lacks one or more of the specified rights.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.3
