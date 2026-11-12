---
title: "ShellBeginEdit Method (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "ShellBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~ShellBeginEdit.html"
---

# ShellBeginEdit Method (ICWShell)

Starts editing the shell.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShellBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell

instance.ShellBeginEdit()
```

### C#

```csharp
void ShellBeginEdit()
```

### C++/CLI

```cpp
void ShellBeginEdit();
```

## VBA Syntax

See [CWShell::ShellBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~ShellBeginEdit.html).

## Examples

[Create Frequency Study with Mixed Mesh (C#)](Create_Frequency_Study_with_Mixed_Mesh_Example_CSharp.htm)
[Create Frequency Study with Mixed Mesh (VB.NET)](Create_Frequency_Study_with_Mixed_Mesh_Example_VBNET.htm)
[Create Frequency Study with Mixed Mesh (VBA)](Create_Frequency_Study_with_Mixed_Mesh_Example_VB.htm)

## Remarks

To start editing a shell, you must call this method. You must call [ICWShell::ShellEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWShell~ShellEndEdit.html) to end editing a shell. Changes are not applied unless you call both methods.

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
