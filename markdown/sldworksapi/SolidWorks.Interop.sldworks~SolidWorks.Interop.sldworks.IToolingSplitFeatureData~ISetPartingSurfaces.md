---
title: "ISetPartingSurfaces Method (IToolingSplitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IToolingSplitFeatureData"
member: "ISetPartingSurfaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~ISetPartingSurfaces.html"
---

# ISetPartingSurfaces Method (IToolingSplitFeatureData)

Sets the parting surface bodies for this tooling split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetPartingSurfaces( _
   ByVal Count As System.Integer, _
   ByRef BodyArr As Body2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IToolingSplitFeatureData
Dim Count As System.Integer
Dim BodyArr As Body2

instance.ISetPartingSurfaces(Count, BodyArr)
```

### C#

```csharp
void ISetPartingSurfaces(
   System.int Count,
   ref Body2 BodyArr
)
```

### C++/CLI

```cpp
void ISetPartingSurfaces(
   System.int Count,
   Body2^% BodyArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of parting surface bodies
- `BodyArr`: - in-process, unmanaged C++: Pointer to an array of parting surface [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html)
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.html)
[IToolingSplitFeatureData::GetPartingSurfacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~GetPartingSurfacesCount.html)
[IToolingSplitFeatureData::IGetPartingSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~IGetPartingSurfaces.html)
[IToolingSplitFeatureData::PartingSurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~PartingSurfaces.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
