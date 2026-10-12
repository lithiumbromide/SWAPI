---
title: "GetNumberOfExplodeSteps Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetNumberOfExplodeSteps"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfExplodeSteps.html"
---

# GetNumberOfExplodeSteps Method (IConfiguration)

Gets the number of explode steps for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNumberOfExplodeSteps() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Integer

value = instance.GetNumberOfExplodeSteps()
```

### C#

```csharp
System.int GetNumberOfExplodeSteps()
```

### C++/CLI

```cpp
System.int GetNumberOfExplodeSteps();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of explode steps on this configuration

## VBA Syntax

See [Configuration::GetNumberOfExplodeSteps](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetNumberOfExplodeSteps.html).

## Remarks

Call this method before calling [IConfiguration::GetExplodeStep](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetExplodeStep.html) or [IConfiguration::IGetExplodeStep](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IGetExplodeStep.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::AddExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep.html)
[IConfiguration::DeleteExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteExplodeStep.html)
[IConfiguration::IAddExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IAddExplodeStep.html)
[IConfiguration::AddRadialExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRadialExplodeStep.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
