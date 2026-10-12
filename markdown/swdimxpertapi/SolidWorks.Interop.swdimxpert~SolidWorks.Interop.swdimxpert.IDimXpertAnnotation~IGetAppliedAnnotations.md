---
title: "IGetAppliedAnnotations Method (IDimXpertAnnotation)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAnnotation"
member: "IGetAppliedAnnotations"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation~IGetAppliedAnnotations.html"
---

# IGetAppliedAnnotations Method (IDimXpertAnnotation)

Gets all of the annotations applied to this DimXpert annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAppliedAnnotations( _
   ByVal Count As System.Integer _
) As DimXpertAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAnnotation
Dim Count As System.Integer
Dim value As DimXpertAnnotation

value = instance.IGetAppliedAnnotations(Count)
```

### C#

```csharp
DimXpertAnnotation IGetAppliedAnnotations(
   System.int Count
)
```

### C++/CLI

```cpp
DimXpertAnnotation^ IGetAppliedAnnotations(
   System.int Count
)
```

### Parameters

- `Count`: Number of applied annotations

### Return Value

in-process, unmanaged C++: Pointer to an array of [IDimXpertAnnotation](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

See [In-process Methods](sldworksapiprogguide.chm::/Overview/In-process_Methods.htm) for details about this type of method.

Before calling this method, call [IDimXpertAnnotation::GetAppliedAnnotationCount](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation~GetAppliedAnnotationCount.html) to get the value for the Count parameter.

## See Also

[IDimXpertAnnotation Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation.html)
[IDimXpertAnnotation Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
