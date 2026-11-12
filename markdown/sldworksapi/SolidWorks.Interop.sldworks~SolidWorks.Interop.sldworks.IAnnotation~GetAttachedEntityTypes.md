---
title: "GetAttachedEntityTypes Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetAttachedEntityTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityTypes.html"
---

# GetAttachedEntityTypes Method (IAnnotation)

Gets the types of entities attached to this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAttachedEntityTypes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Object

value = instance.GetAttachedEntityTypes()
```

### C#

```csharp
System.object GetAttachedEntityTypes()
```

### C++/CLI

```cpp
System.Object^ GetAttachedEntityTypes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) that indicate the attached entity types as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [Annotation::GetAttachedEntityTypes](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetAttachedEntityTypes.html).

## Examples

[Attach Annotation to Entity (C#)](Attach_Annotation_to_Entity_Example_CSharp.htm)
[Attach Annotation to Entity (VB.NET)](Attach_Annotation_to_Entity_Example_VBNET.htm)
[Attach Annotation to Entity (VBA)](Attach_Annotation_to_Entity_Example_VB.htm)

## Remarks

This method supports all annotation types. Use [IAnnotation::GetType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetType.html) to determine the annotation type.

This method returns an array of longs or integers indicating object types. The list of object types corresponds to the list of objects returned by [IAnnotation::GetAttachedEntities3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetAttachedEntities3.html).

You can associate annotations with additional items not listed in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html). If this annotation is attached to one or more entities not listed in swSelectType_e, then this method and [IAnnotation::IGetAttachedEntityTypes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~IGetAttachedEntityTypes.html) return swSelNOTHING in a position in the array corresponding to the unlisted item. IAnnotation::GetAttachedEntities3 indicates an unsupported entity by returning a null value in the position in the array corresponding to the unsupported entity. COM applications that call [IAnnotation::GetAttachedEntityCount3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetAttachedEntityCount3.html) include the null value in the total count of associated entities.

If an annotation is disassociated from its geometry (i.e., dangling), then IAnnotation::GetAttachedEntities3 returns a null value in the position in the array corresponding to the dangling item, and this method returns swSelNOTHING in the position in the array corresponding to the dangling item.

NOTE: If this annotation is not associated with any geometry, then this method and IAnnotation::GetAttachedEntities3 return empty arrays.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::SetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetAttachedEntities.html)

## Availability

SOLIDWORKS 99, datecode 1999207
