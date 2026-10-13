---
title: "GetShellAt Method (ICWShellManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShellManager"
member: "GetShellAt"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager~GetShellAt.html"
---

# GetShellAt Method (ICWShellManager)

Gets the shell at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetShellAt( _
   ByVal NIndex As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As CWShell
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShellManager
Dim NIndex As System.Integer
Dim ErrorCode As System.Integer
Dim value As CWShell

value = instance.GetShellAt(NIndex, ErrorCode)
```

### C#

```csharp
CWShell GetShellAt(
   System.int NIndex,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWShell^ GetShellAt(
   System.int NIndex,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NIndex`: 0-based index of shell to get
- `ErrorCode`: 0 if the shell is returned, 1 if not

### Return Value

[Shell](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWShell.html)

## VBA Syntax

See [CWShellManager::GetShellAt](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShellManager~GetShellAt.html).

## Examples

[Create Frequency Study with Mixed Mesh (C#)](Create_Frequency_Study_with_Mixed_Mesh_Example_CSharp.htm)
[Create Frequency Study with Mixed Mesh (VB.NET)](Create_Frequency_Study_with_Mixed_Mesh_Example_VBNET.htm)
[Create Frequency Study with Mixed Mesh (VBA)](Create_Frequency_Study_with_Mixed_Mesh_Example_VB.htm)

## Remarks

Before calling this method, call [ICWShellManager::ShellCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWShellManager~ShellCount.html) to get NIndex.

## See Also

[ICWShellManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager.html)
[ICWShellManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
