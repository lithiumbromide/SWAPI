---
title: "GetAttachedEntityCount3 Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetAttachedEntityCount3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityCount3.html"
---

# GetAttachedEntityCount3 Method (IAnnotation)

Gets the number of entities to which this annotation is attached.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAttachedEntityCount3() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Integer

value = instance.GetAttachedEntityCount3()
```

### C#

```csharp
System.int GetAttachedEntityCount3()
```

### C++/CLI

```cpp
System.int GetAttachedEntityCount3();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of entities to which this annotation is attached

## VBA Syntax

See [Annotation::GetAttachedEntityCount3](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetAttachedEntityCount3.html).

## Remarks

This method supports all annotation types. See [IAnnotation::GetType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetType.html) to determine the type of annotation.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetAttachedEntities3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities3.html)
[IAnnotation::GetAttachedEntityTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityTypes.html)
[IAnnotation::GetNext3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.html)
[IAnnotation::GetType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetType.html)
[IAnnotation::IGetAttachedEntityTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetAttachedEntityTypes.html)
[IAnnotation::ISetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetAttachedEntities.html)
[IAnnotation::SetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetAttachedEntities.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
