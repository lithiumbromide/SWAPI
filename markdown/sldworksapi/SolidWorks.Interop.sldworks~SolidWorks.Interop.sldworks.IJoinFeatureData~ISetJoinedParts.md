---
title: "ISetJoinedParts Method (IJoinFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJoinFeatureData"
member: "ISetJoinedParts"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~ISetJoinedParts.html"
---

# ISetJoinedParts Method (IJoinFeatureData)

Sets the parts to join.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetJoinedParts( _
   ByVal Count As System.Integer, _
   ByRef Parts As Component2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IJoinFeatureData
Dim Count As System.Integer
Dim Parts As Component2

instance.ISetJoinedParts(Count, Parts)
```

### C#

```csharp
void ISetJoinedParts(
   System.int Count,
   ref Component2 Parts
)
```

### C++/CLI

```cpp
void ISetJoinedParts(
   System.int Count,
   Component2^% Parts
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of parts to join
- `Parts`: - in-process, unmanaged C++: Pointer to an array of joined parts, the [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) objects

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IJoinFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData.html)
[IJoinFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData_members.html)
[IJoinFeatureData::GetJoinedPartsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~GetJoinedPartsCount.html)
[IJoinFeatureData::IGetJoinedParts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~IGetJoinedParts.html)
[IJoinFeatureData::JoinedParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~JoinedParts.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
