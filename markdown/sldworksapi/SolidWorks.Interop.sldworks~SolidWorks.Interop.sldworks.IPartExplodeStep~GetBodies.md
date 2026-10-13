---
title: "GetBodies Method (IPartExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IPartExplodeStep"
member: "GetBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~GetBodies.html"
---

# GetBodies Method (IPartExplodeStep)

Gets the bodies of this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodies() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartExplodeStep
Dim value As System.Object

value = instance.GetBodies()
```

### C#

```csharp
System.object GetBodies()
```

### C++/CLI

```cpp
System.Object^ GetBodies();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of solid [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)

## VBA Syntax

See [PartExplodeStep::GetBodies](ms-its:sldworksapivb6.chm::/sldworks~PartExplodeStep~GetBodies.html).

## Examples

See the [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html) example.

## See Also

[IPartExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html)
[IPartExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep_members.html)
[IPartExplodeStep::SetBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~SetBodies.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
