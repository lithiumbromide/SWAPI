---
title: "ExplodeStepType Property (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "ExplodeStepType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeStepType.html"
---

# ExplodeStepType Property (IExplodeStep)

Gets the type of this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ExplodeStepType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim value As System.Integer

value = instance.ExplodeStepType
```

### C#

```csharp
System.int ExplodeStepType {get;}
```

### C++/CLI

```cpp
property System.int ExplodeStepType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Explode step type as defined in [swAssemblyExplodeStepType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyExplodeStepType.html)

## VBA Syntax

See [ExplodeStep::ExplodeStepType](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~ExplodeStepType.html).

## Examples

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html) examples.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)
[IExplodeStep::DivergeDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~DivergeDirection.html)
[IExplodeStep::DivergeFromAxis Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~DivergeFromAxis.html)
[IExplodeStep::ReverseRotationDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ReverseRotationDirection.html)
[IExplodeStep::ReverseTranslationDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ReverseTranslationDirection.html)
[IExplodeStep::RotateAboutEachComponentOrigin Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~RotateAboutEachComponentOrigin.html)
[IExplodeStep::RotationAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~RotationAngle.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
