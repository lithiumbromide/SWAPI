---
title: "Connect Method (IToolboxConfiguratorAddin)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "IToolboxConfiguratorAddin"
member: "Connect"
kind: "method"
source: "toolboxapi/SolidWorks.Interop.sldtoolboxconfigureaddin~SolidWorks.Interop.sldtoolboxconfigureaddin.IToolboxConfiguratorAddin~Connect.html"
---

# Connect Method (IToolboxConfiguratorAddin)

Connects to the Welcome to Toolbox Setup dialog.

## Syntax

### Visual Basic (Declaration)

```vb
Function Connect( _
   ByVal pTbcApplication As System.Object, _
   ByVal lCookie As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IToolboxConfiguratorAddin
Dim pTbcApplication As System.Object
Dim lCookie As System.Integer
Dim value As System.Boolean

value = instance.Connect(pTbcApplication, lCookie)
```

### C#

```csharp
System.bool Connect(
   System.object pTbcApplication,
   System.int lCookie
)
```

### C++/CLI

```cpp
System.bool Connect(
   System.Object^ pTbcApplication,
   System.int lCookie
)
```

### Parameters

- `pTbcApplication`: [IToolboxConfiguratorApplication](SOLIDWORKS.Interop.sldtoolboxconfigureaddin~SOLIDWORKS.Interop.sldtoolboxconfigureaddin.IToolBoxConfiguratorApplication.html)
- `lCookie`: Add-in ID

### Return Value

True if successful, false if not

## VBA Syntax

See [ToolboxConfiguratorAddin::Connect](ms-its:toolboxapivb6.chm::/ToolboxConfigurationApplicationLib~ToolboxConfiguratorAddin~Connect.html).

## See Also

[IToolboxConfiguratorAddin Interface](SolidWorks.Interop.sldtoolboxconfigureaddin~SolidWorks.Interop.sldtoolboxconfigureaddin.IToolboxConfiguratorAddin.html)
[IToolboxConfiguratorAddin Members](SolidWorks.Interop.sldtoolboxconfigureaddin~SolidWorks.Interop.sldtoolboxconfigureaddin.IToolboxConfiguratorAddin_members.html)
[IToolboxConfiguratorAddin::Disconnect Method](SolidWorks.Interop.sldtoolboxconfigureaddin~SolidWorks.Interop.sldtoolboxconfigureaddin.IToolboxConfiguratorAddin~Disconnect.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
