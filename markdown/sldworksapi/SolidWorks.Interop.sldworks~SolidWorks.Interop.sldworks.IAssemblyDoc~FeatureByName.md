---
title: "FeatureByName Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "FeatureByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~FeatureByName.html"
---

# FeatureByName Method (IAssemblyDoc)

Returns the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object for the named feature in the assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureByName( _
   ByVal Name As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Name As System.String
Dim value As System.Object

value = instance.FeatureByName(Name)
```

### C#

```csharp
System.object FeatureByName(
   System.string Name
)
```

### C++/CLI

```cpp
System.Object^ FeatureByName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the feature

### Return Value

Object for the feature

## VBA Syntax

See [AssemblyDoc::FeatureByName](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~FeatureByName.html).

## Examples

[Get Parent-Child Relationship for Component (VBA)](Get_Parent-Child_Relationship_for_Component_Example_VB.htm)
[Create and Name Plane (VBA)](Create_and_Name_Plane_Example_VB.htm)
[Move Assembly Components to New Folder (C#)](Move_Assembly_Components_to_New_Folder_Example_CSharp.htm)
[Move Assembly Components to New Folder (VB.NET)](Move_Assembly_Components_to_New_Folder_Example_VBNET.htm)
[Move Assembly Components to New Folder (VBA)](Move_Assembly_Components_to_New_Folder_Example_VB.htm)
[Roll Back Model (C#)](Roll_Back_Model_Example_CSharp.htm)
[Roll Back Model (VB.NET)](Roll_Back_Model_Example_VBNET.htm)
[Roll Back Model (VBA)](Roll_Back_Model_Example_VB.htm)
[Suppress Component Feature (C#)](Suppress_Component_Feature_Example_CSharp.htm)
[Suppress Component Feature (VB.NET)](Suppress_Component_Feature_Example_VBNET.htm)
[Suppress Component Feature (VBA)](Suppress_Component_Feature_Example_VB.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::IFeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IFeatureByName.html)
