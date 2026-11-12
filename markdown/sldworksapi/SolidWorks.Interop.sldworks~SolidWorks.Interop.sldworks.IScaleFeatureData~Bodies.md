---
title: "Bodies Property (IScaleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScaleFeatureData"
member: "Bodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~Bodies.html"
---

# Bodies Property (IScaleFeatureData)

Gets or sets whether the bodies are scaled in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Property Bodies As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IScaleFeatureData
Dim value As System.Object

instance.Bodies = value

value = instance.Bodies
```

### C#

```csharp
System.object Bodies {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Bodies {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) that are scaled

## VBA Syntax

See [ScaleFeatureData::Bodies](ms-its:sldworksapivb6.chm::/sldworks~ScaleFeatureData~Bodies.html).

## Examples

[Get Faces Affected By Scale Feature (VBA)](Get_Faces_Affected_by_Scale_Feature_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.html)
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.html)
[IScaleFeatureData::GetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~GetBodiesCount.html)
[IScaleFeatureData::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~IGetBodies.html)
[IScaleFeatureData::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ISetBodies.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
