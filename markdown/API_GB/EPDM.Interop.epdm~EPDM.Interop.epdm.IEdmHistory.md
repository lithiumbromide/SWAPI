---
title: "IEdmHistory Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistory"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory.html"
---

# IEdmHistory Interface

Allows you to access the history listing of files or folders.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmHistory
```

### C#

```csharp
public interface IEdmHistory
```

### C++/CLI

```cpp
public interface class IEdmHistory
```

## Examples

[Get Histories of Files (VB.NET)](Get_Histories_of_Files_Example_VBNET.htm)
[Get Histories of Files (C#)](Get_Histories_of_Files_Example_CSharp.htm)

## Remarks

This interface:

- inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- is extended by [IEdmHistory2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory2.html).

To access this interface, call [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html) with eType set to [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_History.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmHistory Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
