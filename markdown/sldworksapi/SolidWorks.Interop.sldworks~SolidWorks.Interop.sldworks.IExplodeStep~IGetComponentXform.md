---
title: "IGetComponentXform Method (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "IGetComponentXform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~IGetComponentXform.html"
---

# IGetComponentXform Method (IExplodeStep)

Gets the transform for this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetComponentXform() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim value As System.Double

value = instance.IGetComponentXform()
```

### C#

```csharp
System.double IGetComponentXform()
```

### C++/CLI

```cpp
System.double IGetComponentXform();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of 16 doubles describing the transform of the component

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)
[IExplodeStep::GetComponentXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponentXform.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
