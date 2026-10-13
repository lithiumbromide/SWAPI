---
title: "IWeldmentBeadFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html"
---

# IWeldmentBeadFeatureData Interface

Allows access to a weldment bead feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IWeldmentBeadFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData
```

### C#

```csharp
public interface IWeldmentBeadFeatureData
```

### C++/CLI

```cpp
public interface class IWeldmentBeadFeatureData
```

## VBA Syntax

See [WeldmentBeadFeatureData](ms-its:sldworksapivb6.chm::/sldworks~WeldmentBeadFeatureData.html).

## Examples

[Modify Fillet Weld Bead (VBA)](Modify_Fillet_Weld_Bead_Example_VB.htm)
[Modify Fillet Weld Bead (VB.NET)](Modify_Fillet_Weld_Bead_Example_VBNET.htm)
[Modify Fillet Weld Bead (C#)](Modify_Fillet_Weld_Bead_Example_CSharp.htm)

## Remarks

A bead can be applied to two sides: arrow or other. All of these methods and properties use one of these sides as input. A staggered type of weld bead requires applying the weld bead to both sides.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html) and [IFeature::IGetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetDefinition.html)

## Access Diagram

[WeldmentBeadFeatureData](SWObjectModel.pdf#WeldmentBeadFeatureData)

## See Also

[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertFilletBeadFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFilletBeadFeature.html)
[IWeldBead Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead.html)
[IFeatureManager::InsertFilletBeadFeature3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFilletBeadFeature3.html)
[IAssemblyDoc::InsertWeld Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertWeld.html)
[IAssemblyDoc::InsertWeld2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertWeld2.html)
