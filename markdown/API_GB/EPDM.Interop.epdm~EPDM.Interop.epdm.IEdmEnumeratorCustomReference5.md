---
title: "IEdmEnumeratorCustomReference5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorCustomReference5"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5.html"
---

# IEdmEnumeratorCustomReference5 Interface

Allows you to access custom file references.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmEnumeratorCustomReference5
```

### C#

```csharp
public interface IEdmEnumeratorCustomReference5
```

### C++/CLI

```cpp
public interface class IEdmEnumeratorCustomReference5
```

## Examples

[Access Custom File References (VB.NET)](Access_Custom_File_References_Example_VBNET.htm)
[Access Custom File References (C#)](Access_Custom_File_References_Example_CSharp.htm)

## Remarks

This interface:

- inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- is extended by [IEdmEnumeratorCustomReference6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference6.html) which adds the ability to specify or get the number of times that a file is referenced by this file.

To use this interface:

1. Get the file to which you want to add references from the vault using [IEdmVault5::GetFileFromPath](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetFileFromPath.html).
2. Cast the [IEdmFile5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html) object returned in step 1 to IEdmEnumeratorCustomReference5.
3. Get a pointer to the file reference using IEdmVault5::GetFileFromPath.
4. Call [IEdmEnumeratorCustomReference::AddReference](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5~AddReference.html) to add the file reference in step 3 to the file in step 1.

In the SOLIDWORKS PDM Professional user interface, you handle file references in the Contains page of the Properties dialog box. Using the API, you can perform the same file reference tasks that you do in the user interface, for example, adding, removing, and viewing file references. File references can be checked in like any other file in SOLIDWORKS PDM Professional.

## See Also

[IEdmEnumeratorCustomReference5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
