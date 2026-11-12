---
title: "ReverseTranslationDirection Property (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "ReverseTranslationDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ReverseTranslationDirection.html"
---

# ReverseTranslationDirection Property (IExplodeStep)

Gets or sets whether to reverse the explode direction in this regular explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseTranslationDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim value As System.Boolean

instance.ReverseTranslationDirection = value

value = instance.ReverseTranslationDirection
```

### C#

```csharp
System.bool ReverseTranslationDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseTranslationDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the explode direction, false to not

## VBA Syntax

See [ExplodeStep::ReverseTranslationDirection](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~ReverseTranslationDirection.html).

## Examples

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html) examples.

## Remarks

This property is valid only if [IExplodeStep::ExplodeStepType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeStepType.html) is set to [swAssemblyExplodeStepType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyExplodeStepType.html).swAssemblyExplodeStepType_Translate.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
