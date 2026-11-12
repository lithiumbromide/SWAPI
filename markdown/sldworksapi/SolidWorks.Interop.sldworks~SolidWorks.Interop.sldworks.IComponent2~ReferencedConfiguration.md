---
title: "ReferencedConfiguration Property (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "ReferencedConfiguration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedConfiguration.html"
---

# ReferencedConfiguration Property (IComponent2)

Gets or sets the active configuration used by this component.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferencedConfiguration As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.String

instance.ReferencedConfiguration = value

value = instance.ReferencedConfiguration
```

### C#

```csharp
System.string ReferencedConfiguration {get; set;}
```

### C++/CLI

```cpp
property System.String^ ReferencedConfiguration {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the configuration

## VBA Syntax

See [Component2::ReferencedConfiguration](ms-its:sldworksapivb6.chm::/sldworks~Component2~ReferencedConfiguration.html).

## Examples

[Get Names of Bodies in Multibody Part (VBA)](Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm)
[Get Transforms of Assembly Components (VBA)](Get_Transforms_of_Assembly_Components_Example_VB.htm)
[Change Referenced Configuration (VBA)](Change_Referenced_Configuration_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VBA)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VB.NET)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (C#)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm)

## Remarks

You can use this property to change the active configuration of:

- a pattern seed component.
- pattern instance components, but only when the pattern's ForceUseSeedConfiguration property is set to false.

When the configuration is changed, components might become suppressed or unsuppressed. This means that the array previously returned from [IComponent2::GetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetChildren.html) or [IComponent2::IGetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetChildren.html) becomes invalid. If an application is traversing an assembly and calls IComponent2::ReferencedConfiguration, then it should stop the traversal and start again by getting the assembly's [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) and active configuration. The array previously returned from IComponent2::GetChildren or IComponent2::IGetChildren should be released before calling IComponent2::ReferencedConfiguration. To hold onto the changed component, you can perform an extra AddRef() on that component before freeing the array.

After changing the referenced configuration, you must call [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) to display the changes.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::CompConfigProperties5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties5.html)
[IChainPatternFeatureData::ForceUseSeedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~ForceUseSeedConfiguration.html)
[IDerivedPatternFeatureData::ForceUseSeedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~ForceUseSeedConfiguration.html)
[ILocalCircularPatternFeatureData::ForceUseSeedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ForceUseSeedConfiguration.html)
[ILocalCurvePatternFeatureData::ForceUseSeedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~ForceUseSeedConfiguration.html)
[ILocalLinearPatternFeatureData::ForceUseSeedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~ForceUseSeedConfiguration.html)
[ILocalSketchPatternFeatureData::ForceUseSeedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~ForceUseSeedConfiguration.html)
[IMirrorComponentFeatureData::ForceUseSeedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ForceUseSeedConfiguration.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
