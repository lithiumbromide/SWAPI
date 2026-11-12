---
title: "IGetEditBodies Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "IGetEditBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetEditBodies.html"
---

# IGetEditBodies Method (IMacroFeatureData)

Gets the bodies to be modified by this macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetEditBodies( _
   ByVal BodiesCount As System.Integer, _
   ByRef PBodies As Body2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim BodiesCount As System.Integer
Dim PBodies As Body2

instance.IGetEditBodies(BodiesCount, PBodies)
```

### C#

```csharp
void IGetEditBodies(
   System.int BodiesCount,
   out Body2 PBodies
)
```

### C++/CLI

```cpp
void IGetEditBodies(
   System.int BodiesCount,
   [Out] Body2^ PBodies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodiesCount`: Number of bodies to be modified by this macro feature
- `PBodies`: - in-process, unmanaged C++: Pointer to an array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) to be modified by this macro feature

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IMacroFeatureData::GetEditBodiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~GetEditBodiesCount.html) to determine the size the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::ISetEditBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetEditBodies.html)
[IMacroFeatureData::EditBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EditBodies.html)
[IMacroFeatureData::EnableMultiBodyConsume Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EnableMultiBodyConsume.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
