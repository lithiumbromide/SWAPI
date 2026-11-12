---
title: "AccessSelections Method (IMirrorSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorSolidFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~AccessSelections.html"
---

# AccessSelections Method (IMirrorSolidFeatureData)

Gains access to the selections that define the mirror solid feature.

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
Dim instance As IMirrorSolidFeatureData
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
- `Component`: Top-level document (see **Remarks**)

### Return Value

True if the selections were successfully accessed, false if not

## VBA Syntax

See [MirrorSolidFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~MirrorSolidFeatureData~AccessSelections.html).

## Examples

[Get Mirror Solid Feature Data (C#)](Get_Mirror_Solid_Feature_Data_Example_CSharp.htm)
[Get Mirror Solid Feature Data (VB.NET)](Get_Mirror_Solid_Feature_Data_Example_VBNET.htm)
[Get Mirror Solid Feature Data (VBA)](Get_Mirror_Solid_Data_Example_VB.htm)

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is Nothing or null |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) if you modified the feature
- [IMirrorSolidFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorSolidFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[IMirrorSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.html)
[IMirrorSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData_members.html)
[IMirrorSolidFeaturePattern::IAccessSelections2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~IAccessSelections2.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
