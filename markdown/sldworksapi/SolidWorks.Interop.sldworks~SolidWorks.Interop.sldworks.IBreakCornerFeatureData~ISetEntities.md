---
title: "ISetEntities Method (IBreakCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBreakCornerFeatureData"
member: "ISetEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~ISetEntities.html"
---

# ISetEntities Method (IBreakCornerFeatureData)

Sets the faces or edges to which this break corner is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetEntities( _
   ByVal EntCount As System.Integer, _
   ByRef EntArray As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakCornerFeatureData
Dim EntCount As System.Integer
Dim EntArray As System.Object

instance.ISetEntities(EntCount, EntArray)
```

### C#

```csharp
void ISetEntities(
   System.int EntCount,
   ref System.object EntArray
)
```

### C++/CLI

```cpp
void ISetEntities(
   System.int EntCount,
   System.Object^% EntArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntCount`: Number of faces or edges
- `EntArray`: - in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) or [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) of size entCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [BreakCornerFeatureData::ISetEntities](ms-its:sldworksapivb6.chm::/sldworks~BreakCornerFeatureData~ISetEntities.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html)
[IBreakCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData_members.html)
[IBreakCornerFeatureData::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~IGetEntities.html)
[IBreakCornerFeatureData::Entities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~Entities.html)
