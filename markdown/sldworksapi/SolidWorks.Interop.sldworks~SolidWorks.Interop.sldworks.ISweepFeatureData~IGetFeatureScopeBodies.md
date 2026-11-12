---
title: "IGetFeatureScopeBodies Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "IGetFeatureScopeBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IGetFeatureScopeBodies.html"
---

# IGetFeatureScopeBodies Method (ISweepFeatureData)

Obsolete. Gets the solid bodies that the sweep feature affects in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFeatureScopeBodies( _
   ByVal Count As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
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

- in-process, unmanaged C++: Pointer to an array of solid [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISweepFeatureData::GetFeatureScopeBodiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISweepFeatureData~GetFeatureScopeBodiesCount.html) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ISetFeatureScopeBodies.html)
[ISweepFeatureData::FeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~FeatureScope.html)
[ISweepFeatureData::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~FeatureScopeBodies.html)
[ISweepFeatureData::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~AutoSelect.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
