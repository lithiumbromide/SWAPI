---
title: "GetComponentsTransformInterference Method (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "GetComponentsTransformInterference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsTransformInterference.html"
---

# GetComponentsTransformInterference Method (IInterferenceDetectionMgr)

Calculates and gets the interfering components for the specified components and math transform.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentsTransformInterference( _
   ByVal Component As System.Object, _
   ByVal Transform As System.Object, _
   ByRef InterferingComponent As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim Component As System.Object
Dim Transform As System.Object
Dim InterferingComponent As System.Object
Dim value As System.Boolean

value = instance.GetComponentsTransformInterference(Component, Transform, InterferingComponent)
```

### C#

```csharp
System.bool GetComponentsTransformInterference(
   System.object Component,
   System.object Transform,
   out System.object InterferingComponent
)
```

### C++/CLI

```cpp
System.bool GetComponentsTransformInterference(
   System.Object^ Component,
   System.Object^ Transform,
   [Out] System.Object^ InterferingComponent
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Component`: Array of [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)s with which to detect interference
- `Transform`: [IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)
- `InterferingComponent`: Array of interfering [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)s

### Return Value

True if successful, false if not

## VBA Syntax

See [InterferenceDetectionMgr::GetComponentsTransformInterference](ms-its:sldworksapivb6.chm::/sldworks~InterferenceDetectionMgr~GetComponentsTransformInterference.html).

## Examples

[Detect Interferences Using a Transform (VBA)](Detect_Interferences_Using_a_Transform_Example_VB.htm)
[Detect Interferences Using a Transform (VB.NET)](Detect_Interferences_Using_a_Transform_Example_VBNET.htm)
[Detect Interferences Using a Transform (C#)](Detect_Interferences_Using_a_Transform_Example_CSharp.htm)

## See Also

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html)
[IInterferenceDetectionMgr::IGetComponentsTransformInterference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetComponentsTransformInterference.html)
[IInterferenceDetectionMgr::GetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceComponents.html)
[IInterferenceDetectionMgr::IGetInterferenceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferenceComponents.html)
[IInterferenceDetectionMgr::GetInterferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferences.html)
[IInterferenceDetectionMgr::IGetInterferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferences.html)
[IInterferenceDetectionMgr::CreateFastenersFolder Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~CreateFastenersFolder.html)
[IInterferenceDetectionMgr::IgnoreHiddenBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IgnoreHiddenBodies.html)
[IInterferenceDetectionMgr::IncludeMultibodyPartInterferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IncludeMultibodyPartInterferences.html)
[IInterferenceDetectionMgr::MakeInterferingPartsTransparent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~MakeInterferingPartsTransparent.html)
[IInterferenceDetectionMgr::NonInterferingComponentDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~NonInterferingComponentDisplay.html)
[IInterferenceDetectionMgr::ShowIgnoredInterferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~ShowIgnoredInterferences.html)
[IInterferenceDetectionMgr::TreatCoincidenceAsInterference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatCoincidenceAsInterference.html)
[IInterferenceDetectionMgr::TreatSubAssembliesAsComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~TreatSubAssembliesAsComponents.html)
[IInterferenceDetectionMgr::GetComponentsTransformInterferenceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetComponentsTransformInterferenceCount.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
