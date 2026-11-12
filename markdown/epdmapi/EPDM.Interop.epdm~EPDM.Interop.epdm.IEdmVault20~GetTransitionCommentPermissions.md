---
title: "GetTransitionCommentPermissions Method (IEdmVault20)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault20"
member: "GetTransitionCommentPermissions"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault20~GetTransitionCommentPermissions.html"
---

# GetTransitionCommentPermissions Method (IEdmVault20)

Gets whether the specified user must add a state change comment for the specified workflow transitions for the specified documents.

## Syntax

### Visual Basic

```vb
Function GetTransitionCommentPermissions( _
   ByVal lUserID As System.Integer, _
   ByVal poDocIds() As System.Integer, _
   ByVal poTransNames() As System.String _
) As System.Boolean()
```

### C#

```csharp
System.bool[] GetTransitionCommentPermissions(
   System.int lUserID,
   System.int[] poDocIds,
   System.string[] poTransNames
)
```

### C++/CLI

```cpp
System.array<bool>^ GetTransitionCommentPermissions(
   System.int lUserID,
   System.array<int>^ poDocIds,
   System.array<String^>^ poTransNames
)
```

### Parameters

- `lUserID`: User ID (see **Remarks**)
- `poDocIds`: Array of document IDs (see **Remarks**)
- `poTransNames`: Array of workfow transition names (see **Remarks**)

### Return Value

Array of booleans (see **Remarks**)

## Examples

See the [IEdmVault20](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault20.html) examples.

## Remarks

The returned one-dimensional array contains (`n` * `m`) booleans indicating whether lUserID must add a state change comment on each workflow transition in poTransNames for each document in poDocIds.

For:

- `n` = size of poDocIds
- `m` = size of poTransNames
- `permbool_*` = true or false

the returned array follows the order of elements in poDocIds and poTransNames as follows:

{

`permbool_poDocIds(0)_poTransNames(0)`

`...`

`permbool_poDocIds(0)_poTransNames(m-1)`

`permbool_poDocIds(1)_poTransNames(0)`

`...`

`permbool_poDocIds(1)_poTransNames(m-1)`

`...`

`...`

`permbool_poDocIds(n-1)_poTransNames(0)`

`...`

`permbool_poDocIds(n-1)_poTransNames(m-1)`

}

## See Also

[IEdmVault20 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault20.html)
[IEdmVault20 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault20_members.html)

## Availability

SOLIDWORKS PDM Professional 2019
