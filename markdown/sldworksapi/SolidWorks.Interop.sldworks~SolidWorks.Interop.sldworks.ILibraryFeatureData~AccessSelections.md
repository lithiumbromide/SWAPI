---
title: "AccessSelections Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~AccessSelections.html"
---

# AccessSelections Method (ILibraryFeatureData)

Gains access to selections that define this library feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function AccessSelections( _
   ByVal PTopDoc As ModelDoc2, _
   ByVal PComponent As Component2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim PTopDoc As ModelDoc2
Dim PComponent As Component2
Dim value As System.Boolean

value = instance.AccessSelections(PTopDoc, PComponent)
```

### C#

```csharp
System.bool AccessSelections(
   ModelDoc2 PTopDoc,
   Component2 PComponent
)
```

### C++/CLI

```cpp
System.bool AccessSelections(
   ModelDoc2^ PTopDoc,
   Component2^ PComponent
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PTopDoc`: Top-level document (see **Remarks**)
- `PComponent`: Component in which the feature is to be modified (see **Remarks**)

### Return Value

True if the selections were successfully accessed, false if not

## VBA Syntax

See [LibraryFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~AccessSelections.html).

## Examples

[Get Library Feature Data (VBA)](Get_Library_Feature_Data_Example_VB.htm)
[Get Library Feature Data (VB.NET)](Get_Library_Feature_Data_Example_VBNET.htm)
[Get Library Feature Data (C#)](Get_Library_Feature_Data_Example_CSharp.htm)

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | PTopDoc argument is the IModelDoc2 for the part PComponent argument is NULL |
| Assembly | PTopDoc is the IModelDoc2 object for the assembly PComponent argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [ILibraryFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILibraryFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
