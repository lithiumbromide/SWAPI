---
title: "EdmRevError Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRevError"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevError.html"
---

# EdmRevError Structure

Returned from [IEdmRevisionMgr::Commit](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr~Commit.html) if something goes wrong when incrementing the revision number on a file.

## Syntax

### Visual Basic

```vb
Public Structure EdmRevError
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmRevError : System.ValueType
```

### C++/CLI

```cpp
public value class EdmRevError : public System.ValueType
```

## Examples

struct EdmRevError{
integer [mlFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevError~mlFileID.html);
integer [mhError](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevError~mhError.html);
};

## Examples

[Set Initial Revision (VB.NET)](Set_Initial_Revision_Example_VBNET.htm)
[Set Initial Revision (C#)](Set_Initial_Revision_Example_CSharp.htm)

## See Also

[EdmRevError Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevError_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2007
