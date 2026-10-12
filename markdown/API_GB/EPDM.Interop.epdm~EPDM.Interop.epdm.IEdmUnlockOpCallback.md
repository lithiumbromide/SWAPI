---
title: "IEdmUnlockOpCallback Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUnlockOpCallback"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html"
---

# IEdmUnlockOpCallback Interface

Allows you to access information and gain control of [IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) operations.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmUnlockOpCallback
```

### C#

```csharp
public interface IEdmUnlockOpCallback
```

### C++/CLI

```cpp
public interface class IEdmUnlockOpCallback
```

## Examples

[Access Check-in Flags in Check out Dialog (C#)](Access_Check-in_Flags_in_Check_in_Dialog_Example_CSharp.htm)
[Access Check-in Flags in Check out Dialog (VB.NET)](Access_Check-in_Flags_in_Check_in_Dialog_Example_VBNET.htm)
[Prevent Admin from Checking In File (C#)](Prevent_Admin_from_Checking_In_File_Example_CSharp.htm)
[Prevent Admin from Checking In File (VB.NET)](Prevent_Admin_from_Checking_In_File_Example_VBNET.htm)

## Remarks

This interface inherits from IUnknown. See [Using and Implementing IUnknown (COM)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms693423(v=vs.85).aspx).

To use this callback interface:

1. Create a new class.
2. Implement all of the methods of this interface in the new class.
3. Call [IEdmBatchUnlock::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock~CreateTree.html) or [IEdmBatchUnlock::UnlockFiles](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock~UnlockFiles.html), setting poCallback to a pointer to the new class.

## See Also

[IEdmUnlockOpCallback Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
