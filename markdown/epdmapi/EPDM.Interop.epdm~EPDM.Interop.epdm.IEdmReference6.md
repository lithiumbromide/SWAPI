---
title: "IEdmReference6 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmReference6"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference6.html"
---

# IEdmReference6 Interface

Allows you to enumerate referenced and referencing files and set up user-defined references.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmReference6
   Inherits IEdmReference5
```

### C#

```csharp
public interface IEdmReference6 : IEdmReference5
```

### C++/CLI

```cpp
public interface class IEdmReference6 : public IEdmReference5
```

## Remarks

The interface:

- inherits from [IEdmReference5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html).
- is extended by [IEdmReference7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference7.html).

Some file types, such as files from AutoCAD, SOLIDWORKS, Microsoft Word, etc., can contain references to other files. Regardless of file type, you can also set up your own references using SOLIDWORKS PDM Professional's User Defined File References dialog box in file properties. SOLIDWORKS PDM Professional manages all of these references for you and they show up, for example, in the check-in dialog box in the form of a reference tree.

Using IEdmReference5, you can enumerate referenced files and referencing files. You can also set up user-defined references using IEdmReference5.

## See Also

[IEdmReference6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference6_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmReference8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference8.html)
[IEdmReference9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference9.html)
