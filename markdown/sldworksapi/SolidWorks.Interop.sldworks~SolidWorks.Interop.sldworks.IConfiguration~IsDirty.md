---
title: "IsDirty Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "IsDirty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsDirty.html"
---

# IsDirty Method (IConfiguration)

Gets whether this configuration is dirty (i.e., needs to be updated).

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDirty() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Boolean

value = instance.IsDirty()
```

### C#

```csharp
System.bool IsDirty()
```

### C++/CLI

```cpp
System.bool IsDirty();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the configuration is dirty, false if not

## VBA Syntax

See [Configuration::IsDirty](ms-its:sldworksapivb6.chm::/sldworks~Configuration~IsDirty.html).

## Examples

[Are the Assembly Configurations Loaded (C#)](Are_the_Assembly_Configurations_Loaded_Example_CSharp.htm)
[Are the Assembly Configurations Loaded (VB.NET)](Are_the_Assembly_Configurations_Loaded_Example_VBNET.htm)
[Are the Assembly Configurations Loaded (VBA)](Are_the_Assembly_Configurations_Loaded_Example_VB.htm)

## Remarks

If the configuration is dirty, then you can update its date by:

1. [Activating the configuration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ShowConfiguration2.html).
2. [Saving the document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Save3.html) while the configuration is active.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::NeedsRebuild Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.html)
[IModelDoc2::GetSaveFlag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSaveFlag.html)
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
