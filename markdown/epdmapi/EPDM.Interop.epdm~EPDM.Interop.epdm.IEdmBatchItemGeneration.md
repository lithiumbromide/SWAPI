---
title: "IEdmBatchItemGeneration Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchItemGeneration"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration.html"
---

# IEdmBatchItemGeneration Interface

Allows you to generate items from a file structure.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBatchItemGeneration
```

### C#

```csharp
public interface IEdmBatchItemGeneration
```

### C++/CLI

```cpp
public interface class IEdmBatchItemGeneration
```

## Examples

See the [IEdmBatchItemGeneration2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration2.html) examples.

## Remarks

This interface:

- inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- is extended by [IEdmBatchItemGeneration2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration2.html) which allows you to generate stand-alone items without a file structure.

To create several items from files at once:

1. Access this interface by calling [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html), passing [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_BatchItemGeneration as a parameter.
2. Call [IEdmBatchItemGeneration::AddSelection](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~AddSelection.html) one or more times.
3. Call [IEdmBatchItemGeneration::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~CreateTree.html) to compute the file reference tree.
4. Optionally call [IEdmBatchItemGeneration::ShowDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~ShowDlg.html) to show an item dialog.
5. Call [IEdmBatchItemGeneration::GenerateItems](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~GenerateItems.html) to create the items.

See the [Programming Items](Items.htm) topic for more information.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmBatchItemGeneration Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
