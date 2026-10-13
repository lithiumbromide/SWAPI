---
title: "mlLocalVersion Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmListFile"
member: "mlLocalVersion"
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile~mlLocalVersion.html"
---

# mlLocalVersion Field

Version of the file in the local cache, based on the date of the file passed to the [IEdmBatchListing::AddFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~AddFile.html) method.

## Syntax

### Visual Basic

```vb
Public mlLocalVersion As System.Integer
```

### C#

```csharp
public System.int mlLocalVersion
```

### C++/CLI

```cpp
public:
System.int mlLocalVersion
```

### Field Value

Version of the file in the local cache or 0 if the date of the version of the file in local cache passed to IEdmBatchListing::AddFile doesn’t match any version of the file in the vault

## See Also

[EdmListFile Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile.html)
[EdmListFile Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile_members.html)
