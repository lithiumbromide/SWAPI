---
title: "IGetAnnotations Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "IGetAnnotations"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~IGetAnnotations.html"
---

# IGetAnnotations Method (IDimXpertPart)

Gets all of the DimXpert annotations in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAnnotations( _
   ByVal Count As System.Integer _
) As DimXpertAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim Count As System.Integer
Dim value As DimXpertAnnotation

value = instance.IGetAnnotations(Count)
```

### C#

```csharp
DimXpertAnnotation IGetAnnotations(
   System.int Count
)
```

### C++/CLI

```cpp
DimXpertAnnotation^ IGetAnnotations(
   System.int Count
)
```

### Parameters

- `Count`: Number of DimXpert annotations

### Return Value

- in-process, unmanaged C++: Pointer to an array of [IDimXpertAnnotation](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

See [In-process Methods](sldworksapiprogguide.chm::/Overview/In-process_Methods.htm) for details about this type of method.

Before calling this method, call [IDimXpertPart::GetAnnotationCount](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~GetAnnotationCount.html) to get the value for the Count parameter.

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
