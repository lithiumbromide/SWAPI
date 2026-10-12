---
title: "IEdmLabel5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmLabel5"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5.html"
---

# IEdmLabel5 Interface

Allows you to access a file or folder label.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmLabel5
   Inherits IEdmObject5
```

### C#

```csharp
public interface IEdmLabel5 : IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmLabel5 : public IEdmObject5
```

## Examples

[Create Labels on Folders (VB.NET)](Create_Label_Example_VBNET.htm)
[Create Labels on Folders (C#)](Create_Label_Example_CSharp.htm)

## Remarks

This interface:

- inherits from [IEdmObject5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html).
- is extended by [IEdmLabel6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel6.html) which provides the ability to update the history of, delete, and rename file labels.

## Accessors

[IEdmEnumeratorVersion5::GetNextLabel](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetNextLabel.html)

[IEdmFolder5::GetNextLabel](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetNextLabel.html)

[IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html)

## See Also

[IEdmLabel5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmFile16::CreateLabel Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile16~CreateLabel.html)
[IEdmFolder5::CreateLabel Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CreateLabel.html)
