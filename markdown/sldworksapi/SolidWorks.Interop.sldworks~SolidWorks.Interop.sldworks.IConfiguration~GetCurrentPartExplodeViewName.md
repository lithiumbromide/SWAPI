---
title: "GetCurrentPartExplodeViewName Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetCurrentPartExplodeViewName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetCurrentPartExplodeViewName.html"
---

# GetCurrentPartExplodeViewName Method (IConfiguration)

Gets the explode view name in the current configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurrentPartExplodeViewName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.String

value = instance.GetCurrentPartExplodeViewName()
```

### C#

```csharp
System.string GetCurrentPartExplodeViewName()
```

### C++/CLI

```cpp
System.String^ GetCurrentPartExplodeViewName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Explode view name

## VBA Syntax

See [Configuration::GetCurrentPartExplodeViewName](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetCurrentPartExplodeViewName.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::AddPartExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddPartExplodeStep.html)
[IConfiguration::GetNumberOfPartExplodeSteps Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfPartExplodeSteps.html)
[IConfiguration::GetPartExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetPartExplodeStep.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
