---
title: "IGetEntities Method (IBreakCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBreakCornerFeatureData"
member: "IGetEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~IGetEntities.html"
---

# IGetEntities Method (IBreakCornerFeatureData)

Gets the faces or edges to which this break corner is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEntities( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakCornerFeatureData
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetEntities(Count)
```

### C#

```csharp
System.object IGetEntities(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetEntities(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of faces or edges

### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) or [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) of size count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IBreakCornerFeatureData::GetEntitiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBreakCornerFeatureData~GetEntitiesCount.html) before calling this method. See Access Selections that Define Features for additional details on using this method.

## See Also

[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html)
[IBreakCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData_members.html)
[IBreakCornerFeatureData::ISetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~ISetEntities.html)
[IBreakCornerFeatureData::Entities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~Entities.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
