---
title: "SetEndConditionReference Method (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "SetEndConditionReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~SetEndConditionReference.html"
---

# SetEndConditionReference Method (IThreadFeatureData)

Sets the Up To Selection end condition reference of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEndConditionReference( _
   ByVal Value As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim Value As System.Object

instance.SetEndConditionReference(Value)
```

### C#

```csharp
void SetEndConditionReference(
   System.object Value
)
```

### C++/CLI

```cpp
void SetEndConditionReference(
   System.Object^ Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Value`: [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html), or planar [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html) (see **Remarks**)

## VBA Syntax

See [ThreadFeatureData::SetEndConditionReference](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~SetEndConditionReference.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

This method is valid only if [IThreadFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndCondition.html) is set to [swEndConditions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html).swEndCondUpToSelection.

Use [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.html) with Mark = 1 to select the end condition reference.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)
[IThreadFeatureData::GetEndConditionReference Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~GetEndConditionReference.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
