---
title: "GetComponentCount Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetComponentCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentCount.html"
---

# GetComponentCount Method (IAssemblyDoc)

Gets the number of components in the active configuration of this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentCount( _
   ByVal ToplevelOnly As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim ToplevelOnly As System.Boolean
Dim value As System.Integer

value = instance.GetComponentCount(ToplevelOnly)
```

### C#

```csharp
System.int GetComponentCount(
   System.bool ToplevelOnly
)
```

### C++/CLI

```cpp
System.int GetComponentCount(
   System.bool ToplevelOnly
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ToplevelOnly`: True to get only the number of components at the top level of the FeatureManager design tree, false to get the number of top level and all child components in the FeatureManager design tree

### Return Value

Number of components

## VBA Syntax

See [AssemblyDoc::GetComponentCount](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetComponentCount.html).

## Remarks

Use this method before using [IAssemblyDoc::IGetComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IGetComponents.html) to determine the size of the array to pass into that method.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IComponent2::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetChildren.html)
[IComponent2::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetParent.html)
[IConfiguration::GetRootComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.html)
[IConfiguration::IGetRootComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetRootComponent2.html)
[IConfigurationManager::AddConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddConfiguration.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
