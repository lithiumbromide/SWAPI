---
title: "ReverseRotationDirection Property (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "ReverseRotationDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ReverseRotationDirection.html"
---

# ReverseRotationDirection Property (IExplodeStep)

Gets or sets whether to reverse the direction of rotation of components in this regular explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseRotationDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim value As System.Boolean

instance.ReverseRotationDirection = value

value = instance.ReverseRotationDirection
```

### C#

```csharp
System.bool ReverseRotationDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseRotationDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of rotation of components, false to not

## VBA Syntax

See [ExplodeStep::ReverseRotationDirection](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~ReverseRotationDirection.html).

## Examples

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html) examples.

## Remarks

This property is valid only if [IExplodeStep::ExplodeStepType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeStepType.html) is set to [swAssemblyExplodeStepType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyExplodeStepType.html).swAssemblyExplodeStepType_Translate.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
