---
title: "IToolboxConfiguratorAddin Interface"
project: "SOLIDWORKS Toolbox Browser API"
interface: "IToolboxConfiguratorAddin"
member: ""
kind: "interface"
source: "toolboxapi/SolidWorks.Interop.sldtoolboxconfigureaddin~SolidWorks.Interop.sldtoolboxconfigureaddin.IToolboxConfiguratorAddin.html"
---

# IToolboxConfiguratorAddin Interface

Connects to the Toolbox Configurator (Welcome to Toolbox Setup dialog) when it is opened and disconnects from it when it is closed. **NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IToolboxConfiguratorAddin
```

### Visual Basic (Usage)

```vb
Dim instance As IToolboxConfiguratorAddin
```

### C#

```csharp
public interface IToolboxConfiguratorAddin
```

### C++/CLI

```cpp
public interface class IToolboxConfiguratorAddin
```

## VBA Syntax

See [ToolboxConfiguratorAddin](ms-its:toolboxapivb6.chm::/ToolboxConfigurationApplicationLib~ToolboxConfiguratorAddin.html).

## Examples

See [Getting Started](GettingStarted-toolboxapi.html) for more information.

## Remarks

This interface is available only if SOLIDWORKS Toolbox Browser is an active SOLIDWORKS add-in.

## Accessors

There is no functional need to access this interface. As this is a delegate to the Toolbox Configurator user interface, it automatically connects and disconnects as the Toolbox Configurator (Welcome to Toolbox Setup dialog) appears and disappears.

## See Also

[IToolboxConfiguratorAddin Members](SolidWorks.Interop.sldtoolboxconfigureaddin~SolidWorks.Interop.sldtoolboxconfigureaddin.IToolboxConfiguratorAddin_members.html)
[SolidWorks.Interop.sldtoolboxconfigureaddin Namespace](SolidWorks.Interop.sldtoolboxconfigureaddin~SolidWorks.Interop.sldtoolboxconfigureaddin_namespace.html)
