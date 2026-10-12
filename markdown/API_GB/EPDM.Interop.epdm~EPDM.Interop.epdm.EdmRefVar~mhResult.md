---
title: "mhResult Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRefVar"
member: "mhResult"
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar~mhResult.html"
---

# mhResult Field

Result of operation.

## Syntax

### Visual Basic

```vb
Public mhResult As System.Integer
```

### C#

```csharp
public System.int mhResult
```

### C++/CLI

```cpp
public:
System.int mhResult
```

## Remarks

All errors that can be returned on a file level by [IEdmBatchRefVars::GetRefVars](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars~GetRefVars.html) and [IEdmBatchRefVars::SetRefVars](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars~SetRefVars.html) are returned here rather than failing the entire method call.

## See Also

[EdmRefVar Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar.html)
[EdmRefVar Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar_members.html)
