---
title: "ExplodeDistance Property (IPartExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IPartExplodeStep"
member: "ExplodeDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~ExplodeDistance.html"
---

# ExplodeDistance Property (IPartExplodeStep)

Gets or sets the distance to move bodies in this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExplodeDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPartExplodeStep
Dim value As System.Double

instance.ExplodeDistance = value

value = instance.ExplodeDistance
```

### C#

```csharp
System.double ExplodeDistance {get; set;}
```

### C++/CLI

```cpp
property System.double ExplodeDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance in meters to move bodies

## VBA Syntax

See [PartExplodeStep::ExplodeDistance](ms-its:sldworksapivb6.chm::/sldworks~PartExplodeStep~ExplodeDistance.html).

## Examples

See the [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html) example.

## See Also

[IPartExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html)
[IPartExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
