---
title: "ILinearCouplerMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ILinearCouplerMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.html"
---

# ILinearCouplerMateFeatureData Interface

Allows access to linear/linear coupler mate feature data.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ILinearCouplerMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearCouplerMateFeatureData
```

### C#

```csharp
public interface ILinearCouplerMateFeatureData
```

### C++/CLI

```cpp
public interface class ILinearCouplerMateFeatureData
```

## VBA Syntax

See [LinearCouplerMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~LinearCouplerMateFeatureData.html).

## Examples

[Create and Edit Linear-Linear Coupler Mate (VBA)](Create_Linear_Coupler_Mate_Example_VB.htm)
[Create and Edit Linear-Linear Coupler Mate (C#)](Create_Linear_Coupler_Mate_Example_CSharp.htm)

## Remarks

SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html

A linear/linear coupler mate establishes a relationship between the translation of one component and the translation of another component.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this advanced mate interface.

To create a linear/linear coupler mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Specify [ILinearCouplerMateFeatureData::MateEntity1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~MateEntity1.html) and [ILinearCouplerMateFeatureData::MateEntity2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~MateEntity2.html).
3. Specify other properties of the LinearCouplerMateFeatureData object as required.

To edit a linear/linear coupler mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a LinearCouplerMateFeatureData object.
3. Modify the LinearCouplerMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete a linear/linear coupler mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[LinearCouplerMateFeatureData](SWObjectModel.pdf#LinearCouplerMateFeatureData)

## See Also

[ILinearCouplerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
