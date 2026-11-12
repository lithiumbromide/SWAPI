---
title: "Visible Property (IProjectionArrow)"
project: "SOLIDWORKS API Help"
interface: "IProjectionArrow"
member: "Visible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~Visible.html"
---

# Visible Property (IProjectionArrow)

Gets whether the projection arrow is visible.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Visible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionArrow
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

True if projection arrow is visible, false if not

## VBA Syntax

See [ProjectionArrow::Visible](ms-its:sldworksapivb6.chm::/sldworks~ProjectionArrow~Visible.html).

## Examples

[Is There a Projection Arrow and Is It Visible (C#)](Is_There_a_Projection_Arrow_and_Is_It_Visible_Example_CSharp.htm)
[Is There a Projection Arrow and Is It Visible (VB.NET)](Is_There_a_Projection_Arrow_and_Is_It_Visible_Example_VBNET.htm)
[Is There a Projection Arrow and Is It Visible (VBA)](Is_There_a_Projection_Arrow_and_Is_It_Visible_Example_VB.htm)

## See Also

[IProjectionArrow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.html)
[IProjectionArrow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow_members.html)

## Availability

SOLIDWORKS 2009 SP03, Revision Number 17.3
