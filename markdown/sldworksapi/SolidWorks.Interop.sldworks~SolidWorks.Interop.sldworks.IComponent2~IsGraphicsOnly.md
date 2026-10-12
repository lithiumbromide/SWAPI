---
title: "IsGraphicsOnly Property (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IsGraphicsOnly"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsGraphicsOnly.html"
---

# IsGraphicsOnly Property (IComponent2)

Gets whether this component is graphics only.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsGraphicsOnly As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Boolean

value = instance.IsGraphicsOnly
```

### C#

```csharp
System.bool IsGraphicsOnly {get;}
```

### C++/CLI

```cpp
property System.bool IsGraphicsOnly {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if graphics only, false if not

## VBA Syntax

See [Component2::IsGraphicsOnly](ms-its:sldworksapivb6.chm::/sldworks~Component2~IsGraphicsOnly.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
