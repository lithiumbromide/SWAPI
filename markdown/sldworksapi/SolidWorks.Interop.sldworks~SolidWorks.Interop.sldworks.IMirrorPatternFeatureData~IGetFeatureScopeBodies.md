---
title: "IGetFeatureScopeBodies Method (IMirrorPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPatternFeatureData"
member: "IGetFeatureScopeBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~IGetFeatureScopeBodies.html"
---

# IGetFeatureScopeBodies Method (IMirrorPatternFeatureData)

Gets the solid bodies that the mirror pattern feature affects in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFeatureScopeBodies( _
   ByVal Count As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPatternFeatureData
Dim Count As System.Integer
Dim value As Body2

value = instance.IGetFeatureScopeBodies(Count)
```

### C#

```csharp
Body2 IGetFeatureScopeBodies(
   System.int Count
)
```

### C++/CLI

```cpp
Body2^ IGetFeatureScopeBodies(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of solid bodies to affect

### Return Value

- in-process, unmanaged C++: Pointer to an array of solid [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody.html) of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IMirrorPatternFeatureData::GetFeatureScopeBodiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPatternFeatureData~GetFeatureScopeBodiesCount.html) to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.html)
[IMirrorPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData_members.html)
[IMirrorPatternFeatureData::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~ISetFeatureScopeBodies.html)
[IMirrorPatternFeatureData::FeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~FeatureScope.html)
[IMirrorPatternFeatureData::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~FeatureScopeBodies.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
