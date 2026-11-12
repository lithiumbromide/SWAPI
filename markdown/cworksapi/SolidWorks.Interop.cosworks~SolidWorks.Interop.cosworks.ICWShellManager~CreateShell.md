---
title: "CreateShell Method (ICWShellManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShellManager"
member: "CreateShell"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager~CreateShell.html"
---

# CreateShell Method (ICWShellManager)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateShell( _
   ByVal DispArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShellManager
Dim DispArray As System.Object
Dim value As System.Integer

value = instance.CreateShell(DispArray)
```

### C#

```csharp
System.int CreateShell(
   System.object DispArray
)
```

### C++/CLI

```cpp
System.int CreateShell(
   System.Object^ DispArray
)
```

### Parameters

- `DispArray`: Array of entities (faces or reference surfaces) to use to create the shell

### Return Value

Error as defined in [swsShellManagerError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsShellManagerError_e.html)

## VBA Syntax

See [CWShellManager::CreateShell](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShellManager~CreateShell.html).

## See Also

[ICWShellManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager.html)
[ICWShellManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager_members.html)
[ICWShellManager::DeleteShell Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager~DeleteShell.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
