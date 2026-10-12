---
title: "CreateSmartComponent Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "CreateSmartComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSmartComponent.html"
---

# CreateSmartComponent Method (IAssemblyDoc)

Creates a Smart Component.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSmartComponent( _
   ByVal ComponentIn As Component2, _
   ByVal RelatedComponents As System.Object, _
   ByVal RelatedFeatures As System.Object, _
   ByVal AutoSizeDiameter As System.Boolean, _
   ByVal LpMateReference As Entity, _
   ByVal BoundingValues As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim ComponentIn As Component2
Dim RelatedComponents As System.Object
Dim RelatedFeatures As System.Object
Dim AutoSizeDiameter As System.Boolean
Dim LpMateReference As Entity
Dim BoundingValues As System.Object
Dim value As System.Boolean

value = instance.CreateSmartComponent(ComponentIn, RelatedComponents, RelatedFeatures, AutoSizeDiameter, LpMateReference, BoundingValues)
```

### C#

```csharp
System.bool CreateSmartComponent(
   Component2 ComponentIn,
   System.object RelatedComponents,
   System.object RelatedFeatures,
   System.bool AutoSizeDiameter,
   Entity LpMateReference,
   System.object BoundingValues
)
```

### C++/CLI

```cpp
System.bool CreateSmartComponent(
   Component2^ ComponentIn,
   System.Object^ RelatedComponents,
   System.Object^ RelatedFeatures,
   System.bool AutoSizeDiameter,
   Entity^ LpMateReference,
   System.Object^ BoundingValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ComponentIn`: [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) to make smart
- `RelatedComponents`: Array of the components to associate with the Smart Component
- `RelatedFeatures`: Array of the [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) contained in the components to associate with the Smart Component
- `AutoSizeDiameter`: True to auto-size a cylindrical Smart Component that has multiple configurations, false to not
- `LpMateReference`: Concentric mate reference between a cylindrical face or axis and a feature
- `BoundingValues`: Array of doubles specifying minimum and maximum diameter values with which each configuration is compatible

### Return Value

True if the Smart Component is created, false if not

## VBA Syntax

See [AssemblyDoc::CreateSmartComponent](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~CreateSmartComponent.html).

## Examples

[Make Smart Component (VBA)](Make_Smart_Component_Example_VB.htm)
[Make Smart Component With Mate (VBA)](Make_Smart_Component_with__Mate_Example_VB.htm)

## Remarks

For example, a component with these configurations:

- TenInchDiameter
- ThirteenInchDiameter
- TwentyInchDiameter

might have a BoundingValues array of [9,11,12,14,19,21], which specifies a +1 tolerance over each configuration parameter.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::AddSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddSmartComponent.html)
[IComponent2::GetSmartComponentData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSmartComponentData.html)
[IComponent2::IsSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSmartComponent.html)
[IComponent2::SetSmartComponentData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSmartComponentData.html)
[ISmartComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
