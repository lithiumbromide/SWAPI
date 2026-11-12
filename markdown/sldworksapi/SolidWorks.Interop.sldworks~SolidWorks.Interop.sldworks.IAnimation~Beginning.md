---
title: "Beginning Method (IAnimation)"
project: "SOLIDWORKS API Help"
interface: "IAnimation"
member: "Beginning"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation~Beginning.html"
---

# Beginning Method (IAnimation)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function Beginning() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnimation
Dim value As System.Boolean

value = instance.Beginning()
```

### C#

```csharp
System.bool Beginning()
```

### C++/CLI

```cpp
System.bool Beginning();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the animation is positioned at its beginning, false if an animation controller
is not running

## VBA Syntax

See [Animation::Beginning](ms-its:sldworksapivb6.chm::/sldworks~Animation~Beginning.html).

## See Also

[IAnimation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation.html)
[IAnimation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
