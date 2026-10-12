---
title: "FeatureByName Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "FeatureByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureByName.html"
---

# FeatureByName Method (IPartDoc)

Gets the named feature in the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureByName( _
   ByVal Name As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Name As System.String
Dim value As System.Object

value = instance.FeatureByName(Name)
```

### C#

```csharp
System.object FeatureByName(
   System.string Name
)
```

### C++/CLI

```cpp
System.Object^ FeatureByName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of feature

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [PartDoc::FeatureByName](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~FeatureByName.html).

## Examples

[Autodimension All Sketches (VBA)](Autodimension_All_Sketches_Example_VB.htm)
[Get and Set Constraint for Dome Feature (VBA)](Get_and_Set_Constraint_for_Dome_Feature_Example_VB.htm)
[Move Copy Sketch Entities (C#)](Move_Copy_Sketch_Entities_Example_CSharp.htm)
[Move Copy Sketch Entities (VB.NET)](Move_Copy_Sketch_Entities_Example_VBNET.htm)
[Move Copy Sketch Entities (VBA)](Move_Copy_Sketch_Entities_Example_VB.htm)
[Roll Back Model (C#)](Roll_Back_Model_Example_CSharp.htm)
[Roll Back Model (VB.NET)](Roll_Back_Model_Example_VBNET.htm)
[Roll Back Model (VBA)](Roll_Back_Model_Example_VB.htm)
[Suppress Component Feature (C#)](Suppress_Component_Feature_Example_CSharp.htm)
[Suppress Component Feature (VB.NET)](Suppress_Component_Feature_Example_VBNET.htm)
[Suppress Component Feature (VBA)](Suppress_Component_Feature_Example_VB.htm)

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::IFeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFeatureByName.html)
[IPartDoc::IFeatureById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFeatureById.html)
[IPartDoc::FeatureById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureById.html)
[IAssemblyDoc::FeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~FeatureByName.html)
[IAssemblyDoc::IFeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IFeatureByName.html)
[IComponent2::FeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FeatureByName.html)
[IDrawingDoc::FeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~FeatureByName.html)
[IDrawingDoc::IFeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IFeatureByName.html)
