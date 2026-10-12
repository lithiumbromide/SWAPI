---
title: "RotateAboutEachComponentOrigin Property (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "RotateAboutEachComponentOrigin"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~RotateAboutEachComponentOrigin.html"
---

# RotateAboutEachComponentOrigin Property (IExplodeStep)

Gets or sets whether components rotate about their origins in this regular explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotateAboutEachComponentOrigin As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim value As System.Boolean

instance.RotateAboutEachComponentOrigin = value

value = instance.RotateAboutEachComponentOrigin
```

### C#

```csharp
System.bool RotateAboutEachComponentOrigin {get; set;}
```

### C++/CLI

```cpp
property System.bool RotateAboutEachComponentOrigin {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if components rotate about their origins, false if not

## VBA Syntax

See [ExplodeStep::RotateAboutEachComponentOrigin](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~RotateAboutEachComponentOrigin.html).

## Examples

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html) examples.

## Remarks

If [IExplodeStep::AutoSpaceComponentsOnDrag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~AutoSpaceComponentsOnDrag.html) is set to true, then this property is automatically false.

This property is valid only if [IExplodeStep::ExplodeStepType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeStepType.html) is set to [swAssemblyExplodeStepType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyExplodeStepType.html).swAssemblyExplodeStepType_Translate.

If this property is set to true, then the rotation axis is automatically populated.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
