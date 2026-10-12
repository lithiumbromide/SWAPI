---
title: "ShellEndEdit Method (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "ShellEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~ShellEndEdit.html"
---

# ShellEndEdit Method (ICWShell)

Ends editing a shell.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShellEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim value As System.Integer

value = instance.ShellEndEdit()
```

### C#

```csharp
System.int ShellEndEdit()
```

### C++/CLI

```cpp
System.int ShellEndEdit();
```

### Return Value

Error as defined [swsShellEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsShellEndEditError_e.html)

## VBA Syntax

See [CWShell::ShellEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~ShellEndEdit.html).

## Examples

[Create Frequency Study with Mixed Mesh (C#)](Create_Frequency_Study_with_Mixed_Mesh_Example_CSharp.htm)
[Create Frequency Study with Mixed Mesh (VB.NET)](Create_Frequency_Study_with_Mixed_Mesh_Example_VBNET.htm)
[Create Frequency Study with Mixed Mesh (VBA)](Create_Frequency_Study_with_Mixed_Mesh_Example_VB.htm)

## Remarks

You must call [ICWShell::ShellBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWShell~ShellBeginEdit.html) to start editing a shell. To end editing a shell, you must call this method. Changes are not applied unless you call both methods.

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
