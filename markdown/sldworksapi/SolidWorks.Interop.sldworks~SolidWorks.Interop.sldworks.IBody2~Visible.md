---
title: "Visible Property (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "Visible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Visible.html"
---

# Visible Property (IBody2)

Gets whether this body is visible or hidden.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Visible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Boolean

value = instance.Visible
```

### C#

```csharp
System.bool Visible {get;}
```

### C++/CLI

```cpp
property System.bool Visible {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the body is visible, false if it is hidden

## VBA Syntax

See [Body2::Visible](ms-its:sldworksapivb6.chm::/sldworks~Body2~Visible.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
