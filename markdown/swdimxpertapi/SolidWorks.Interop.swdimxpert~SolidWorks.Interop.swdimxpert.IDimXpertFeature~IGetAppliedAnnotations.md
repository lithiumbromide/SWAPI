---
title: "IGetAppliedAnnotations Method (IDimXpertFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertFeature"
member: "IGetAppliedAnnotations"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature~IGetAppliedAnnotations.html"
---

# IGetAppliedAnnotations Method (IDimXpertFeature)

Gets all of the annotations applied to this DimXpert feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAppliedAnnotations( _
   ByVal Count As System.Integer _
) As DimXpertAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertFeature
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

- `Count`: Number of annotations applied to this DimXpert feature

### Return Value

in-process, unmanaged C++: Pointer to an array of [IDimXpertAnnotation](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

See [In-process Methods](sldworksapiprogguide.chm::/Overview/In-process_Methods.htm) for details about this type of method.

Before calling this method, call [IDimXpertFeature::GetAppliedAnnotationCount](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature~GetAppliedAnnotationCount.html) to get the value for the Count parameter.

## See Also

[IDimXpertFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature.html)
[IDimXpertFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
