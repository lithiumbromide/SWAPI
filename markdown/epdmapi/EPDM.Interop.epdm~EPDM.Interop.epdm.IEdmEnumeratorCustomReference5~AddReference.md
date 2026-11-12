---
title: "AddReference Method (IEdmEnumeratorCustomReference5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorCustomReference5"
member: "AddReference"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5~AddReference.html"
---

# AddReference Method (IEdmEnumeratorCustomReference5)

Obsolete. Superseded by [IEdmEnumeratorCustomReference6::AddReference2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference6~AddReference2.html).

## Syntax

### Visual Basic

```vb
Sub AddReference( _
   ByVal lFileID As System.Integer, _
   ByVal lFolderID As System.Integer _
)
```

### C#

```csharp
void AddReference(
   System.int lFileID,
   System.int lFolderID
)
```

### C++/CLI

```cpp
void AddReference(
   System.int lFileID,
   System.int lFolderID
)
```

### Parameters

- `lFileID`: ID of referenced file
- `lFolderID`: ID of parent folder of referenced file

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_FILE_NOT_LOCKED_BY_YOU: File is not checked out.

## See Also

[IEdmEnumeratorCustomReference5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5.html)
[IEdmEnumeratorCustomReference5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
