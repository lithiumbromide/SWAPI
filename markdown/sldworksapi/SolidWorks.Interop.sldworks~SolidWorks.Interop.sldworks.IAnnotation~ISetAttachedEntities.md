---
title: "ISetAttachedEntities Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "ISetAttachedEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetAttachedEntities.html"
---

# ISetAttachedEntities Method (IAnnotation)

Attaches this annotation to the specified entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetAttachedEntities( _
   ByVal Count As System.Integer, _
   ByRef LpArr As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim Count As System.Integer
Dim LpArr As System.Object
Dim value As System.Boolean

value = instance.ISetAttachedEntities(Count, LpArr)
```

### C#

```csharp
System.bool ISetAttachedEntities(
   System.int Count,
   ref System.object LpArr
)
```

### C++/CLI

```cpp
System.bool ISetAttachedEntities(
   System.int Count,
   System.Object^% LpArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of entities to which to attach this annotation
- `LpArr`: - in-process, unmanaged C++: Pointer to an array of entities to attach this annotation to (see **Remarks**)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if the annotation is attached to the entities, false if not

## Remarks

Not all annotations can be attached to a different entity (i.e., face, edge, or vertex). Experiment with this method to determine which annotations can be attached to which entities.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetAttachedEntities2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities2.html)
[SetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetAttachedEntities.html)

## Availability

2007 FCS, Revision Number 15
