---
title: "IEdmEnumeratorVariable5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable5"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html"
---

# IEdmEnumeratorVariable5 Interface

Allows you to access the contents of a file or folder data card.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmEnumeratorVariable5
```

### C#

```csharp
public interface IEdmEnumeratorVariable5
```

### C++/CLI

```cpp
public interface class IEdmEnumeratorVariable5
```

## Examples

[Change Card Variables Add-in (VB.NET)](Change_Card_Variables_Addin_Example_VBNET.htm)
[Change Card Variables Add-in (C#)](Change_Card_Variables_Addin_Example_CSharp.htm)
[Set Part Number Using Default Serial Numbers (C#)](Set_Part_Number_Using_Default_Serial_Numbers_Example_CSharp.htm)
[Set Part Number Using Default Serial Numbers (VB.NET)](Set_Part_Number_Using_Default_Serial_Numbers_Example_VBNET.htm)

## Remarks

This interface:

- inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- is extended by [IEdmEnumeratorVariable6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable6.html) which adds the ability to read a variable directly from the database.

The IEdmEnumeratorVariable`n` interface is a pointer to a file. If this pointer is not released, then other operations on the file can fail with a sharing violation. The recommendation in SOLIDWORKS PDM Professional 2008 and later is to always call [IEdmEnumeratorVariable8::CloseFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable8~CloseFile.html) when you are finished updating a file to make it possible for other applications and API functions to access the file. This replaces the earlier work-around to explicitly clear IEdmEnumeratorVariable pointers (set them to Nothing in Visual Basic and call Marshal.ReleaseComObject in .NET).

IEdmEnumeratorVariable`n` interfaces on the following do not need calls to IEdmEnumeratorVariable8::CloseFile:

- folders (cast IEdmFolder5 to this interface)
- file data cards (for add-ins, this interface is stored in [EdmCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.html)::mpoExtra of the poCmd argument returned in IEdmAddIn5::OnCmd only when EdmCmd::meCmdType = [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_CardButton or EdmCmdType.EdmCmd_CardInput)

## Accessors

[IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html)

[IEdmFile5::GetEnumeratorVariable](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetEnumeratorVariable.html)

[IEdmFolder5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)

## See Also

[IEdmEnumeratorVariable5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
