---
title: "EnableMultiBodyConsume Property (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "EnableMultiBodyConsume"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EnableMultiBodyConsume.html"
---

# EnableMultiBodyConsume Property (IMacroFeatureData)

Gets or sets whether to replace the original edit body with multiple solid bodies created during regeneration of a multibody macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableMultiBodyConsume As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.Boolean

instance.EnableMultiBodyConsume = value

value = instance.EnableMultiBodyConsume
```

### C#

```csharp
System.bool EnableMultiBodyConsume {get; set;}
```

### C++/CLI

```cpp
property System.bool EnableMultiBodyConsume {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to replace the original edit body with multiple solid bodies, false to not

## VBA Syntax

See [MacroFeatureData::EnableMultiBodyConsume](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~EnableMultiBodyConsume.html).

## Examples

[Create Multibody Macro Feature (VBA)](Create_Multibody_Macro_Feature_Example_VB.htm)
[Create Multibody Macro Feature (VB.NET)](Create_Multibody_Macro_Feature_Example_VBNET.htm)
[Create Multibody Macro Feature (C#)](Create_Multibody_Macro_Feature_Example_CSharp.htm)

## Remarks

This method was designed to work specifically with macro features that generate multiple solid bodies. The [rebuild](sldworksapiprogguide.chm::/Macro_Features/Rebuild_Function.htm) function of a macro feature creates or regenerates the macro feature in the FeatureManager design tree. By default, if the rebuild function creates multiple solid bodies, it appends the new solid bodies to the original edit body in the Solid Bodies folder of the FeatureManager design tree.

Always set this property to true in the rebuild function when working with macro features involving multiple input or output bodies.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetEditBodiesCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEditBodiesCount.html)
[IMacroFeatureData::IGetEditBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetEditBodies.html)
[IMacroFeatureData::EditBodies Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EditBodies.html)

## Availability

SOLIDWORKS 2013 SP05, Revision Number 21.5
