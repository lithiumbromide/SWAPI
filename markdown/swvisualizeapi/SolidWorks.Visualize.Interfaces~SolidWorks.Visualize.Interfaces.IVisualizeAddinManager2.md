---
title: "IVisualizeAddinManager2 Interface"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IVisualizeAddinManager2"
member: ""
kind: "interface"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2.html"
---

# IVisualizeAddinManager2 Interface

Allows access to the Visualize Addin Manager.
**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IVisualizeAddinManager2
   Inherits IVisualizeAddinManager
```

### Visual Basic (Usage)

```vb
Dim instance As IVisualizeAddinManager2
```

### C#

```csharp
public interface IVisualizeAddinManager2 : IVisualizeAddinManager
```

### C++/CLI

```cpp
public interface class IVisualizeAddinManager2 : public IVisualizeAddinManager
```

## VBA Syntax

See [IVisualizeAddinManager2](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IVisualizeAddinManager2.html).

## Examples

Read [Getting Started](GettingStarted.html) to learn about downloading an advanced Visualize C# plug-in from the API Support Knowledge Base.

## Remarks

This interface extends [IVisualizeAddinManager](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager.html) by adding the ability to:

- Launch Visualize with a project file
- Specify a grouping mode when saving a model to Visualize
- Render asynchronously with a callback handler

## Accessors

[IVisualizeAddin2::GetAddinManager2](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddin2~GetAddinManager2.html)

## See Also

[IVisualizeAddinManager2 Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2_members.html)
[SolidWorks.Visualize.Interfaces Namespace](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces_namespace.html)
