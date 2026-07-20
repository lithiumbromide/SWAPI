---
title: "IsDisplayPaneVisible Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IsDisplayPaneVisible"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsDisplayPaneVisible.html"
---

# IsDisplayPaneVisible Method (IModelDocExtension)

Gets whether the Display Pane is visible in this active document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDisplayPaneVisible() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

value = instance.IsDisplayPaneVisible()
```

### C#

```csharp
System.bool IsDisplayPaneVisible()
```

### C++/CLI

```cpp
System.bool IsDisplayPaneVisible();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

True if the Display Pane is visible, false if not

## VBA Syntax

See

[ModelDocExtension::IsDisplayPaneVisible](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IsDisplayPaneVisible.html)

.

## Examples

[Create Task Pane View Add-in (C#)](Create_TaskPaneView_Add-in_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

[ISldWorks::GetActiveDisplayPane Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetActiveDisplayPane.html)

## Availability

SOLIDWORKS 2024 SP02, Revision Number 32.2
