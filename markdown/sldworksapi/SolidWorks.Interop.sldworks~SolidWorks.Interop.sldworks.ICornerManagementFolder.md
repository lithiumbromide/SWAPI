---
title: "ICornerManagementFolder Interface"
project: "SOLIDWORKS API Help"
interface: "ICornerManagementFolder"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html"
---

# ICornerManagementFolder Interface

Allows access to a corner management folder in a structure system.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICornerManagementFolder
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerManagementFolder
```

### C#

```csharp
public interface ICornerManagementFolder
```

### C++/CLI

```cpp
public interface class ICornerManagementFolder
```

## VBA Syntax

See [CornerManagementFolder](ms-its:sldworksapivb6.chm::/sldworks~CornerManagementFolder.html).

## Examples

[Access Structure System Corner Treatments (VBA)](Access_Structure_System_Corner_Treatments_Example_VB.htm)
[Access Structure System Corner Treatments (VB.NET)](Access_Structure_System_Corner_Treatments_Example_VB.htm)
[Access Structure System Corner Treatments (C#)](Access_Structure_System_Corner_Treatments__Example_CSharp.htm)

## Remarks

A Corner Management folder is automatically created in the FeatureManager design tree when a [structure system](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.html) is created.

For more information, see the **SOLIDWORKS Design user-interface help > Weldments and Structure System > Structure System > Corner Management** topic.

## Accessors

[IFeatureManager::GetCornerManagementFolders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetCornerManagementFolders.html) and then [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html)

## Access Diagram

[CornerManagementFolder](SWObjectModel.pdf#CornerManagementFolder)

## See Also

[ICornerManagementFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
