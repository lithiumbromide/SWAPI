---
title: "IEdmObject5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmObject5"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html"
---

# IEdmObject5 Interface

Contains several properties and methods that are common to all derived interfaces.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmObject5
```

### C#

```csharp
public interface IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmObject5
```

## Examples

[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)

## Remarks

Almost all objects that are stored in SOLIDWORKS PDM Professional's database inherit from this parent interface. See [EmdObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectInfo.html) for a list of all of the interfaces that inherit from IEdmObject5.

You can retrieve all objects inheriting from IEdmObject5 using [IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html) if you know the type and the database ID.

This interface inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).

## Accessors

[IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html)

## See Also

[IEdmObject5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
