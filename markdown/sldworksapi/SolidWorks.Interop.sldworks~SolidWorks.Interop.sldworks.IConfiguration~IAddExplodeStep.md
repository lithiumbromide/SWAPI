---
title: "IAddExplodeStep Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "IAddExplodeStep"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IAddExplodeStep.html"
---

# IAddExplodeStep Method (IConfiguration)

Adds a new explode step to the configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddExplodeStep( _
   ByVal ExplDist As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal RigidSubassembly As System.Boolean, _
   ByVal ExplodeRelated As System.Boolean _
) As ExplodeStep
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim ExplDist As System.Double
Dim ReverseDir As System.Boolean
Dim RigidSubassembly As System.Boolean
Dim ExplodeRelated As System.Boolean
Dim value As ExplodeStep

value = instance.IAddExplodeStep(ExplDist, ReverseDir, RigidSubassembly, ExplodeRelated)
```

### C#

```csharp
ExplodeStep IAddExplodeStep(
   System.double ExplDist,
   System.bool ReverseDir,
   System.bool RigidSubassembly,
   System.bool ExplodeRelated
)
```

### C++/CLI

```cpp
ExplodeStep^ IAddExplodeStep(
   System.double ExplDist,
   System.bool ReverseDir,
   System.bool RigidSubassembly,
   System.bool ExplodeRelated
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ExplDist`: Explode distance
- `ReverseDir`: True to reverse the direction of the explode step, false to not
- `RigidSubassembly`: True to explode entire sub assembly, false to explode just the selected component
- `ExplodeRelated`: True to explode related components together, false to not

### Return Value

Pointer to a newly created [explode step](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExplodeStep.html)

## VBA Syntax

See [Configuration::IAddExplodeStep](ms-its:sldworksapivb6.chm::/sldworks~Configuration~IAddExplodeStep.html).

## Remarks

Before calling this method, you must select by mark both an edge direction to explode along and a component to move. For example:

```vb
boolstatus = Model.Extension.SelectByID2('', 'EDGE', -0.011, 0.06, 0.084, True, 1, Nothing)
boolstatus = Model.Extension.SelectByID2('squarebolt1-1@Assem1', 'COMPONENT', 0, 0, 0, True, 2, Nothing, swSelectOptionDefault)
```

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::AddExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep.html)
[IConfiguration::DeleteExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteExplodeStep.html)
[IConfiguration::GetExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetExplodeStep.html)
[IConfiguration::GetNumberOfExplodeSteps Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfExplodeSteps.html)
[IConfiguration::IGetExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetExplodeStep.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
