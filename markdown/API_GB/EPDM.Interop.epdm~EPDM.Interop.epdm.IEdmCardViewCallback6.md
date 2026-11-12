---
title: "IEdmCardViewCallback6 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardViewCallback6"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6.html"
---

# IEdmCardViewCallback6 Interface

Handles customized loading and saving of data in a card view.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmCardViewCallback6
```

### C#

```csharp
public interface IEdmCardViewCallback6
```

### C++/CLI

```cpp
public interface class IEdmCardViewCallback6
```

## Examples

[Create Custom Card View (VB.NET)](Create_Custom_Card_View_Example_VBNET.htm)
[Create Custom Card View (C#)](Create_Custom_Card_View_Example_CSharp.htm)

## Remarks

This interface inherits from IUnknown. See [Using and Implementing IUnknown (COM)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms693423(v=vs.85).aspx).

This callback interface allows you to customize how data is loaded and saved in a simple card view that is created using [IEdmVault10::CreateCardViewEx2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault10~CreateCardViewEx2.html). To use this callback interface:

1. Create a new class.
2. Implement all of the methods of IEdmCardViewCallback6 in the new class.
3. Call IEdmVault10::CreateCardViewEx2, setting poCallback to a pointer to the new class.

## See Also

[IEdmCardViewCallback6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
