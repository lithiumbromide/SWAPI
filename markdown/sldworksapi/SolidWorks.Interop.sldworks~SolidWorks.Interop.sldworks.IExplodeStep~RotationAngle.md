---
title: "RotationAngle Property (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "RotationAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~RotationAngle.html"
---

# RotationAngle Property (IExplodeStep)

Gets or sets the angle of component rotation in this regular or radial explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotationAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim value As System.Double

instance.RotationAngle = value

value = instance.RotationAngle
```

### C#

```csharp
System.double RotationAngle {get; set;}
```

### C++/CLI

```cpp
property System.double RotationAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle in radians of component rotation

## VBA Syntax

See [ExplodeStep::RotationAngle](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~RotationAngle.html).

## Examples

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html) examples.

## Remarks

If [IExplodeStep::AutoSpaceComponentsOnDrag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~AutoSpaceComponentsOnDrag.html) is set to true, then this property is automatically 0.0.

If [IExplodeStep::ExplodeStepType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeStepType.html) is set to [swAssemblyExplodeStepType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyExplodeStepType.html):

- swAssemblyExplodeStepType_Radial, then this property sets the degree of rotation of components about their origins.
- swAssemblyExplodeStepType_Translate, then this property sets the degree of rotation of components about the rotation axis.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
