---
title: "IGetDefinition Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IGetDefinition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetDefinition.html"
---

# IGetDefinition Method (IFeature)

Gets the feature data object for a feature, such as an extrusion, loft, fillet, chamfer, etc., in order to access the parameters that control the definition of this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDefinition() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Object

value = instance.IGetDefinition()
```

### C#

```csharp
System.object IGetDefinition()
```

### C++/CLI

```cpp
System.Object^ IGetDefinition();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

IUnknown interface to the feature data object; use QueryInterface to get the interface to the actual object (see **Remarks**)

## VBA Syntax

See [Feature::IGetDefinition](ms-its:sldworksapivb6.chm::/sldworks~Feature~IGetDefinition.html).

## Remarks

You can use this method to query the feature data object, and you can modify the feature data object using [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html). Set the feature data object to null when it is no longer needed. Not all feature types are supported, so check to see that the returned object is valid.

To:

- get the type of feature and the name of its associated interface, use [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.html) or [IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.html).
- see a complete list of interfaces for feature data objects (e.g., interfaces ending in FeatureData or FeatureData2, such as IExtrudeFeatureData2, ILoftFeatureData, ISimpleFilletFeatureData2, IChamferFeatureData2, etc.), see the **Features Interfaces** section in [Functional Categories](FunctionalCategories-sldworksapi.html).
- get the object of a feature that is not a feature data object, use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html)
[IFeature::IModifyDefinition2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.html)
[IFeature::ModifyDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html)
