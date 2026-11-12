---
title: "SetShowInBOM Method (IEdmEnumeratorCustomReference7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorCustomReference7"
member: "SetShowInBOM"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference7~SetShowInBOM.html"
---

# SetShowInBOM Method (IEdmEnumeratorCustomReference7)

Sets whether to show the specified file's user-defined file references in a BOM.

## Syntax

### Visual Basic

```vb
Sub SetShowInBOM( _
   ByVal lFileID As System.Integer, _
   ByVal lFolderID As System.Integer, _
   ByVal bShowInBOM As System.Boolean _
)
```

### C#

```csharp
void SetShowInBOM(
   System.int lFileID,
   System.int lFolderID,
   System.bool bShowInBOM
)
```

### C++/CLI

```cpp
void SetShowInBOM(
   System.int lFileID,
   System.int lFolderID,
   System.bool bShowInBOM
)
```

### Parameters

- `lFileID`: ID of referenced file
- `lFolderID`: ID of parent folder of referenced file
- `bShowInBOM`: True to show the specified file's user-defined file references in a BOM, false to not

## See Also

[IEdmEnumeratorCustomReference7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference7.html)
[IEdmEnumeratorCustomReference7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference7_members.html)
[IEdmEnumeratorCustomReference7::GetShowInBOM Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference7~GetShowInBOM.html)

## Availability

SOLIDWORKS PDM Professional 2017
