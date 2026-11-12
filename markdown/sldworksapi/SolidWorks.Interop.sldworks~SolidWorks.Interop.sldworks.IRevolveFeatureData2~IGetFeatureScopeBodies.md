---
title: "IGetFeatureScopeBodies Method (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "IGetFeatureScopeBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IGetFeatureScopeBodies.html"
---

# IGetFeatureScopeBodies Method (IRevolveFeatureData2)

Gets the solid bodies that the revolve feature affects in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFeatureScopeBodies( _
   ByVal Count As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
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

Call [IRevolveFeatureData2::GetFeatureScopeBodiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevolveFeatureData2~GetFeatureScopeBodiesCount.html) before calling this method to get the value of Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)
[IRevolveFeatureData2::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ISetFeatureScopeBodies.html)
[IRevolveFeatureData2::FeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~FeatureScope.html)
[IRevolveFeatureData2::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~FeatureScopeBodies.html)
[IRevolveFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~AutoSelect.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
