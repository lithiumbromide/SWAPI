---
title: "IEdmSearch8 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch8"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8.html"
---

# IEdmSearch8 Interface

Allows you to quickly find files or folders.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmSearch8
   Inherits IEdmSearch5, IEdmSearch6, IEdmSearch7
```

### C#

```csharp
public interface IEdmSearch8 : IEdmSearch5, IEdmSearch6, IEdmSearch7
```

### C++/CLI

```cpp
public interface class IEdmSearch8 : public IEdmSearch5, IEdmSearch6, IEdmSearch7
```

## Examples

[Create a Task that Finds Approved Files (VB.NET)](Schedule_Task_Addin_Example_VBNET.htm)
[Create a Task that Finds Approved Files (C#)](Schedule_Task_Addin_Example_CSharp.htm)

## Remarks

This interface:

- extends [IEdmSearch7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch7.html) by providing the ability to construct more complicated search criteria using:

  - Comparison operators
  - Boolean OR and AND

- is extended by [IEdmSearch9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9.html).

## See Also

[IEdmSearch8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
