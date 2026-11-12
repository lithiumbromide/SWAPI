---
title: "DeleteExplodeStep Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "DeleteExplodeStep"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteExplodeStep.html"
---

# DeleteExplodeStep Method (IConfiguration)

Deletes the specified explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteExplodeStep( _
   ByVal ExplodeStepName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim ExplodeStepName As System.String
Dim value As System.Boolean

value = instance.DeleteExplodeStep(ExplodeStepName)
```

### C#

```csharp
System.bool DeleteExplodeStep(
   System.string ExplodeStepName
)
```

### C++/CLI

```cpp
System.bool DeleteExplodeStep(
   System.String^ ExplodeStepName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ExplodeStepName`: Name of the explode step to delete

### Return Value

True if the explode step was deleted successfully, false if not

## VBA Syntax

See [Configuration::DeleteExplodeStep](ms-its:sldworksapivb6.chm::/sldworks~Configuration~DeleteExplodeStep.html).

## Examples

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html) examples.

## Remarks

This method is valid only for the active configuration.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::AddExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep.html)
[IConfiguration::IAddExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IAddExplodeStep.html)
[IConfiguration::GetExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetExplodeStep.html)
[IConfiguration::GetNumberOfExplodeSteps Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfExplodeSteps.html)
[IConfiguration::IGetExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetExplodeStep.html)
[IConfiguration::AddRadialExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRadialExplodeStep.html)
[IConfiguration::AddPartExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddPartExplodeStep.html)
[IConfiguration::GetPartExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetPartExplodeStep.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
