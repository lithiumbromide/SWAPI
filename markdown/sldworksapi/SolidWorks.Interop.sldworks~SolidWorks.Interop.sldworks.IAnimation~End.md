---
title: "End Method (IAnimation)"
project: "SOLIDWORKS API Help"
interface: "IAnimation"
member: "End"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation~End.html"
---

# End Method (IAnimation)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function End() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnimation
Dim value As System.Boolean

value = instance.End()
```

### C#

```csharp
System.bool End()
```

### C++/CLI

```cpp
System.bool End();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the animation is positioned at its ends, false if the animation controller is not running

## VBA Syntax

See [Animation::End](ms-its:sldworksapivb6.chm::/sldworks~Animation~End.html).

## See Also

[IAnimation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation.html)
[IAnimation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
