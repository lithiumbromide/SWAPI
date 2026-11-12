---
title: "IGetSeedComponentArray Method (IDerivedPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPatternFeatureData"
member: "IGetSeedComponentArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~IGetSeedComponentArray.html"
---

# IGetSeedComponentArray Method (IDerivedPatternFeatureData)

Gets the seed component features for this derived pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSeedComponentArray() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPatternFeatureData
Dim value As System.Object

value = instance.IGetSeedComponentArray()
```

### C#

```csharp
System.object IGetSeedComponentArray()
```

### C++/CLI

```cpp
System.Object^ IGetSeedComponentArray();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of seed component [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

You can use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html) to get the [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html) object for each seed component represented by a feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDerivedPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html)
[IDerivedPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.html)
[IDerivedPatternFeatureData::GetSeedComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~GetSeedComponentCount.html)
[IDerivedPatternFeatureData::ISetSeedComponentArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~ISetSeedComponentArray.html)
[IDerivedPatternFeatureData::SeedComponentArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~SeedComponentArray.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
