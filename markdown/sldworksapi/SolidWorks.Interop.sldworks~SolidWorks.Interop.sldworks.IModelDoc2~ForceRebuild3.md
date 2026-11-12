---
title: "ForceRebuild3 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ForceRebuild3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html"
---

# ForceRebuild3 Method (IModelDoc2)

Forces a rebuild of all features in the active configuration in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function ForceRebuild3( _
   ByVal TopOnly As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim TopOnly As System.Boolean
Dim value As System.Boolean

value = instance.ForceRebuild3(TopOnly)
```

### C#

```csharp
System.bool ForceRebuild3(
   System.bool TopOnly
)
```

### C++/CLI

```cpp
System.bool ForceRebuild3(
   System.bool TopOnly
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TopOnly`: True rebuilds the top-level assembly only; false rebuilds the top-level assembly and all subassemblies

### Return Value

True if all features in the active configuration at the specified assembly level in the model are rebuilt, false if not

## VBA Syntax

See [ModelDoc2::ForceRebuild3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ForceRebuild3.html).

## Examples

[Force Rebuild (VBA)](Force_Rebuild_Example_VB.htm)
[Iterate Through All Configurations (VBA)](Iterate_Through_All_Configurations_Example_VB.htm)
[Rebuild All Configurations (VBA)](Rebuild_All_Configurations_Example_VB.htm)
[Rebuild Model (VBA)](Rebuild_Example_VB.htm)
[Set Dimensions to Mid-Tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)
[Use Safe Entity (VBA)](Use_Safe_Entity_Example_VB.htm)
[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::EditRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.html)
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)
[IModelDoc2::Rebuild Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Rebuild.html)
[IModelDoc2::ShowFeatureErrorDialog Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowFeatureErrorDialog.html)
[IConfiguration::AddRebuildSaveMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRebuildSaveMark.html)
[IConfiguration::NeedsRebuild Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.html)
[IModelDocExtension::EditRebuildAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditRebuildAll.html)
[IModelDocExtension::ForceRebuildAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ForceRebuildAll.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
