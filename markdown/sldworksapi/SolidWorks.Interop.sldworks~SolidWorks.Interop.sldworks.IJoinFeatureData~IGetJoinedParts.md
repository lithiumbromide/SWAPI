---
title: "IGetJoinedParts Method (IJoinFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJoinFeatureData"
member: "IGetJoinedParts"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~IGetJoinedParts.html"
---

# IGetJoinedParts Method (IJoinFeatureData)

Gets the joined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetJoinedParts( _
   ByVal Count As System.Integer _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IJoinFeatureData
Dim Count As System.Integer
Dim value As Component2

value = instance.IGetJoinedParts(Count)
```

### C#

```csharp
Component2 IGetJoinedParts(
   System.int Count
)
```

### C++/CLI

```cpp
Component2^ IGetJoinedParts(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of joined parts

### Return Value

- in-process, unmanaged C++: Pointer to an array of joined parts, the [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) objects

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IJoinFeatureData::GetJoinedPartsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IJoinFeatureData~GetJoinedPartsCount.html) before calling this method to determine Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IJoinFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData.html)
[IJoinFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData_members.html)
[IJoinFeatureData::ISetJoinedParts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~ISetJoinedParts.html)
[IJoinFeatureData::JoinedParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~JoinedParts.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
