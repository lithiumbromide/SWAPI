---
title: "GetComponentsAndTransforms Method (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "GetComponentsAndTransforms"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsAndTransforms.html"
---

# GetComponentsAndTransforms Method (IInterferenceDetectionMgr)

Gets the interfering components and their transforms.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentsAndTransforms( _
   ByRef ComponentList As System.Object, _
   ByRef TransformList As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim ComponentList As System.Object
Dim TransformList As System.Object
Dim value As System.Boolean

value = instance.GetComponentsAndTransforms(ComponentList, TransformList)
```

### C#

```csharp
System.bool GetComponentsAndTransforms(
   out System.object ComponentList,
   out System.object TransformList
)
```

### C++/CLI

```cpp
System.bool GetComponentsAndTransforms(
   [Out] System.Object^ ComponentList,
   [Out] System.Object^ TransformList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ComponentList`: Array of interfering [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)
- `TransformList`: Array of [transforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)

### Return Value

True if successful, false if not

## VBA Syntax

See [InterferenceDetectionMgr::GetComponentsAndTransforms](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr~GetComponentsAndTransforms.html).

## Examples

[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)
[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)

## See Also

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html)
[IInterferenceDectectionMgr::SetComponentsAndTransforms Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~SetComponentsAndTransforms.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
