---
title: "IEdmVault5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html"
---

# IEdmVault5 Interface

Allows you to access a file vault.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmVault5
```

### C#

```csharp
public interface IEdmVault5
```

### C++/CLI

```cpp
public interface class IEdmVault5
```

## Examples

[Destroy Deleted Files in Vault (C#)](Destroy_Deleted_Files_in_Vault_Example_CSharp.htm)
[Destroy Deleted Files in Vault (VB.NET)](Destroy_Deleted_Files_in_Vault_Example_VBNET.htm)
[Get and Set Folder Permissions (C#)](Get_and_Set_Folder_Permissions_Example_CSharp.htm)
[Get and Set Folder Permissions (VB.NET)](Get_and_Set_Folder_Permissions_Example_VBNET.htm)
[Traverse Folders and Files in Vault (C#)](Traverse_Folders_and_Files_in_Vault_Example_CSharp.htm)
[Traverse Folders and Files in Vault (VB.NET)](Traverse_Folders_and_Files_in_Vault_Example_VBNET.htm)
[Change Card Variables Add-in (VB.NET)](Change_Card_Variables_Addin_Example_VBNET.htm)
[Change Card Variables Add-in (C#)](Change_Card_Variables_Addin_Example_CSharp.htm)
[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#)](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)

## Remarks

This interface represents a SOLIDWORKS PDM Professional file vault. It is the highest-level interface within this API; most of the other interfaces in this API are retrieved from this interface either directly or indirectly.

[Standalone program](StandAloneApp.htm)s using this API should first declare and create an instance of this interface. Because interfaces are abstract definitions and not implementations, they cannot be created directly using the **New** keyword.

The type library includes a creatable class called EdmVault5, which implements the IEdmVault5 interface.

You can create an instance of the EdmVault5 class with the **New** keyword, and because this class implements the IEdmVault5 interface, you can reference it with the variable declared as IEdmVault5 interface type. By convention, interface names begin with an uppercase letter I. Once the IEdmVault5 interface object is created, most of the other interface objects within this API are returned either directly or indirectly by methods and properties of the IEdmVault5 object or some other object that originated from it. Add-in programs are passed an IEdmVault5 object when the add-in is loaded and when needed.

To access this interface, stand-alone programs can:

- Obtain an instance through one of the accessors.
- Create an instance:

```
Dim vault as EdmVault5
vault = new EdmVault5
```

After obtaining an instance, programs must call [IEdmVault5::Login](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html) or [IEdmVault5::LoginAuto](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html) to establish a connection with the file vault.

This interface:

- inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- is extended by [IEdmVault6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault6.html).

## Accessors

[IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html)

[IEdmFile5::Vault](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~Vault.html)

[IEdmFolder5::Vault](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~Vault.html)

[IEdmObject5::Vault](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5~Vault.html)

## See Also

[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
