---
title: "IGetTableAnnotations Method (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "IGetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~IGetTableAnnotations.html"
---

# IGetTableAnnotations Method (IBomFeature)

Gets the BOM table annotations for this BOM table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTableAnnotations( _
   ByVal Count As System.Integer _
) As BomTableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim Count As System.Integer
Dim value As BomTableAnnotation

value = instance.IGetTableAnnotations(Count)
```

### C#

```csharp
BomTableAnnotation IGetTableAnnotations(
   System.int Count
)
```

### C++/CLI

```cpp
BomTableAnnotation^ IGetTableAnnotations(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of BOM table annotations for this BOM feature

### Return Value

- in-process, unmanaged C++: Pointer to an array of [IBOMTableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation.html) objects
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IBomFeature::GetTableAnnotationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~GetTableAnnotationCount.html) to determine the size of the array.

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)
[IBomFeature::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetTableAnnotations.html)

## Availability

SOLIDWORKS 204 FCS, Revision Number 12
