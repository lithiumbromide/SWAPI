---
title: "Stop Method (IAnimation)"
project: "SOLIDWORKS API Help"
interface: "IAnimation"
member: "Stop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation~Stop.html"
---

# Stop Method (IAnimation)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function Stop() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnimation
Dim value As System.Boolean

value = instance.Stop()
```

### C#

```csharp
System.bool Stop()
```

### C++/CLI

```cpp
System.bool Stop();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the animation stops playing and is positioned at its beginning, false if an animation controller is not running

## VBA Syntax

See [Animation::Stop](ms-its:sldworksapivb6.chm::/sldworks~Animation~Stop.html).

## See Also

[IAnimation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation.html)
[IAnimation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
