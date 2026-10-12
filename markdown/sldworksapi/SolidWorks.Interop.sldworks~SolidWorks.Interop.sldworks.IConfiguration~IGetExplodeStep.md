---
title: "IGetExplodeStep Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "IGetExplodeStep"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetExplodeStep.html"
---

# IGetExplodeStep Method (IConfiguration)

Gets a pointer to the specified explode step in the configuration explode step sequence.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetExplodeStep( _
   ByVal ExplodeStepIndex As System.Integer _
) As ExplodeStep
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim ExplodeStepIndex As System.Integer
Dim value As ExplodeStep

value = instance.IGetExplodeStep(ExplodeStepIndex)
```

### C#

```csharp
ExplodeStep IGetExplodeStep(
   System.int ExplodeStepIndex
)
```

### C++/CLI

```cpp
ExplodeStep^ IGetExplodeStep(
   System.int ExplodeStepIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ExplodeStepIndex`: Index number of the explode step in the explode step sequence

### Return Value

Pointer to the [explode step](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExplodeStep.html)

## VBA Syntax

See [Configuration::IGetExplodeStep](ms-its:sldworksapivb6.chm::/sldworks~Configuration~IGetExplodeStep.html).

## Remarks

Before calling this method, call [IConfiguration::GetNumberOfExplodeSteps](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetNumberOfExplodeSteps.html) to get the number of explode steps in the sequence.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::AddExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep.html)
[IConfiguration::DeleteExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteExplodeStep.html)
[IConfiguration::GetExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetExplodeStep.html)
[IConfiguration::IAddExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IAddExplodeStep.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
