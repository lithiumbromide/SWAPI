---
title: "mlEdmAddFlags Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmAddFileInfo"
member: "mlEdmAddFlags"
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFileInfo~mlEdmAddFlags.html"
---

# mlEdmAddFlags Field

File add flags.

## Syntax

### Visual Basic

```vb
Public mlEdmAddFlags As System.Integer
```

### C#

```csharp
public System.int mlEdmAddFlags
```

### C++/CLI

```cpp
public:
System.int mlEdmAddFlags
```

### Field Value

Combination of [EdmAddFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFlag.html) bits. [IEdmFolder6::AddFiles](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder6~AddFiles.html) returns the HRESULT code for the file add in this member. The code is S_OK (0) if the file add is successful.

## See Also

[EdmAddFileInfo Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFileInfo.html)
[EdmAddFileInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFileInfo_members.html)
