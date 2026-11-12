---
title: "IEdmData Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmData"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmData.html"
---

# IEdmData Interface

Allows you to access the properties of an object created by a template.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmData
```

### C#

```csharp
public interface IEdmData
```

### C++/CLI

```cpp
public interface class IEdmData
```

## Examples

[Execute Template and Return Data (VB.NET)](Execute_Template_2_Example_VBNET.htm)
[Execute Template and Return Data (C#)](Execute_Template_2_Example_CSharp.htm)

## Remarks

This interface inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).

[IEdmTemplate53::RunEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate53~RunEx.html) executes a template to create one or more files or folders. It returns an array of these interfaces, one for each file or folder, in its ppoRetData parameter.

## Accessors

[IEdmTemplate53::RunEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate53~RunEx.html)

## See Also

[IEdmData Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmData_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
