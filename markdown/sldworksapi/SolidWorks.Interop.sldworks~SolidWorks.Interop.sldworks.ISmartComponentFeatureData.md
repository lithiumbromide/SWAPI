---
title: "ISmartComponentFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ISmartComponentFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData.html"
---

# ISmartComponentFeatureData Interface

Allows access to a Smart Component.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISmartComponentFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ISmartComponentFeatureData
```

### C#

```csharp
public interface ISmartComponentFeatureData
```

### C++/CLI

```cpp
public interface class ISmartComponentFeatureData
```

## VBA Syntax

See [SmartComponentFeatureData](ms-its:sldworksapivb6.chm::/sldworks~SmartComponentFeatureData.html).

## Examples

[Delete Smart Feature (VBA)](Delete_Smart_Feature_Example_VB.htm)
[Delete Smart Feature (VB.NET)](Delete_Smart_Feature_Example_VBNET.htm)
[Delete Smart Feature (C#)](Delete_Smart_Feature_Example_CSharp.htm)

## Remarks

A Smart Component is defined by:

- Components
- Features
- Feature references

A Smart Component is created in a training assembly. When the Smart Component is saved, it is saved with the training assembly in a SOLIDWORKS part.

When the Smart Component is inserted or edited in a target assembly, the training assembly opens in a small preview window, and the PropertyManager page of the Smart Component displays.

See the SOLIDWORKS Help for more information about Smart Components.

| Use... | To... |
| --- | --- |
| This interface | Gain access to the training assembly of a Smart Component. Gain access to the selection lists on the PropertyManager page of a Smart Component. Insert features and components into a Smart Component. Delete features and components from a Smart Component. |
| IComponent2::GetSmartComponentData | Get the current features, components, and feature references of a Smart Component. |
| IComponent2::SetSmartComponentData | Change which features and components to enable in a Smart Component and to insert Smart Features in a target assembly. |

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html) and [IFeature::IGetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetDefinition.html)

## Access Diagram

[SmartComponentFeatureData](SWObjectModel.pdf#SmartComponentFeatureData)

## See Also

[ISmartComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IComponent2::IsSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSmartComponent.html)
