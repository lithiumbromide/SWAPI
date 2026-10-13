---
title: "GetNumberOfPartExplodeSteps Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetNumberOfPartExplodeSteps"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfPartExplodeSteps.html"
---

# GetNumberOfPartExplodeSteps Method (IConfiguration)

Gets the number of explode steps in the explode view of a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNumberOfPartExplodeSteps() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Integer

value = instance.GetNumberOfPartExplodeSteps()
```

### C#

```csharp
System.int GetNumberOfPartExplodeSteps()
```

### C++/CLI

```cpp
System.int GetNumberOfPartExplodeSteps();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of explode steps

## VBA Syntax

See [Configuration::GetNumberOfPartExplodeSteps](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetNumberOfPartExplodeSteps.html).

## Remarks

This method is valid only for the active configuration.

Before calling this method, call [IPartDoc::ShowExploded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ShowExploded.html) to activate the explode view of interest.

Call this method before calling [IConfiguration::GetPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetPartExplodeStep.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::AddPartExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddPartExplodeStep.html)
[IConfiguration::GetCurrentPartExplodeViewName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetCurrentPartExplodeViewName.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
