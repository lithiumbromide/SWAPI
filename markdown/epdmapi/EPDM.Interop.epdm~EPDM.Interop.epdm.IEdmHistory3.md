---
title: "IEdmHistory3 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistory3"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3.html"
---

# IEdmHistory3 Interface

Allows you to access the sorted history listing of files or folders.

NOTE:

Click the

Members

link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmHistory3
   Inherits IEdmHistory, IEdmHistory2
```

### C#

```csharp
public interface IEdmHistory3 : IEdmHistory, IEdmHistory2
```

### C++/CLI

```cpp
public interface class IEdmHistory3 : public IEdmHistory, IEdmHistory2
```

## Examples

[Get Histories of Files (VB.NET)](Get_Histories_of_Files_Example_VBNET.htm)

[Get Histories of Files (C#)](Get_Histories_of_Files_Example_CSharp.htm)

## Remarks

This interface:

- extends

  [IEdmHistory2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory2.html)

  by providing:

- is extended by

  [IEdmHistory4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory4.html)

  .

To access this interface, call[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)with eType set to[EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_History.

## Accessors

IEdmVault7::CreateUtility

## See Also

[IEdmHistory3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
