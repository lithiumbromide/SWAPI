---
title: "IEdmAddCustomRefs3 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddCustomRefs3"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs3.html"
---

# IEdmAddCustomRefs3 Interface

Allows you to create or manage user-defined file references.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmAddCustomRefs3
   Inherits IEdmAddCustomRefs, IEdmAddCustomRefs2
```

### C#

```csharp
public interface IEdmAddCustomRefs3 : IEdmAddCustomRefs, IEdmAddCustomRefs2
```

### C++/CLI

```cpp
public interface class IEdmAddCustomRefs3 : public IEdmAddCustomRefs, IEdmAddCustomRefs2
```

## Remarks

This interface extends [IEdmAddCustomRefs2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs2.html).

To manage existing references:

1. Create IEdmAddCustomRefs3 using [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html).
2. Call [IEdmAddCustomRefs3::ShowEditReferencesDlg2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs3~ShowEditReferencesDlg2.html) to display existing file references.

To create new references:

1. Create IEdmAddCustomRefs2 using [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html).
2. Call [IEdmAddCustomRefs::AddReferencesClipboard](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~AddReferencesClipboard.html), [IEdmAddCustomRefs2::AddReferencesID2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs2~AddReferencesID2.html), or [IEdmAddCustomRefs2::AddReferencesPath2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs2~AddReferencesPath2.html) to add file references.
3. (Optional) Call [IEdmAddCustomRefs::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~CreateTree.html) and [IEdmAddCustomRefs::ShowDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~ShowDlg.html) to display the file references.
4. Call [IEdmAddCustomRefs::CreateReferences](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~CreateReferences.html) to create the new references.

## See Also

[IEdmAddCustomRefs3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs3_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
