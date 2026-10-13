---
title: "RemoveReference Method (IEdmEnumeratorCustomReference5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorCustomReference5"
member: "RemoveReference"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5~RemoveReference.html"
---

# RemoveReference Method (IEdmEnumeratorCustomReference5)

Removes the specified custom file reference from this file.

## Syntax

### Visual Basic

```vb
Sub RemoveReference( _
   ByVal lFileID As System.Integer, _
   ByVal lFolderID As System.Integer _
)
```

### C#

```csharp
void RemoveReference(
   System.int lFileID,
   System.int lFolderID
)
```

### C++/CLI

```cpp
void RemoveReference(
   System.int lFileID,
   System.int lFolderID
)
```

### Parameters

- `lFileID`: ID of file to remove
- `lFolderID`: ID of the file's parent folder

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_FILE_NOT_LOCKED_BY_YOU: The file is not checked out.

## See Also

[IEdmEnumeratorCustomReference5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5.html)
[IEdmEnumeratorCustomReference5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
