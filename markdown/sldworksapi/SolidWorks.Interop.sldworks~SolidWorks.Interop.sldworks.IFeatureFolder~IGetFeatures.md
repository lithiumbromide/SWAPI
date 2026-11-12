---
title: "IGetFeatures Method (IFeatureFolder)"
project: "SOLIDWORKS API Help"
interface: "IFeatureFolder"
member: "IGetFeatures"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder~IGetFeatures.html"
---

# IGetFeatures Method (IFeatureFolder)

Gets the features in this feature folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFeatures( _
   ByVal NumOfFeatures As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureFolder
Dim NumOfFeatures As System.Integer
Dim value As Feature

value = instance.IGetFeatures(NumOfFeatures)
```

### C#

```csharp
Feature IGetFeatures(
   System.int NumOfFeatures
)
```

### C++/CLI

```cpp
Feature^ IGetFeatures(
   System.int NumOfFeatures
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFeatures`: Number of features in the folder

### Return Value

- in-process, unmanaged C++: Pointer to an array of [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IFeatureFolder::GetFeatureCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureFolder~GetFeatureCount.html) to populate NumOfFeatures.

## See Also

[IFeatureFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder.html)
[IFeatureFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder_members.html)
[IFeatureFolder::GetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder~GetFeatures.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
