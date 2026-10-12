---
title: "GetComponentXform Method (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "GetComponentXform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponentXform.html"
---

# GetComponentXform Method (IExplodeStep)

Gets the transform of this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentXform() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim value As System.Object

value = instance.GetComponentXform()
```

### C#

```csharp
System.object GetComponentXform()
```

### C++/CLI

```cpp
System.Object^ GetComponentXform();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of 16 doubles describing the transform of the explode step

## VBA Syntax

See [ExplodeStep::GetComponentXform](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~GetComponentXform.html).

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)
[IExplodeStep::IGetComponentXform Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~IGetComponentXform.html)
[IExplodeStep::GetComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponents.html)
[IExplodeStep::GetSpecificComponentXForm Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetSpecificComponentXForm.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
