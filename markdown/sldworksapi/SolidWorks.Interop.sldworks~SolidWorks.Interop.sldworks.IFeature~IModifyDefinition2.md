---
title: "IModifyDefinition2 Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IModifyDefinition2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.html"
---

# IModifyDefinition2 Method (IFeature)

Updates the definition of a feature with the new values in an associated feature data object obtained with [IFeature::IGetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetDefinition.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IModifyDefinition2( _
   ByVal Data As System.Object, _
   ByVal TopDoc As ModelDoc2, _
   ByVal Component As Component2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim Data As System.Object
Dim TopDoc As ModelDoc2
Dim Component As Component2
Dim value As System.Boolean

value = instance.IModifyDefinition2(Data, TopDoc, Component)
```

### C#

```csharp
System.bool IModifyDefinition2(
   System.object Data,
   ModelDoc2 TopDoc,
   Component2 Component
)
```

### C++/CLI

```cpp
System.bool IModifyDefinition2(
   System.Object^ Data,
   ModelDoc2^ TopDoc,
   Component2^ Component
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Data`: IUnknown interface to the feature data object; use QueryInterface to get the interface to the actual object
- `TopDoc`: Top-level document (see **Remarks**)
- `Component`: Component for the feature (see **Remarks**)

### Return Value

True if the feature is updated successfully, false if not

## VBA Syntax

See [Feature::IModifyDefinition2](ms-its:sldworksapivb6.chm::/sldworks~Feature~IModifyDefinition2.html).

## Remarks

| To modify a feature in... | Then TopDoc argument... |
| --- | --- |
| A part | Is the IModelDoc2 object for the part and the Component argument should be Nothing or null |
| An assembly | Should be the assembly IModelDoc2 object and the Component argument should be the IComponent2 object in which the feature is to be modified |

When you modify a feature in an assembly, this method leaves the assembly in Editing Part mode. You can switch back to editing the assembly by calling [IAssemblyDoc::EditAssembly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~EditAssembly.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html)
[IFeature::ModifyDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
