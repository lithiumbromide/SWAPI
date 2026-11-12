---
title: "ISetFeatureScopeBodies Method (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "ISetFeatureScopeBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ISetFeatureScopeBodies.html"
---

# ISetFeatureScopeBodies Method (IWizardHoleFeatureData2)

Sets the solid bodies that the Hole Wizard feature affects in the multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetFeatureScopeBodies( _
   ByVal Count As System.Integer, _
   ByRef BodyArr As Body2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim Count As System.Integer
Dim BodyArr As Body2

instance.ISetFeatureScopeBodies(Count, BodyArr)
```

### C#

```csharp
void ISetFeatureScopeBodies(
   System.int Count,
   ref Body2 BodyArr
)
```

### C++/CLI

```cpp
void ISetFeatureScopeBodies(
   System.int Count,
   Body2^% BodyArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of solid bodies to affect
- `BodyArr`: Array of solid [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) of size Count

## VBA Syntax

See [WizardHoleFeatureData2::ISetFeatureScopeBodies](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~ISetFeatureScopeBodies.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetFeatureScopeBodiesCount.html)
[IWizardHoleFeatureData2::IGetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~IGetFeatureScopeBodies.html)
[IWizardHoleFeatureData2::FeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FeatureScope.html)
[IWizardHoleFeatureData2::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FeatureScopeBodies.html)
[IWizardHoleFeatureData2::Vertex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Vertex.html)
[IWizardHoleFeatureData2::IVertex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~IVertex.html)

## Availability

SOLIDWORKS 206 FCS, Revision Number 14.0
