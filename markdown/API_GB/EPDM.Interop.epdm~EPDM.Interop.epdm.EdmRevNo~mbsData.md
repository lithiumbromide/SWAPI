---
title: "mbsData Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRevNo"
member: "mbsData"
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevNo~mbsData.html"
---

# mbsData Field

Format string as entered in the administration tool.

## Syntax

### Visual Basic

```vb
Public mbsData As System.String
```

### C#

```csharp
public System.string mbsData
```

### C++/CLI

```cpp
public:
System.String^ mbsData
```

## Remarks

The components are represented by escape sequences like this "%1n", "%2n"... where 1 and 2 are the database IDs of the components; i.e., the same as [EdmRevComponent's mlComponentID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent~mlComponentID.html) field.

## See Also

[EdmRevNo Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevNo.html)
[EdmRevNo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevNo_members.html)
