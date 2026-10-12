---
title: "IGetFeatures Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IGetFeatures"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFeatures.html"
---

# IGetFeatures Method (IBody2)

Gets the features in this body in a multibody sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFeatures( _
   ByVal NumberOfFeatures As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumberOfFeatures As System.Integer
Dim value As Feature

value = instance.IGetFeatures(NumberOfFeatures)
```

### C#

```csharp
Feature IGetFeatures(
   System.int NumberOfFeatures
)
```

### C++/CLI

```cpp
Feature^ IGetFeatures(
   System.int NumberOfFeatures
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumberOfFeatures`: Number of features in this body in a multibody sheet metal part

### Return Value

- in-process, unmanaged C++: Pointer to an array of [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) in this body in a multibody sheet metal part
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IBody2::GetFeatureCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetFeatureCount.html) to get NumberOfFeatures.

The features of a body in a multibody sheet metal part are located in the solid bodies folder in the FeatureManager design tree.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFeatures.html)
[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html)
[IBodyFolder::GetBodyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodyCount.html)
[IBodyFolder::GetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodies.html)
[IBodyFolder::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~IGetBodies.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
