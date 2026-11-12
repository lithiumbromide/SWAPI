---
title: "IEdmAddCustomRefs Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddCustomRefs"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs.html"
---

# IEdmAddCustomRefs Interface

Allows you to create or manage user-defined file references.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmAddCustomRefs
```

### C#

```csharp
public interface IEdmAddCustomRefs
```

### C++/CLI

```cpp
public interface class IEdmAddCustomRefs
```

## Examples

[Add Custom File Reference (VB.NET)](Add_Custom_File_Reference_Example_VBNET.htm)
[Add Custom File Reference (C#)](Add_Custom_File_Reference_Example_CSharp.htm)

## Remarks

This interface:

- inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- is extended by [IEdmAddCustomRefs2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs2.html).

To manage existing references:

1. Create IEdmAddCustomRefs using [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html).
2. Call [IEdmAddCustomRefs::ShowEditReferencesDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~ShowEditReferencesDlg.html) to display the existing file references.

To create new references:

1. Create IEdmAddCustomRefs using [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html).
2. Call [IEdmAddCustomRefs::AddReferencesClipboard](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~AddReferencesClipboard.html), [IEdmAddCustomRefs::AddReferencesID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~AddReferencesID.html), or [IEdmAddCustomRefs::AddReferencesPath](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~AddReferencesPath.html) to add file references.
3. (Optional) Call [IEdmAddCustomRefs::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~CreateTree.html) and [IEdmAddCustomRefs::ShowDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~ShowDlg.html) to display the file references.
4. Call [IEdmAddCustomRefs::CreateReferences](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~CreateReferences.html) to create the new references.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmAddCustomRefs Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
