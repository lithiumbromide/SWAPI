---
title: "IEdmFile7 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile7"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7.html"
---

# IEdmFile7 Interface

Allows you to access a file in SOLIDWORKS PDM Professional.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmFile7
   Inherits IEdmFile5, IEdmFile6, IEdmObject5
```

### C#

```csharp
public interface IEdmFile7 : IEdmFile5, IEdmFile6, IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmFile7 : public IEdmFile5, IEdmFile6, IEdmObject5
```

## Examples

[Access Bill of Materials (VB.NET)](Access_Bill_of_Materials_Example_VBNET.htm)
[Access Bill of Materials (C#)](Access_Bill_of_Materials_Example_CSharp.htm)

## Remarks

This interface:

- inherits from [IEdmFile6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile6.html).
- is extended by [IEdmFile8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile8.html) which provides the ability to get the file type and update the file data card with default values when a new configuration is added by SOLIDWORKS.

To access an item in the vault, cast this interface's object to an [IEdmItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html).

## See Also

[IEdmFile7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
