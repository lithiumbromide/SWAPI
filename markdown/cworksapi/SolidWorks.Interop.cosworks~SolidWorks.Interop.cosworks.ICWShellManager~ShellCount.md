---
title: "ShellCount Property (ICWShellManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShellManager"
member: "ShellCount"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager~ShellCount.html"
---

# ShellCount Property (ICWShellManager)

Gets the number of shells in the study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ShellCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShellManager
Dim value As System.Integer

value = instance.ShellCount
```

### C#

```csharp
System.int ShellCount {get;}
```

### C++/CLI

```cpp
property System.int ShellCount {
   System.int get();
}
```

### Property Value

Number of shells in the study

## VBA Syntax

See [CWShellManager::ShellCount](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShellManager~ShellCount.html).

## See Also

[ICWShellManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager.html)
[ICWShellManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
