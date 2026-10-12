---
title: "PlayMode Property (IAnimation)"
project: "SOLIDWORKS API Help"
interface: "IAnimation"
member: "PlayMode"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation~PlayMode.html"
---

# PlayMode Property (IAnimation)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Property PlayMode As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnimation
Dim value As System.Integer

instance.PlayMode = value

value = instance.PlayMode
```

### C#

```csharp
System.int PlayMode {get; set;}
```

### C++/CLI

```cpp
property System.int PlayMode {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Mode in which this animation is playing as defined in [swAnimationPlayMode_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAnimationPlayMode_e.html)

## VBA Syntax

See [Animation::PlayMode](ms-its:sldworksapivb6.chm::/sldworks~Animation~PlayMode.html).

## See Also

[IAnimation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation.html)
[IAnimation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
