---
title: "SetAttachedEntities Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "SetAttachedEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetAttachedEntities.html"
---

# SetAttachedEntities Method (IAnnotation)

Attaches this annotation to the specified entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAttachedEntities( _
   ByVal AttachedEnts As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim AttachedEnts As System.Object
Dim value As System.Boolean

value = instance.SetAttachedEntities(AttachedEnts)
```

### C#

```csharp
System.bool SetAttachedEntities(
   System.object AttachedEnts
)
```

### C++/CLI

```cpp
System.bool SetAttachedEntities(
   System.Object^ AttachedEnts
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AttachedEnts`: Array of entities to attach this annotation to (see **Remarks**)

### Return Value

True if the annotation is attached to the entities, false if not

## VBA Syntax

See [Annotation::SetAttachedEntities](ms-its:sldworksapivb6.chm::/sldworks~Annotation~SetAttachedEntities.html).

## Examples

[Attach Annotation to Entity (C#)](Attach_Annotation_to_Entity_Example_CSharp.htm)
[Attach Annotation to Entity (VB.NET)](Attach_Annotation_to_Entity_Example_VBNET.htm)
[Attach Annotation to Entity (VBA)](Attach_Annotation_to_Entity_Example_VB.htm)

## Remarks

Not all annotations can be attached to a different entity (i.e., face, edge, or vertex). Experiment with this method to determine which annotations can be attached to which entities.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::ISetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetAttachedEntities.html)
[IAnnotation::GetAttachedEntities2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities2.html)

## Availability

2007 FCS, Revision Number 15
