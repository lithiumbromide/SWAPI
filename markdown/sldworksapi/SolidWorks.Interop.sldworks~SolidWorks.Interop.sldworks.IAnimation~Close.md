---
title: "Close Method (IAnimation)"
project: "SOLIDWORKS API Help"
interface: "IAnimation"
member: "Close"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation~Close.html"
---

# Close Method (IAnimation)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function Close() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnimation
Dim value As System.Boolean

value = instance.Close()
```

### C#

```csharp
System.bool Close()
```

### C++/CLI

```cpp
System.bool Close();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the animation controller closes, false if the animation controller is not
running

## VBA Syntax

See [Animation::Close](ms-its:sldworksapivb6.chm::/sldworks~Animation~Close.html).

## See Also

[IAnimation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation.html)
[IAnimation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
