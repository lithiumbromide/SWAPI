---
title: "AccessSelections Method (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~AccessSelections.html"
---

# AccessSelections Method (ISheetMetalFeatureData)

Gains access to the selections that define this sheet metal feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function AccessSelections( _
   ByVal TopDoc As System.Object, _
   ByVal Component As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim TopDoc As System.Object
Dim Component As System.Object
Dim value As System.Boolean

value = instance.AccessSelections(TopDoc, Component)
```

### C#

```csharp
System.bool AccessSelections(
   System.object TopDoc,
   System.object Component
)
```

### C++/CLI

```cpp
System.bool AccessSelections(
   System.Object^ TopDoc,
   System.Object^ Component
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TopDoc`: Top-level document (see **Remarks**)
- `Component`: Component in which the feature is to be modified (see **Remarks**)

### Return Value

True if the selections were successfully accessed, false if not

## VBA Syntax

See [SheetMetalFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~AccessSelections.html).

## Examples

[Change Bend Radius of Sheet Metal Part (VBA)](Change_Bend_Radius_of_Sheet_Metal_Part_Example_VB.htm)
[Get Fixed Face of Sheet Metal Part (VBA)](Get_Fixed_Face_of_Sheet_Metal_Part_Example_VB.htm)

## Remarks

To access sheet metal feature data in sheet metal models created in SOLIDWORKS 2013 or later, follow the examples of [IModelDocExtension::GetTemplateSheetMetal](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetTemplateSheetMetal.html).

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is NULL |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [ISheetMetalFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheetMetalFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)
[ISheetMetalFeatureData::IAccessSelections2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~IAccessSelections2.html)

## Availability

SOLIDWORKS 2001 SP1, Revision Number 9.1
