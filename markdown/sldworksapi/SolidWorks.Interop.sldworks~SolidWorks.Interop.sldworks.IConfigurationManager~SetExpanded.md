---
title: "SetExpanded Method (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "SetExpanded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetExpanded.html"
---

# SetExpanded Method (IConfigurationManager)

Sets whether to display and expand all of the configuration nodes in the specified pane of the ConfigurationManager.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetExpanded( _
   ByVal WhichPane As System.Integer, _
   ByVal Expand As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim WhichPane As System.Integer
Dim Expand As System.Boolean

instance.SetExpanded(WhichPane, Expand)
```

### C#

```csharp
void SetExpanded(
   System.int WhichPane,
   System.bool Expand
)
```

### C++/CLI

```cpp
void SetExpanded(
   System.int WhichPane,
   System.bool Expand
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichPane`: Display pane as defined in [swFeatMgrPane_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatMgrPane_e.html):

  - swFeatMgrPaneTop
  - swFeatMgrPaneBottom
- `Expand`: True to expand all of the nodes, false to collapse them

## VBA Syntax

See [ConfigurationManager::SetExpanded](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~SetExpanded.html).

## Examples

[Work With Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)
[IConfiguration::SetExpanded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetExpanded.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
