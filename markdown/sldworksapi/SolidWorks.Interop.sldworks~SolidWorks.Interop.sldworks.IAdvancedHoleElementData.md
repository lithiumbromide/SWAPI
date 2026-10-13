---
title: "IAdvancedHoleElementData Interface"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleElementData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html"
---

# IAdvancedHoleElementData Interface

Allows access to Advanced Hole element data.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IAdvancedHoleElementData
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleElementData
```

### C#

```csharp
public interface IAdvancedHoleElementData
```

### C++/CLI

```cpp
public interface class IAdvancedHoleElementData
```

## VBA Syntax

See [AdvancedHoleElementData](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleElementData.html).

## Examples

[Create Advanced Hole Feature (VBA)](Create_Advanced_Hole_Example_VB.htm)
[Create Advanced Hole Feature (VB.NET)](Create_Advanced_Hole_Example_VBNET.htm)
[Create Advanced Hole Feature (C#)](Create_Advanced_Hole_Example_CSharp.htm)

## Remarks

IAdvancedHoleElementData is extended by the following:

- [ICounterboreElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData.html)
- [ICountersinkElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData.html)
- [IStraightElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.html)
- [IStraightTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.html)
- [ITaperedTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData.html)

After accessing the IAdvancedHoleElementData object, cast it to a hole type-specific object using one of the interfaces above and set the hole type-specific properties.

To create an Advanced Hole feature, see the [IFeatureManager::AdvancedHole](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AdvancedHole.html) Remarks.

## Accessors

[IModelDocExtension::CreateAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateAdvancedHoleElementData.html)

## Access Diagram

[AdvancedHoleElementData](SWObjectModel.pdf#AdvancedHoleElementData)

## See Also

[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IAdvancedHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.html)
