---
title: "GetSubAssemblyExplodeSteps Method (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "GetSubAssemblyExplodeSteps"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetSubAssemblyExplodeSteps.html"
---

# GetSubAssemblyExplodeSteps Method (IExplodeStep)

Gets the explode steps of this subassembly explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSubAssemblyExplodeSteps() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim value As System.Object

value = instance.GetSubAssemblyExplodeSteps()
```

### C#

```csharp
System.object GetSubAssemblyExplodeSteps()
```

### C++/CLI

```cpp
System.Object^ GetSubAssemblyExplodeSteps();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IExplodeSteps](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html) in the subassembly explode view

## VBA Syntax

See [ExplodeStep::GetSubAssemblyExplodeSteps](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~GetSubAssemblyExplodeSteps.html).

## Examples

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html) examples.

## Remarks

A subassembly explode step is created when you click **Reuse Subassembly Explode** on the Explode PropertyManager. This method retrieves the nested explode steps of the subassembly.

This method is valid only if [IExplodeStep::ExplodeStepType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeStepType.html) returns [swAssemblyExplodeStepType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyExplodeStepType.html).swAssemblyExplodeStepType_SubAssembly.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
