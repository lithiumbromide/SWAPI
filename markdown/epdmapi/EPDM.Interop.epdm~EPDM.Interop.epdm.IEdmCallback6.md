---
title: "IEdmCallback6 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCallback6"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6.html"
---

# IEdmCallback6 Interface

Monitors the progress of a supported API operation.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmCallback6
```

### C#

```csharp
public interface IEdmCallback6
```

### C++/CLI

```cpp
public interface class IEdmCallback6
```

## Examples

[Add Files to Vault (VB.NET)](Add_Files_to_Vault_Example_VBNET.htm)
[Add Files to Vault (C#)](Add_Files_to_Vault_Example_CSharp.htm)

## Remarks

This interface inherits from IUnknown. See [Using and Implementing IUnknown (COM)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms693423(v=vs.85).aspx).

This callback interface works only with methods that provide a poCallback argument. For example:

- [IEdmFolder6::AddFiles](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder6~AddFiles.html)
- [IEdmBatchAdd::CommitAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd~CommitAdd.html)

To use this interface:

1. Create a new class.
2. Implement all of the methods of IEdmCallback6 in the new class.
3. Call one of the methods whose progress you want to monitor, setting its poCallback argument to a pointer to the new class.

## See Also

[IEdmCallback6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
