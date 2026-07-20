---
title: "IEdmEnumeratorVariable8 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable8"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable8.html"
---

# IEdmEnumeratorVariable8 Interface

Allows you to access the contents of a file data card.

NOTE:

Click the

Members

link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmEnumeratorVariable8
   Inherits IEdmEnumeratorVariable5, IEdmEnumeratorVariable6, IEdmEnumeratorVariable7
```

### C#

```csharp
public interface IEdmEnumeratorVariable8 : IEdmEnumeratorVariable5, IEdmEnumeratorVariable6, IEdmEnumeratorVariable7
```

### C++/CLI

```cpp
public interface class IEdmEnumeratorVariable8 : public IEdmEnumeratorVariable5, IEdmEnumeratorVariable6, IEdmEnumeratorVariable7
```

## Examples

[Set Part Number Using Default Serial Numbers (C#)](Set_Part_Number_Using_Default_Serial_Numbers_Example_CSharp.htm)

[Set Part Number Using Default Serial Numbers (VB.NET)](Set_Part_Number_Using_Default_Serial_Numbers_Example_VBNET.htm)

## Remarks

This interface:

- extends

  [IEdmEnumeratorVariable7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable7.html)

  by providing the ability to close the file.
- does not support folder data cards. Use

  [IEdmEnumeratorVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html)

  and

  [IEdmEnumeratorVariable6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable6.html)

  for folder data cards.
- is extended by

  [IEdmEnumeratorVariable9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable9.html)

  .

See the**Remarks**for[IEdmEnumeratorVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html).

If you want to update variables in several files or folders, use[IEdmBatchUpdate2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2.html), which is more efficient than this interface.

## See Also

[IEdmEnumeratorVariable8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable8_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
