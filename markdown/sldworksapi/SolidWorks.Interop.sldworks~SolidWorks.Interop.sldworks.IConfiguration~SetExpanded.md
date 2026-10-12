---
title: "SetExpanded Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "SetExpanded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetExpanded.html"
---

# SetExpanded Method (IConfiguration)

Sets whether to expand this configuration's node in the specified pane of the ConfigurationManager.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetExpanded( _
   ByVal WhichPane As System.Integer, _
   ByVal Expanded As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim WhichPane As System.Integer
Dim Expanded As System.Boolean

instance.SetExpanded(WhichPane, Expanded)
```

### C#

```csharp
void SetExpanded(
   System.int WhichPane,
   System.bool Expanded
)
```

### C++/CLI

```cpp
void SetExpanded(
   System.int WhichPane,
   System.bool Expanded
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichPane`: Display pane as defined in [swFeatMgrPane_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatMgrPane_e.html):

  - swFeatMgrPaneTop
  - swFeatMgrPaneBottom
- `Expanded`: True to expand the node, false to collapse it

## VBA Syntax

See [Configuration::SetExpanded](ms-its:sldworksapivb6.chm::/sldworks~Configuration~SetExpanded.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::GetExpanded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetExpanded.html)
[IConfigurationManager::SetExpanded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetExpanded.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
