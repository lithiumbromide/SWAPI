---
title: "ISetSeedComponentArray Method (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "ISetSeedComponentArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~ISetSeedComponentArray.html"
---

# ISetSeedComponentArray Method (ILocalLinearPatternFeatureData)

Sets an array of seed component features to pattern for this linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetSeedComponentArray( _
   ByVal FeatCount As System.Integer, _
   ByRef ArrayDataIn As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim FeatCount As System.Integer
Dim ArrayDataIn As System.Object

instance.ISetSeedComponentArray(FeatCount, ArrayDataIn)
```

### C#

```csharp
void ISetSeedComponentArray(
   System.int FeatCount,
   ref System.object ArrayDataIn
)
```

### C++/CLI

```cpp
void ISetSeedComponentArray(
   System.int FeatCount,
   System.Object^% ArrayDataIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FeatCount`: Number of seed components
- `ArrayDataIn`: - in-process, unmanaged C++: Pointer to an array of seed component [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) (see **Remarks**)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

You can pass a mixed array of [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) and [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) objects representing components.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)
[ILocalLinearPatternFeatureData::GetSeedComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~GetSeedComponentCount.html)
[ILocalLinearPatternFeatureData::IGetSeedComponentArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~IGetSeedComponentArray.html)
[ILocalLinearPatternFeatureData::SeedComponentArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~SeedComponentArray.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
