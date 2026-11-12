---
title: "IEdmFile6 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile6"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile6.html"
---

# IEdmFile6 Interface

Allows you to access a file in SOLIDWORKS PDM Professional.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmFile6
   Inherits IEdmFile5, IEdmObject5
```

### C#

```csharp
public interface IEdmFile6 : IEdmFile5, IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmFile6 : public IEdmFile5, IEdmObject5
```

## Examples

[Get File Information (VB.NET)](Get_File_Info_Example_VBNET.htm)
[Get File Information (C#)](Get_File_Info_Example_CSharp.htm)

## Remarks

This interface:

- inherits from [IEdmFile5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html).
- is extended by [IEdmFile7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7.html) which provides the ability to get computed and derived bills of materials and check whether a file needs to be rebuilt.

## See Also

[IEdmFile6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile6_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
