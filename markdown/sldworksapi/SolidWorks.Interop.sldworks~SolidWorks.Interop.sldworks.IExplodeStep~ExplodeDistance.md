---
title: "ExplodeDistance Property (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "ExplodeDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeDistance.html"
---

# ExplodeDistance Property (IExplodeStep)

Gets or sets the distance to move components in this regular or radial explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExplodeDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
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

Distance in meters to move components

## VBA Syntax

See [ExplodeStep::ExplodeDistance](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~ExplodeDistance.html).

## Examples

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html) examples.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
