---
title: "SetBodies Method (IPartExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IPartExplodeStep"
member: "SetBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~SetBodies.html"
---

# SetBodies Method (IPartExplodeStep)

Sets the bodies of this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetBodies( _
   ByVal Bodies As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPartExplodeStep
Dim Bodies As System.Object

instance.SetBodies(Bodies)
```

### C#

```csharp
void SetBodies(
   System.object Bodies
)
```

### C++/CLI

```cpp
void SetBodies(
   System.Object^ Bodies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bodies`: Array of solid [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)

## VBA Syntax

See [PartExplodeStep::SetBodies](ms-its:sldworksapivb6.chm::/sldworks~PartExplodeStep~SetBodies.html).

## See Also

[IPartExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html)
[IPartExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep_members.html)
[IPartExplodeStep::GetBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~GetBodies.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
