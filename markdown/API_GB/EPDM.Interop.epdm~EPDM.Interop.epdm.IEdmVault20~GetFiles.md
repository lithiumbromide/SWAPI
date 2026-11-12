---
title: "GetFiles Method (IEdmVault20)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault20"
member: "GetFiles"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault20~GetFiles.html"
---

# GetFiles Method (IEdmVault20)

Gets the specified files in this vault.

## Syntax

### Visual Basic

```vb
Function GetFiles( _
   ByVal poDocsIDs() As EdmDocIDs _
) As System.Object()
```

### C#

```csharp
System.object[] GetFiles(
   EdmDocIDs[] poDocsIDs
)
```

### C++/CLI

```cpp
System.array<Object^>^ GetFiles(
   array<EdmDocIDs>^ poDocsIDs
)
```

### Parameters

- `poDocsIDs`: Array of [EdmDocIDs](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDocIDs.html)

### Return Value

Array of [IEdmFile5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)s

## See Also

[IEdmVault20 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault20.html)
[IEdmVault20 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault20_members.html)

## Availability

SOLIDWORKS PDM Professional 2019
