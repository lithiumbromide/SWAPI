---
title: "DivergeFromAxis Property (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "DivergeFromAxis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~DivergeFromAxis.html"
---

# DivergeFromAxis Property (IExplodeStep)

Gets or sets whether to move components at an angle from the explode direction of this radial explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Property DivergeFromAxis As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim value As System.Boolean

instance.DivergeFromAxis = value

value = instance.DivergeFromAxis
```

### C#

```csharp
System.bool DivergeFromAxis {get; set;}
```

### C++/CLI

```cpp
property System.bool DivergeFromAxis {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to move components at an angle from the explode direction, false to not (see **Remarks**)

## VBA Syntax

See [ExplodeStep::DivergeFromAxis](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~DivergeFromAxis.html).

## Examples

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html) examples.

## Remarks

This property is valid only if [IExplodeStep::ExplodeStepType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeStepType.html) is set to [swAssemblyExplodeStepType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyExplodeStepType.html).swAssemblyExplodeStepType_Radial.

If you set this property to false, then [IExplodeStep::DivergeDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~DivergeDirection.html) is automatically set to nothing or null.

If you want to set this property to true, then you must first set IExplodeStep::DivergeDirection to a valid diverge direction entity.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
