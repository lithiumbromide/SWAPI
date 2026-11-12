---
title: "IGetMultiJogLeaders Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "IGetMultiJogLeaders"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetMultiJogLeaders.html"
---

# IGetMultiJogLeaders Method (IAnnotation)

Gets the multi-jog leaders on this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMultiJogLeaders( _
   ByVal Count As System.Integer _
) As MultiJogLeader
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim Count As System.Integer
Dim value As MultiJogLeader

value = instance.IGetMultiJogLeaders(Count)
```

### C#

```csharp
MultiJogLeader IGetMultiJogLeaders(
   System.int Count
)
```

### C++/CLI

```cpp
MultiJogLeader^ IGetMultiJogLeaders(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of multi-jog leaders on this annotation

### Return Value

- in-process, unmanaged C++: Pointer to an array of the [multi-jog leaders](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMultiJogLeader.html)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IAnnotation::GetMultiJogLeaderCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetMultiJogLeaderCount.html) to get Count.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetMultiJogLeaders Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaders.html)

## Availability

SOLIDWORKS 2008 SP1, Revision Number 16.1
