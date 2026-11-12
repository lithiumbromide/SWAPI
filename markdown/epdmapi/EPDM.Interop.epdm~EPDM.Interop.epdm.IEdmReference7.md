---
title: "IEdmReference7 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmReference7"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference7.html"
---

# IEdmReference7 Interface

Allows you to enumerate referenced and referencing files and set up user-defined references.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmReference7
   Inherits IEdmReference5, IEdmReference6
```

### C#

```csharp
public interface IEdmReference7 : IEdmReference5, IEdmReference6
```

### C++/CLI

```cpp
public interface class IEdmReference7 : public IEdmReference5, IEdmReference6
```

## Examples

[Get Parent References of File (VB.NET)](Get_Parent_References_Example_VBNET.htm)
[Get Parent References of File (C#)](Get_Parent_References_Example_CSharp.htm)

## Remarks

This interface:

- provides more control over which children or parent files to enumerate than earlier versions of this interface.
- inherits from [IEdmReference6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference6.html).
- is extended by [IEdmReference8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference8.html).

## See Also

[IEdmReference7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference7_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmReference5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html)
[IEdmReference9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference9.html)
