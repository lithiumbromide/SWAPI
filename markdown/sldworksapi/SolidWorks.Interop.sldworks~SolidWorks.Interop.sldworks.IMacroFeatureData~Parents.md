---
title: "Parents Property (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "Parents"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~Parents.html"
---

# Parents Property (IMacroFeatureData)

Gets or sets the parent features for this macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Parents As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.Object

instance.Parents = value

value = instance.Parents
```

### C#

```csharp
System.object Parents {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Parents {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of parent [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) for this macro feature

## VBA Syntax

See [MacroFeatureData::Parents](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~Parents.html).

## Remarks

Parent features set by this property are not persistent when the macro feature is regenerated. Reset the parent features in the [SwComFeature::Regenerate](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwComFeature~Regenerate.html) handler.

| To get the parent features... | Use... |
| --- | --- |
| assigned to a macro feature by IMacroFeatureData::Parents or IMacroFeatureData::ISetParents | IMacroFeatureData::Parents or IMacroFeatureData::IGetParents - or- IFeature::GetParents or IFeature::IGetParents |
| of a macro feature created by first selecting objects and then calling IFeatureManager::InsertMacroFeature3 or IFeatureManager::IInsertMacroFeature3 | IMacroFeatureData::GetSelections3 or IMacroFeatureData::IGetSelections3 - or - IFeature::GetParents or IFeature::IGetParents |

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetParentsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParentsCount.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
