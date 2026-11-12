---
title: "IEdmReference5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmReference5"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html"
---

# IEdmReference5 Interface

Allows you to enumerate referenced and referencing files and set up user-defined references.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmReference5
```

### C#

```csharp
public interface IEdmReference5
```

### C++/CLI

```cpp
public interface class IEdmReference5
```

## Examples

[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)

## Remarks

The interface:

- inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- is extended by [IEdmReference6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference6.html).

Some file types, such as files from AutoCAD, SOLIDWORKS, Microsoft Word, etc., can contain references to other files. Regardless of file type, you can also set up your own references using SOLIDWORKS PDM Professional's User Defined File References dialog box in file properties. SOLIDWORKS PDM Professional manages all of these references for you and they show up, for example, in the check-in dialog box in the form of a reference tree.

Using IEdmReference5, you can enumerate referenced files and referencing files. You can also set up user-defined references using IEdmReference5.

## Accessors

[IEdmFile5::GetReferenceTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetReferenceTree.html)

[IEdmReference5::GetNextChild](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetNextChild.html)

[IEdmReference5::GetNextParent](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetNextParent.html)

## See Also

[IEdmReference5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmReference7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference7.html)
[IEdmReference8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference8.html)
[IEdmReference9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference9.html)
