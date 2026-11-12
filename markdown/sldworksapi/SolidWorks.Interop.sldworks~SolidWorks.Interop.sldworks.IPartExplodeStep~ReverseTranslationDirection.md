---
title: "ReverseTranslationDirection Property (IPartExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IPartExplodeStep"
member: "ReverseTranslationDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~ReverseTranslationDirection.html"
---

# ReverseTranslationDirection Property (IPartExplodeStep)

Gets or sets whether to reverse the direction of explode in this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseTranslationDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartExplodeStep
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

True to reverse the direction of explode, false to not

## VBA Syntax

See [PartExplodeStep::ReverseTranslationDirection](ms-its:sldworksapivb6.chm::/sldworks~PartExplodeStep~ReverseTranslationDirection.html).

## Examples

See the [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html) example.

## See Also

[IPartExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html)
[IPartExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
