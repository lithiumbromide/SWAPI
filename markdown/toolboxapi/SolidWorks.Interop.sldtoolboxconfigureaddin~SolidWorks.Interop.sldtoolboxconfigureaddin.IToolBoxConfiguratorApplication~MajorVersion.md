---
title: "MajorVersion Property (IToolBoxConfiguratorApplication)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "IToolBoxConfiguratorApplication"
member: "MajorVersion"
kind: "property"
source: "toolboxapi/SolidWorks.Interop.sldtoolboxconfigureaddin~SolidWorks.Interop.sldtoolboxconfigureaddin.IToolBoxConfiguratorApplication~MajorVersion.html"
---

# MajorVersion Property (IToolBoxConfiguratorApplication)

Gets the major version of the Welcome to Toolbox Setup dialog.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MajorVersion As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IToolBoxConfiguratorApplication
Dim value As System.Integer

value = instance.MajorVersion
```

### C#

```csharp
System.int MajorVersion {get;}
```

### C++/CLI

```cpp
property System.int MajorVersion {
   System.int get();
}
```

### Property Value

Major version of the Welcome to Toolbox Setup dialog

## VBA Syntax

See [ToolBoxConfiguratorApplication::MajorVersion](ms-its:toolboxapivb6.chm::/ToolboxConfigurationApplicationLib~CTbcApplication~MajorVersion.html).

## See Also

[IToolBoxConfiguratorApplication Interface](SolidWorks.Interop.sldtoolboxconfigureaddin~SolidWorks.Interop.sldtoolboxconfigureaddin.IToolBoxConfiguratorApplication.html)
[IToolBoxConfiguratorApplication Members](SolidWorks.Interop.sldtoolboxconfigureaddin~SolidWorks.Interop.sldtoolboxconfigureaddin.IToolBoxConfiguratorApplication_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
