---
title: "IGetFeatures Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "IGetFeatures"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~IGetFeatures.html"
---

# IGetFeatures Method (IDimXpertPart)

Gets all of the DimXpert features in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFeatures( _
   ByVal Count As System.Integer _
) As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim Count As System.Integer
Dim value As DimXpertFeature

value = instance.IGetFeatures(Count)
```

### C#

```csharp
DimXpertFeature IGetFeatures(
   System.int Count
)
```

### C++/CLI

```cpp
DimXpertFeature^ IGetFeatures(
   System.int Count
)
```

### Parameters

- `Count`: Number of DimXpert features

### Return Value

- in-process, unmanaged C++: Pointer to an array of [IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

See [In-process Methods](sldworksapiprogguide.chm::/Overview/In-process_Methods.htm) for details about this type of method.

Before calling this method, call [IDimXpertPart::GetFeatureCount](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~GetFeatureCount.html) to get the value for the Count parameter.

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
