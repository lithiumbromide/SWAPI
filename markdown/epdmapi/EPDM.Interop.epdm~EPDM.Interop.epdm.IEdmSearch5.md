---
title: "IEdmSearch5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch5"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.html"
---

# IEdmSearch5 Interface

Allows you to quickly find files or folders.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmSearch5
```

### C#

```csharp
public interface IEdmSearch5
```

### C++/CLI

```cpp
public interface class IEdmSearch5
```

## Examples

[Create a Task that Finds Approved Files (VB.NET)](Schedule_Task_Addin_Example_VBNET.htm)
[Create a Task that Finds Approved Files (C#)](Schedule_Task_Addin_Example_CSharp.htm)

## Remarks

This interface:

- inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- is extended by [IEdmSearch6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch6.html).

There is a bit of overhead involved in creating an IEdmSearch5 object, so if you intend to perform several searches, call [IEdmSearch5::Clear](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~Clear.html) to clear and re-use the current search object instead of calling [IEdmVault5::CreateSearch](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~CreateSearch.html) to create new search objects.

## Accessors

[IEdmVault5::CreateSearch](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~CreateSearch.html)

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmSearch5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
