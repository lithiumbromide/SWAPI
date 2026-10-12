---
title: "AddReference2 Method (IEdmEnumeratorCustomReference6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorCustomReference6"
member: "AddReference2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference6~AddReference2.html"
---

# AddReference2 Method (IEdmEnumeratorCustomReference6)

Obsolete. Superseded by [IEdmEnumeratorCustomReference7::AddReference3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference7~AddReference3.html).

## Syntax

### Visual Basic

```vb
Sub AddReference2( _
   ByVal lFileID As System.Integer, _
   ByVal lFolderID As System.Integer, _
   ByVal lQuantity As System.Integer _
)
```

### C#

```csharp
void AddReference2(
   System.int lFileID,
   System.int lFolderID,
   System.int lQuantity
)
```

### C++/CLI

```cpp
void AddReference2(
   System.int lFileID,
   System.int lFolderID,
   System.int lQuantity
)
```

### Parameters

- `lFileID`: ID of referenced file
- `lFolderID`: ID of parent folder of referenced file
- `lQuantity`: Number of times the referenced file is referenced

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_FILE_NOT_LOCKED_BY_YOU: File is not checked out.

## See Also

[IEdmEnumeratorCustomReference6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference6.html)
[IEdmEnumeratorCustomReference6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference6_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
