---
title: "GetEndConditionReference Method (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "GetEndConditionReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~GetEndConditionReference.html"
---

# GetEndConditionReference Method (IThreadFeatureData)

Gets the Up To Selection end condition reference of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEndConditionReference() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Object

value = instance.GetEndConditionReference()
```

### C#

```csharp
System.object GetEndConditionReference()
```

### C++/CLI

```cpp
System.Object^ GetEndConditionReference();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html), or planar [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)

## VBA Syntax

See [ThreadFeatureData::GetEndConditionReference](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~GetEndConditionReference.html).

## Remarks

This method is valid only if [IThreadFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndCondition.html) is set to [swEndConditions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html).swEndCondUpToSelection

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)
[IThreadFeatureData::SetEndConditionReference Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~SetEndConditionReference.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
