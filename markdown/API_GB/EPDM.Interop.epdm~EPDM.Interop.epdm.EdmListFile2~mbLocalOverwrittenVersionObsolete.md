---
title: "mbLocalOverwrittenVersionObsolete Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmListFile2"
member: "mbLocalOverwrittenVersionObsolete"
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2~mbLocalOverwrittenVersionObsolete.html"
---

# mbLocalOverwrittenVersionObsolete Field

Gets whether a file in a user's local cache is valid or obsolete because the file was overwritten by another user who checked out the file, modified the file, and checked in the file.

## Syntax

### Visual Basic

```vb
Public mbLocalOverwrittenVersionObsolete As System.Short
```

### C#

```csharp
public System.short mbLocalOverwrittenVersionObsolete
```

### C++/CLI

```cpp
public:
System.short mbLocalOverwrittenVersionObsolete
```

### Field Value

- 0 = file in the user’s local cache is valid

- 1 = file in the user’s local cache is obsolete

## See Also

[EdmListFile2 Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2.html)
[EdmListFile2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2_members.html)
