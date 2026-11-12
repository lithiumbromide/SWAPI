---
title: "GetElementLocation Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetElementLocation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElementLocation.html"
---

# GetElementLocation Method (ICWMesh)

Gets the coordinates of an element's center.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetElementLocation( _
   ByVal NNodeNo As System.Integer, _
   ByRef XVal As System.Double, _
   ByRef YVal As System.Double, _
   ByRef ZVal As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim NNodeNo As System.Integer
Dim XVal As System.Double
Dim YVal As System.Double
Dim ZVal As System.Double
Dim value As System.Integer

value = instance.GetElementLocation(NNodeNo, XVal, YVal, ZVal)
```

### C#

```csharp
System.int GetElementLocation(
   System.int NNodeNo,
   out System.double XVal,
   out System.double YVal,
   out System.double ZVal
)
```

### C++/CLI

```cpp
System.int GetElementLocation(
   System.int NNodeNo,
   [Out] System.double XVal,
   [Out] System.double YVal,
   [Out] System.double ZVal
)
```

### Parameters

- `NNodeNo`: Element number
- `XVal`: X coordinate of the element's center
- `YVal`: Y coordinate of the element's center
- `ZVal`: Z coordinate of the element's center

### Return Value

Error as defined in [swsMeshElementNodeLocation_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshElementNodeLocation_e.html)

## VBA Syntax

See [CWMesh::GetElementLocation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetElementLocation.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetDefaultElementSizeAndTolerance Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetDefaultElementSizeAndTolerance.html)
[ICWMesh::GetElementDataFromEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElementDataFromEntity.html)
[ICWMesh::GetElements Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElements.html)
[ICWMesh::ElementCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ElementCount.html)
[ICWMesh::ElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ElementSize.html)
[ICWMesh::MinElementsInCircle Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementsInCircle.html)
[ICWMesh::MaxAspectRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MaxAspectRatio.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
