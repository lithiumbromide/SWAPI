---
title: "CreateAdvancedHoleElementData Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CreateAdvancedHoleElementData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateAdvancedHoleElementData.html"
---

# CreateAdvancedHoleElementData Method (IModelDocExtension)

Creates an Advanced Hole element data object of the specified type.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateAdvancedHoleElementData( _
   ByVal ElmType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim ElmType As System.Integer
Dim value As System.Object

value = instance.CreateAdvancedHoleElementData(ElmType)
```

### C#

```csharp
System.object CreateAdvancedHoleElementData(
   System.int ElmType
)
```

### C++/CLI

```cpp
System.Object^ CreateAdvancedHoleElementData(
   System.int ElmType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ElmType`: Advanced Hole element type as defined in [swAdvWzdGeneralHoleTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAdvWzdGeneralHoleTypes_e.html)

### Return Value

[IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html) (see **Remarks**)

## VBA Syntax

See [ModelDocExtension::CreateAdvancedHoleElementData](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~CreateAdvancedHoleElementData.html).

## Examples

[Create Advanced Hole Feature (VBA)](Create_Advanced_Hole_Example_VB.htm)
[Create Advanced Hole Feature (VB.NET)](Create_Advanced_Hole_Example_VBNET.htm)
[Create Advanced Hole Feature (C#)](Create_Advanced_Hole_Example_CSharp.htm)

## Remarks

After calling this method, use the IAdvancedHoleElementData object to get and set the properties common to all Advanced Hole elements. Cast the returned object using one of the following hole type-specific interfaces to set hole-specific properties:

- [ICounterboreElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData.html)
- [ICountersinkElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData.html)
- [IStraightElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.html)
- [IStraightTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.html)
- [ITaperedTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData.html)

To create and Advanced Hole, see the [IFeatureManager::AdvancedHole](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AdvancedHole.html) Remarks.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
