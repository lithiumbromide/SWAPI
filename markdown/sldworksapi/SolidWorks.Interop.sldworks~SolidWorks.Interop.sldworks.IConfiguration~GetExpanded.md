---
title: "GetExpanded Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetExpanded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetExpanded.html"
---

# GetExpanded Method (IConfiguration)

Gets whether this configuration's node is expanded in the specified pane of the ConfigurationManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExpanded( _
   ByVal WhichPane As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim WhichPane As System.Integer
Dim value As System.Boolean

value = instance.GetExpanded(WhichPane)
```

### C#

```csharp
System.bool GetExpanded(
   System.int WhichPane
)
```

### C++/CLI

```cpp
System.bool GetExpanded(
   System.int WhichPane
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichPane`: Valid options in [swFeatMgrPane_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatMgrPane_e.html):

  - swFeatMgrPaneTop
  - swFeatMgrPaneBottom

### Return Value

True if node is expanded, false if not

## VBA Syntax

See [Configuration::GetExpanded](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetExpanded.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::SetExpanded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetExpanded.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
