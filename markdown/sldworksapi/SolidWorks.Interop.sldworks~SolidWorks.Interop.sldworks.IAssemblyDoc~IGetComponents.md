---
title: "IGetComponents Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IGetComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetComponents.html"
---

# IGetComponents Method (IAssemblyDoc)

Gets all of the components in the active configuration of this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetComponents( _
   ByVal ToplevelOnly As System.Boolean, _
   ByVal Count As System.Integer _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim ToplevelOnly As System.Boolean
Dim Count As System.Integer
Dim value As Component2

value = instance.IGetComponents(ToplevelOnly, Count)
```

### C#

```csharp
Component2 IGetComponents(
   System.bool ToplevelOnly,
   System.int Count
)
```

### C++/CLI

```cpp
Component2^ IGetComponents(
   System.bool ToplevelOnly,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ToplevelOnly`: True to get only the number of components at the top level of the FeatureManager design tree, false to get the number of top level and all child components in the FeatureManager design tree
- `Count`: Number of components

### Return Value

- in-process, unmanaged C++: Pointer to an array of [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before using this method, use [IAssemblyDoc::GetComponentCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~GetComponentCount.html) to determine the size of the array to pass to this method.

The components returned by this method can be in any order. You should not rely on the order to indicate anything about children or parents. If the hierarchy and order are important, then use [IModelDoc2::FirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FirstFeature.html), [IFeature::GetTypeName2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetTypeName2.html), [IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html), [IComponent2::FirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~FirstFeature.html), and [IFeature::GetNextFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetNextFeature.html) to retrieve your information.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IComponent2::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetChildren.html)
[IComponent2::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetParent.html)
[IConfiguration::GetRootComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.html)
[IConfiguration::IGetRootComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetRootComponent2.html)
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html)
[IAssemblyDoc::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponents.html)
[IAssemblyDoc::GetComponentByID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByID.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.
