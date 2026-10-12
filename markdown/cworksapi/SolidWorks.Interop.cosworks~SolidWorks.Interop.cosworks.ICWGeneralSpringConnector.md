---
title: "ICWGeneralSpringConnector Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGeneralSpringConnector"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html"
---

# ICWGeneralSpringConnector Interface

Allows access to a general spring connector.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWGeneralSpringConnector
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGeneralSpringConnector
```

### C#

```csharp
public interface ICWGeneralSpringConnector
```

### C++/CLI

```cpp
public interface class ICWGeneralSpringConnector
```

## VBA Syntax

See [CWGeneralSpringConnector](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGeneralSpringConnector.html).

## Examples

[Add General Spring Connector (VBA)](Add_Orthotropic_Spring_Connector_Example_VB.htm)

## Remarks

This API:

- simulates more precisely a spring between two components whose surfaces may be flat, non-flat, or cylindrical.
- uses distributed coupling technology to establish a more realistic spring connector simulation.
- references a local coordinate system as you specify six stiffness parameters to accurately represent a general spring connector.
- requires at least one non-zero stiffness value be specified: [AxialStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~AxialStiffnessValue.html), [TorsionalStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~TorsionalStiffnessValue.html), [BendingStiffnessYValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~BendingStiffnessYValue.html), [BendingStiffnessZValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~BendingStiffnessZValue.html), [LateralStiffnessYValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~LateralStiffnessYValue.html), [LateralStiffnessZValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~LateralStiffnessZValue.html)
- works only in linear static, linear dynamic, frequency, and buckling study types.

- is available only with Simulation Professional and Simulation Premium licenses.

For more information, see the **SOLIDWORKS > Simulation > Loads and Restraints > Connectors** online help.

## Accessors

[ICWLoadsAndRestraintsManager::AddGeneralSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddGeneralSpringConnector.html)

[ICWLoadsAndRestraintsManager::GetGeneralSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetGeneralSpringConnector.html)

## See Also

[ICWGeneralSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
