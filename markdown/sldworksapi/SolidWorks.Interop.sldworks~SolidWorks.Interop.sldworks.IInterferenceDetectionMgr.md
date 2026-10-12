---
title: "IInterferenceDetectionMgr Interface"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html"
---

# IInterferenceDetectionMgr Interface

Allows you to run interference detection on an assembly to determine whether components interfere with each other.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IInterferenceDetectionMgr
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
```

### C#

```csharp
public interface IInterferenceDetectionMgr
```

### C++/CLI

```cpp
public interface class IInterferenceDetectionMgr
```

## VBA Syntax

See [InterferenceDetectionMgr](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr.html).

## Examples

[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)
[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)
[Detect Interferences Using a Transform (C#)](Detect_Interferences_Using_a_Transform_Example_CSharp.htm)
[Detect Interferences Using a Transform (VB.NET)](Detect_Interferences_Using_a_Transform_Example_VBNET.htm)
[Detect Interferences Using a Transform (VBA)](Detect_Interferences_Using_a_Transform_Example_VB.htm)
[Set Components and Transforms for Interference Detection (C#)](Set_Components_and_Transforms_for_Interference_Detection_Example_CSharp.htm)
[Set Components and Transforms for Interference Detection (VB.NET)](Set_Components_and_Transforms_for_Interference_Detection_Example_VBNET.htm)
[Set Components and Transforms for Interference Detection (VBA)](Set_Components_and_Transforms_for_Interference_Detection_Example_VB.htm)

## Remarks

See the SOLIDWORKS Help for details about interference detection.

Use [ICollisionDetectionManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.html) to perform high-efficiency collision detection among groups of components transformed to a variety of positions.

## Accessors

[IAssemblyDoc::InterferenceDetectionManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~InterferenceDetectionManager.html)

## Access Diagram

[InterferenceDetectionMgr](SWObjectModel.pdf#InterferenceDetectionMgr)

## See Also

[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IInterference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference.html)
[IModeler::CheckInterferenceBetweenTwoBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterferenceBetweenTwoBodies.html)
