---
title: "GetActiveDisplayPane Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetActiveDisplayPane"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetActiveDisplayPane.html"
---

# GetActiveDisplayPane Method (ISldWorks)

Gets the active Display Pane.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetActiveDisplayPane() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Integer

value = instance.GetActiveDisplayPane()
```

### C#

```csharp
System.int GetActiveDisplayPane()
```

### C++/CLI

```cpp
System.int GetActiveDisplayPane();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Active display pane as defined by

[swDisplayPaneIndex_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDisplayPaneIndex_e.html)

## VBA Syntax

See

[SldWorks::GetActiveDisplayPane](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetActiveDisplayPane.html)

.

## Examples

[Create Task Pane View Add-in (C#)](Create_TaskPaneView_Add-in_Example_CSharp.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)

[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

[IModelDocExtension::IsDisplayPaneVisible Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsDisplayPaneVisible.html)

## Availability

SOLIDWORKS 2024 SP02, Revision Number 32.2
