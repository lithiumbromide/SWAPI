---
title: "IGetFaces Method (IDimXpertFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertFeature"
member: "IGetFaces"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature~IGetFaces.html"
---

# IGetFaces Method (IDimXpertFeature)

Gets the SOLIDWORKS faces in this DimXpert feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaces( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertFeature
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetFaces(Count)
```

### C#

```csharp
System.object IGetFaces(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetFaces(
   System.int Count
)
```

### Parameters

- `Count`: Number of faces on this DimXpert feature

### Return Value

in-process, unmanaged C++: Pointer to an array of [faces](ms-its:sldworksapi.chm::/Solidworks.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

See [In-process Methods](sldworksapiprogguide.chm::/Overview/In-process_Methods.htm) for details about this type of method.

Before calling this method, call [IDimXpertFeature::GetFaceCount](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature~GetFaceCount.html) to get the value for the Count parameter.

## See Also

[IDimXpertFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature.html)
[IDimXpertFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
