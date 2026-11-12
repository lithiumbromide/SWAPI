---
title: "GetDefaultMaterial Method (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "GetDefaultMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~GetDefaultMaterial.html"
---

# GetDefaultMaterial Method (ICWShell)

Gets the CAD material of the shell.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDefaultMaterial() As CWMaterial
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim value As CWMaterial

value = instance.GetDefaultMaterial()
```

### C#

```csharp
CWMaterial GetDefaultMaterial()
```

### C++/CLI

```cpp
CWMaterial^ GetDefaultMaterial();
```

### Return Value

[Material](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMaterial.html)

## VBA Syntax

See [CWShell::GetDefaultMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~GetDefaultMaterial.html).

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)
[ICWShell::GetShellMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~GetShellMaterial.html)
[ICWShell::SetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetLibraryMaterial.html)
[ICWShell::SetShellMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetShellMaterial.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
