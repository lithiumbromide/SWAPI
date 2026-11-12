---
title: "ISetBodiesToBeTrimmed Method (IWeldmentTrimExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentTrimExtendFeatureData"
member: "ISetBodiesToBeTrimmed"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~ISetBodiesToBeTrimmed.html"
---

# ISetBodiesToBeTrimmed Method (IWeldmentTrimExtendFeatureData)

Sets the bodies to trim.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetBodiesToBeTrimmed( _
   ByVal Count As System.Integer, _
   ByRef BodiesIn As Body2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentTrimExtendFeatureData
Dim Count As System.Integer
Dim BodiesIn As Body2

instance.ISetBodiesToBeTrimmed(Count, BodiesIn)
```

### C#

```csharp
void ISetBodiesToBeTrimmed(
   System.int Count,
   ref Body2 BodiesIn
)
```

### C++/CLI

```cpp
void ISetBodiesToBeTrimmed(
   System.int Count,
   Body2^% BodiesIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of bodies to trim
- `BodiesIn`: - in-process, unmanaged C++: Pointer to an array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) to trim (see **Remarks**)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Only end-trim corner types (swEndConditionTrim) can have multiple bodies to trim. Use [IWeldmentTrimExtendFeatureData::CornerType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentTrimExtendFeatureData~CornerType.html) to determine the type of corner.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.html)
[IWeldmentTrimExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.html)
[IWeldmentTrimExtendFeatureData::GetBodiesToBeTrimmedCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetBodiesToBeTrimmedCount.html)
[IWeldmentTrimExtendFeatureData::IGetBodiesToBeTrimmed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetBodiesToBeTrimmed.html)
[IWeldmentTrimExtendFeatureData::BodiesToBeTrimmed Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~BodiesToBeTrimmed.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
