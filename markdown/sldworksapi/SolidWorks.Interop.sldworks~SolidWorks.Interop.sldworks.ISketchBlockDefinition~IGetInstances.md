---
title: "IGetInstances Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "IGetInstances"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetInstances.html"
---

# IGetInstances Method (ISketchBlockDefinition)

Gets all of the block instances of this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetInstances( _
   ByVal Count As System.Integer _
) As SketchBlockInstance
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim Count As System.Integer
Dim value As SketchBlockInstance

value = instance.IGetInstances(Count)
```

### C#

```csharp
SketchBlockInstance IGetInstances(
   System.int Count
)
```

### C++/CLI

```cpp
SketchBlockInstance^ IGetInstances(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of block instances

### Return Value

- in-process, unmanaged C++: Pointer to an array of all of the [block instances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISketchBlockDefinition::GetInstanceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetInstanceCount.html) before calling this method to get the value of Count.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::GetInstances Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetInstances.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
