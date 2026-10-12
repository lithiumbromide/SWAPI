---
title: "GetSerNoVar Method (IEdmEnumeratorVariable7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable7"
member: "GetSerNoVar"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable7~GetSerNoVar.html"
---

# GetSerNoVar Method (IEdmEnumeratorVariable7)

Gets the IDs of all variables that have the specified serial number.

## Syntax

### Visual Basic

```vb
Sub GetSerNoVar( _
   ByVal bsSerNoName As System.String, _
   ByVal lFolderID As System.Integer, _
   ByRef ppoRetIDs As System.Integer() _
)
```

### C#

```csharp
void GetSerNoVar(
   System.string bsSerNoName,
   System.int lFolderID,
   out System.int[] ppoRetIDs
)
```

### C++/CLI

```cpp
void GetSerNoVar(
   System.String^ bsSerNoName,
   System.int lFolderID,
   [Out] System.array<int> ppoRetIDs
)
```

### Parameters

- `bsSerNoName`: Serial number of variables to find
- `lFolderID`: ID of the file's parent folder; 0 if the file is not shared
- `ppoRetIDs`: Array of IDs of variables with bSerNoName

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmEnumeratorVariable7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable7.html)
[IEdmEnumeratorVariable7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable7_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.4
