---
title: "GetComponentsTransformInterferenceCount Method (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "GetComponentsTransformInterferenceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsTransformInterferenceCount.html"
---

# GetComponentsTransformInterferenceCount Method (IInterferenceDetectionMgr)

Calculates and gets the number of interfering components for the specified components and math transform.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentsTransformInterferenceCount( _
   ByVal NumOfComponent As System.Integer, _
   ByRef Component As Component2, _
   ByRef Transform As MathTransform _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim NumOfComponent As System.Integer
Dim Component As Component2
Dim Transform As MathTransform
Dim value As System.Integer

value = instance.GetComponentsTransformInterferenceCount(NumOfComponent, Component, Transform)
```

### C#

```csharp
System.int GetComponentsTransformInterferenceCount(
   System.int NumOfComponent,
   ref Component2 Component,
   ref MathTransform Transform
)
```

### C++/CLI

```cpp
System.int GetComponentsTransformInterferenceCount(
   System.int NumOfComponent,
   Component2^% Component,
   MathTransform^% Transform
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfComponent`: Number of components in the Component array
- `Component`: Array of [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)s
- `Transform`: [IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

### Return Value

Number of interfering components

## VBA Syntax

See [InterferenceDetectionMgr::GetComponentsTransformInterferenceCount](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr~GetComponentsTransformInterferenceCount.html).

## Remarks

Call this method before calling [IInterferenceDetectionMgr::IGetComponentsTransformInterference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IInterferenceDetectionMgr~IGetComponentsTransformInterference.html) to get the size of the array returned by that method.

## See Also

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html)
[IInterferenceDetectionMgr::GetComponentsTransformInterferenceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsTransformInterferenceCount.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
