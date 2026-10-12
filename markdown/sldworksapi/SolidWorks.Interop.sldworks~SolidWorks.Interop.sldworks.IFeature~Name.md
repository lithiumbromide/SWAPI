---
title: "Name Property (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "Name"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.html"
---

# Name Property (IFeature)

Gets or sets the name of the current feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.String

instance.Name = value

value = instance.Name
```

### C#

```csharp
System.string Name {get; set;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the feature

## VBA Syntax

See [Feature::Name](ms-its:sldworksapivb6.chm::/sldworks~Feature~Name.html).

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)
[Get Parent Features (C++)](Get_Parent_Features_Example_CPlusPlus_COM.htm)
[Get Selected Feature (C++)](Get_Selected_Feature_Example_CPlusPlus_COM.htm)
[Get Sketches (C++)](Get_Sketches_Example_CPlusPlus_COM.htm)
[Find Total Length of Sketch Segments in Sketch (VBA)](Find_Total_Length_of_Sketch_Segments_in_Sketch_Example_VB.htm)
[Get Section Properties for Faces from Section Planes (VBA)](Get_Section_Properties_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VB.NET)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (C#)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VBA)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm)

## Remarks

Feature names can be seen in the FeatureManager design tree of any part or assembly.

Any change to a feature name is not visible to the user until a rebuild has been done. See [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html).

If you are setting the name of a feature, then the new name must be unique in the FeatureManager design tree. If the name is not unique, then the name is not changed. Also, the name cannot contain characters that are reserved by SOLIDWORKS.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetNameForSelection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNameForSelection.html)
