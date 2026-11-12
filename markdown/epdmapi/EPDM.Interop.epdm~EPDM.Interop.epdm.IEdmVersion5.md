---
title: "IEdmVersion5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVersion5"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5.html"
---

# IEdmVersion5 Interface

Allows you to access the version of a file.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmVersion5
```

### C#

```csharp
public interface IEdmVersion5
```

### C++/CLI

```cpp
public interface class IEdmVersion5
```

## Examples

[Get Revision Names for Local Version of File (C#)](Get_Revision_Names_for_Local_Version_of_File_Example_CSharp.htm)
[Get Revision Names for Local Version of File (VB.NET)](Get_Revision_Names_for_Local_Version_of_File_Example_VBNET.htm)

## Remarks

This interface:

- inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- is extended by [IEdmVersion6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion6.html).

Whenever a new or modified file is checked in, a new version of it is created and stored in the file vault. The versions are denoted by numbers, e.g., 1,2,3, etc.

## Accessors

[IEdmEnumeratorVersion5::GetNextVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetNextVersion.html)

[IEdmEnumeratorVersion5::GetVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetVersion.html)

[IEdmRevision5::Version](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision5~Version.html)

## See Also

[IEdmVersion5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
