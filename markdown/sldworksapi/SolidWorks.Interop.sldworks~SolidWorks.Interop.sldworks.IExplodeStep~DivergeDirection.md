---
title: "DivergeDirection Property (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "DivergeDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~DivergeDirection.html"
---

# DivergeDirection Property (IExplodeStep)

Gets or sets the diverge direction entity for this radial explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Property DivergeDirection As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim value As System.Object

instance.DivergeDirection = value

value = instance.DivergeDirection
```

### C#

```csharp
System.object DivergeDirection {get; set;}
```

### C++/CLI

```cpp
property System.Object^ DivergeDirection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Cylindrical [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), conical face, linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), or [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html) (see **Remarks**)

## VBA Syntax

See [ExplodeStep::DivergeDirection](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~DivergeDirection.html).

## Examples

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html) examples.

## Remarks

This property is valid only if:

- [IExplodeStep::ExplodeStepType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeStepType.html) is set to [swAssemblyExplodeStepType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyExplodeStepType.html).swAssemblyExplodeStepType_Radial,

- and -

- the selected entity creates an angle with the explode direction.

If you set this property to a valid diverge direction entity, then [IExplodeStep::DivergeFromAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~DivergeFromAxis.html) is automatically set to true.

If you set this property to Nothing or null, then IExplodeStep::DivergeFromAxis is automatically set to false.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
