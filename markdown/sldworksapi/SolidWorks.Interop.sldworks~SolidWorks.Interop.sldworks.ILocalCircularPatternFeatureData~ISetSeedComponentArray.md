---
title: "ISetSeedComponentArray Method (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "ISetSeedComponentArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ISetSeedComponentArray.html"
---

# ISetSeedComponentArray Method (ILocalCircularPatternFeatureData)

Sets an array of seed component features for this circular component pattern feature.

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
Dim instance As ILocalCircularPatternFeatureData
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
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

You can pass a mixed array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html) and [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html) objects representing components.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)
[ILocalCircularPatternFeatureData::GetSeedComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetSeedComponentCount.html)
[ILocalCircularPatternFeatureData::IGetSeedComponentArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~IGetSeedComponentArray.html)
[ILocalCircularPatternFeatureData::SeedComponentArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~SeedComponentArray.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
