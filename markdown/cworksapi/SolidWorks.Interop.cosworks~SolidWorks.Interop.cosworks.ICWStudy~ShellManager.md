---
title: "ShellManager Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "ShellManager"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ShellManager.html"
---

# ShellManager Property (ICWStudy)

Gets the shell manager.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ShellManager As CWShellManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWShellManager

value = instance.ShellManager
```

### C#

```csharp
CWShellManager ShellManager {get;}
```

### C++/CLI

```cpp
property CWShellManager^ ShellManager {
   CWShellManager^ get();
}
```

### Property Value

[Shell manager](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWShellManager.html)

## VBA Syntax

See [CWStudy::ShellManager](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~ShellManager.html).

## Examples

[Create Frequency Study with Mixed Mesh (C#)](Create_Frequency_Study_with_Mixed_Mesh_Example_CSharp.htm)
[Create Frequency Study with Mixed Mesh (VB.NET)](Create_Frequency_Study_with_Mixed_Mesh_Example_VBNET.htm)
[Create Frequency Study with Mixed Mesh (VBA)](Create_Frequency_Study_with_Mixed_Mesh_Example_VB.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
