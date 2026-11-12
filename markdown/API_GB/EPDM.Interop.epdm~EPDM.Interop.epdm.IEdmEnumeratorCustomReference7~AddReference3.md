---
title: "AddReference3 Method (IEdmEnumeratorCustomReference7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorCustomReference7"
member: "AddReference3"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference7~AddReference3.html"
---

# AddReference3 Method (IEdmEnumeratorCustomReference7)

Adds a custom file reference to this file.

## Syntax

### Visual Basic

```vb
Sub AddReference3( _
   ByVal lFileID As System.Integer, _
   ByVal lFolderID As System.Integer, _
   ByVal lQuantity As System.Integer, _
   Optional ByVal bShowInBOM As System.Boolean _
)
```

### C#

```csharp
void AddReference3(
   System.int lFileID,
   System.int lFolderID,
   System.int lQuantity,
   System.bool bShowInBOM
)
```

### C++/CLI

```cpp
void AddReference3(
   System.int lFileID,
   System.int lFolderID,
   System.int lQuantity,
   System.bool bShowInBOM
)
```

### Parameters

- `lFileID`: ID of referenced file
- `lFolderID`: ID of parent folder of referenced file
- `lQuantity`: Number of times the referenced file is referenced
- `bShowInBOM`: True to show this file reference in the BOM, false to not

## Examples

See the [IEdmEnumeratorCustomReference7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference7.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_FILE_NOT_LOCKED_BY_YOU: File is not checked out.

## See Also

[IEdmEnumeratorCustomReference7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference7.html)
[IEdmEnumeratorCustomReference7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference7_members.html)

## Availability

SOLIDWORKS PDM Professional 2017
