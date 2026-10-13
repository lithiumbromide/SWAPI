---
title: "IThreadFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html"
---

# IThreadFeatureData Interface

Allows access to a thread feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IThreadFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
```

### C#

```csharp
public interface IThreadFeatureData
```

### C++/CLI

```cpp
public interface class IThreadFeatureData
```

## VBA Syntax

See [ThreadFeatureData](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData.html).

## Examples

[Create a Thread Feature (VBA)](Create_a_Thread_Feature_Example_VB.htm)
[Create a Thread Feature (VB.NET)](Create_a_Thread_Feature_Example_VBNET.htm)
[Create a Thread Feature (C#)](Create_a_Thread_Feature_Example_CSharp.htm)

## Remarks

This interface:

- Accesses the feature data for a thread created either inside a cylindrical hole or around a cylindrical rod.
- Is functionally similar to the Thread PropertyManager in the SOLIDWORKS Design user interface.

To create a Thread feature, see [Thread Features and ThreadFeatureData Objects](sldworksapiprogguide.chm::/OVERVIEW/Thread_Features_and_ThreadFeatureData_Objects.htm).

For more information, see the **Thread PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html) and [IFeature::IGetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetDefinition.html)

[IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html)

## Access Diagram

[ThreadFeatureData](SWObjectModel.pdf#ThreadFeatureData)

## See Also

[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::CreateFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html)
