---
title: "SendMessageToUser Method (IToolBoxConfiguratorApplication)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "IToolBoxConfiguratorApplication"
member: "SendMessageToUser"
kind: "method"
source: "toolboxapi/SolidWorks.Interop.sldtoolboxconfigureaddin~SolidWorks.Interop.sldtoolboxconfigureaddin.IToolBoxConfiguratorApplication~SendMessageToUser.html"
---

# SendMessageToUser Method (IToolBoxConfiguratorApplication)

Prompts the user with the specified message.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SendMessageToUser( _
   ByVal message As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IToolBoxConfiguratorApplication
Dim message As System.String

instance.SendMessageToUser(message)
```

### C#

```csharp
void SendMessageToUser(
   System.string message
)
```

### C++/CLI

```cpp
void SendMessageToUser(
   System.String^ message
)
```

### Parameters

- `message`: Message string

## VBA Syntax

See [ToolBoxConfiguratorApplication::SendMessageToUser](ms-its:toolboxapivb6.chm::/ToolboxConfigurationApplicationLib~CTbcApplication~SendMessageToUser.html).

## See Also

[IToolBoxConfiguratorApplication Interface](SolidWorks.Interop.sldtoolboxconfigureaddin~SolidWorks.Interop.sldtoolboxconfigureaddin.IToolBoxConfiguratorApplication.html)
[IToolBoxConfiguratorApplication Members](SolidWorks.Interop.sldtoolboxconfigureaddin~SolidWorks.Interop.sldtoolboxconfigureaddin.IToolBoxConfiguratorApplication_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
