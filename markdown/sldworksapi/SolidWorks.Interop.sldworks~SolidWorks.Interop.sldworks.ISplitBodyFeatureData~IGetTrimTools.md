---
title: "IGetTrimTools Method (ISplitBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitBodyFeatureData"
member: "IGetTrimTools"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~IGetTrimTools.html"
---

# IGetTrimTools Method (ISplitBodyFeatureData)

Gets the trimming surfaces used as trim tools in this Split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTrimTools( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitBodyFeatureData
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetTrimTools(Count)
```

### C#

```csharp
System.object IGetTrimTools(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetTrimTools(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of trimming surfaces used as trim tools in this Split feature

### Return Value

- in-process, unmanaged C++: Pointer to an array of trimming surfaces used as trim tools:

  - Planar and non-planar faces
  - Reference planes
  - Reference surfaces
  - Sketches
- VBA, VB.NET, C#, and C++/CLI: Not supported
- See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISplitBodyFeatureData::GetTrimToolsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitBodyFeatureData~GetTrimToolsCount.html) before calling this method to determine the size of the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html)
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.html)
[ISplitBodyFeatureData::TrimTools Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~TrimTools.html)
[ISplitBodyFeatureData::ISetTrimTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~ISetTrimTools.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
