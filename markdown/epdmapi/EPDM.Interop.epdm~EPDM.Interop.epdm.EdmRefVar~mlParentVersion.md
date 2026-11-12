---
title: "mlParentVersion Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRefVar"
member: "mlParentVersion"
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar~mlParentVersion.html"
---

# mlParentVersion Field

Version of parent file (assembly).

## Syntax

### Visual Basic

```vb
Public mlParentVersion As System.Integer
```

### C#

```csharp
public System.int mlParentVersion
```

### C++/CLI

```cpp
public:
System.int mlParentVersion
```

## Remarks

This member is ignored during write operations, because only the latest version can be updated. Read operations interpret the value, 0, as the latest version.

## See Also

[EdmRefVar Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar.html)
[EdmRefVar Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar_members.html)
