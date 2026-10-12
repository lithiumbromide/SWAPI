---
title: "IGetDecals Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetDecals"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetDecals.html"
---

# IGetDecals Method (IComponent2)

Gets the decals applied to this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDecals( _
   ByVal Count As System.Integer _
) As Decal
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim Count As System.Integer
Dim value As Decal

value = instance.IGetDecals(Count)
```

### C#

```csharp
Decal IGetDecals(
   System.int Count
)
```

### C++/CLI

```cpp
Decal^ IGetDecals(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of decals

### Return Value

- in-process, unmanaged C++: Pointer to an array of [decals](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDecal.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IComponent2::GetDecalsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetDecalsCount.html) to get the value of Count.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetDecals.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
