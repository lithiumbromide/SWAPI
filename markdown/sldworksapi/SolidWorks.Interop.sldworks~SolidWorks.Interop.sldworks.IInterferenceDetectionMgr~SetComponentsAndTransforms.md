---
title: "SetComponentsAndTransforms Method (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "SetComponentsAndTransforms"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~SetComponentsAndTransforms.html"
---

# SetComponentsAndTransforms Method (IInterferenceDetectionMgr)

Sets the interfering components and their transforms.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetComponentsAndTransforms( _
   ByVal ComponentList As System.Object, _
   ByVal TransformList As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim ComponentList As System.Object
Dim TransformList As System.Object
Dim value As System.Integer

value = instance.SetComponentsAndTransforms(ComponentList, TransformList)
```

### C#

```csharp
System.int SetComponentsAndTransforms(
   System.object ComponentList,
   System.object TransformList
)
```

### C++/CLI

```cpp
System.int SetComponentsAndTransforms(
   System.Object^ ComponentList,
   System.Object^ TransformList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ComponentList`: Array of interfering [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)
- `TransformList`: Array of [transforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)

### Return Value

Status as defined by [swSetComponentsAndTransformsStatus_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSetComponentsAndTransformsStatus_e.html)

## VBA Syntax

See [InterferenceDetectionMgr::SetComponentsAndTransforms](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr~SetComponentsAndTransforms.html).

## Examples

[Set Components and Transforms for Interference Detection (C#)](Set_Components_and_Transforms_for_Interference_Detection_Example_CSharp.htm)
[Set Components and Transforms for Interference Detection (VB.NET)](Set_Components_and_Transforms_for_Interference_Detection_Example_VBNET.htm)
[Set Components and Transforms for Interference Detection (VBA)](Set_Components_and_Transforms_for_Interference_Detection_Example_VB.htm)

## Remarks

You must pass in absolute transforms to this method.

If you want to transform a component incrementally before interference detection, then you must multiply that incremental transform by the component's existing transform before passing in the resultant transform.

To produce the effect of identity transforms on components (i.e., the components do not move while participating in interference detection), the transforms for those components passed in can be null or Nothing. However, passing in null or Nothing for all of the transforms is interpreted as invalid input.

**NOTE:** A null or Nothing is interpreted as the component’s existing transform (i.e., an identity incremental transform).

## See Also

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html)
[IInterferenceDectectionMgr::GetComponentsAndTransforms Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsAndTransforms.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
