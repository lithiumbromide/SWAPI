---
title: "GetEditTargetTransform Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetEditTargetTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEditTargetTransform.html"
---

# GetEditTargetTransform Method (IMacroFeatureData)

Gets the transform of the component where the macro feature resides if at least one selection in the macro feature belongs to a different component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEditTargetTransform() As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As MathTransform

value = instance.GetEditTargetTransform()
```

### C#

```csharp
MathTransform GetEditTargetTransform()
```

### C++/CLI

```cpp
MathTransform^ GetEditTargetTransform();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) of the component where the macro feature resides if at least one selection in the macro feature belongs to a different component, or NULL if all of the selections in the macro feature belong to the component where the macro feature resides

## VBA Syntax

See [MacroFeatureData::GetEditTargetTransform](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetEditTargetTransform.html).

## Remarks

When [regenerating a macro feature](sldworksapiprogguide.chm::/Macro_Features/Rebuild_Function.htm) in a part that is a component in an assembly, you cannot get the component's transform where the macro feature resides because you cannot get the component using [IEntity::GetComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity~GetComponent.html) or [IEntity::IGetComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity~IGetComponent2.html) in a part document. However, you may need the component's transform because references from other components to it often need to be transformed.

This method provides this transform. If there are no external references among the macro feature selections ([IMacroFeatureData::GetSelections3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~GetSelections3.html) or [IMacroFeatureData::IGetSelections3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IGetSelections3.html)), then this method returns NULL. If there are external references among the macro feature selections, then this method returns the transform of the component where the macro feature resides.

For example, if the macro feature includes a selection box in which the user can select a face, and the user selects a face on a different component, then this method can get the component's transform where the macro feature resides. However, if all of the selections in the macro feature belong to the component where the macro feature resides, then this method returns NULL because you probably will not need the transform. See also [Macro Features and Component Transforms](sldworksapiprogguide.chm::/Macro_Features/Macro_Features_and_Component_Transforms.htm).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::FeatureTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~FeatureTransform.html)
[IMacroFeatureData::PatternTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PatternTransform.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
