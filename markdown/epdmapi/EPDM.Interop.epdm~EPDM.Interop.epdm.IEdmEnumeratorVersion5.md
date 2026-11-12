---
title: "IEdmEnumeratorVersion5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVersion5"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5.html"
---

# IEdmEnumeratorVersion5 Interface

Allows you to access the versions and revisions of a file.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmEnumeratorVersion5
```

### C#

```csharp
public interface IEdmEnumeratorVersion5
```

### C++/CLI

```cpp
public interface class IEdmEnumeratorVersion5
```

## Examples

[Get File Version Information (C#)](Get_File_Version_Information_Example_CSharp.htm)
[Get File Version Information (VB.NET)](Get_File_Version_Information_Example_VBNET.htm)
[Get Revision Names for Local Version of File (C#)](Get_Revision_Names_for_Local_Version_of_File_Example_CSharp.htm)
[Get Revision Names for Local Version of File (VB.NET)](Get_Revision_Names_for_Local_Version_of_File_Example_VBNET.htm)

## Remarks

This interface inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).

To access this interface, cast an [IEdmFile5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html) object to this interface.

A new version of a file is created every time the file has been modified and checked in. Versions are denoted by numbers (1,2,3,..,N). In addition to versions, users can also set up revisions. Revisions are user-friendly names that can be set on versions of files.

This interface is extended by [IEdmEnumeratorVersion6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion6.html).

## See Also

[IEdmEnumeratorVersion5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
